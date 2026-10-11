#!/usr/bin/env python3
"""Home Assistant MCP server.

Wraps the Home Assistant REST API as MCP tools for the skills in this repo
(control-devices, manage-automations, query-status).

Required environment variables:
  HA_URL    Base URL of your Home Assistant instance, e.g. http://homeassistant.local:8123
  HA_TOKEN  A long-lived access token from your Home Assistant profile page

Install:  pip install -r requirements.txt
Run:      python ha_server.py   (normally started by your MCP client)
"""

import json
import os
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from typing import Any
from urllib.parse import quote

from mcp.server.fastmcp import FastMCP

HA_URL = os.environ.get("HA_URL", "").rstrip("/")
HA_TOKEN = os.environ.get("HA_TOKEN", "")

mcp = FastMCP("home-assistant")


def _ha_request(method: str, path: str, body: dict | None = None) -> Any:
    if not HA_URL or not HA_TOKEN:
        raise RuntimeError(
            "HA_URL and HA_TOKEN environment variables must be set. "
            "Create a long-lived access token on your Home Assistant profile page."
        )
    headers = {
        "Authorization": f"Bearer {HA_TOKEN}",
        "Content-Type": "application/json",
    }
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(f"{HA_URL}/api{path}", data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read().decode()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"Home Assistant API error {e.code}: {e.read().decode()}")


# -- State tools -------------------------------------------------------------

@mcp.tool()
def get_all_states(domain: str = "") -> str:
    """List entity states (entity_id, state, friendly name), optionally filtered by domain.
    Domain examples: light, switch, climate, sensor, binary_sensor, cover, fan, media_player."""
    states = _ha_request("GET", "/states")
    if domain:
        states = [s for s in states if s["entity_id"].startswith(f"{domain}.")]
    summary = [
        {
            "entity_id": s["entity_id"],
            "state": s["state"],
            "friendly_name": s.get("attributes", {}).get("friendly_name", ""),
        }
        for s in states
    ]
    return json.dumps(summary, indent=2)


@mcp.tool()
def get_state(entity_id: str) -> str:
    """Return the full state and attributes of one entity, e.g. light.living_room."""
    return json.dumps(_ha_request("GET", f"/states/{quote(entity_id, safe='.')}"), indent=2)


# -- Service tools -----------------------------------------------------------

@mcp.tool()
def call_service(domain: str, service: str, entity_id: str = "", extra: str = "") -> str:
    """Call a Home Assistant service to control a device.

    domain:    e.g. light, switch, climate, cover, fan, media_player, scene, script
    service:   e.g. turn_on, turn_off, toggle, set_temperature
    entity_id: target entity. If blank, the call targets every entity in the domain,
               so confirm with the user before leaving it blank.
    extra:     JSON string with more service data, e.g. {"brightness_pct": 50}
    """
    body: dict = {}
    if entity_id:
        body["entity_id"] = entity_id
    if extra:
        try:
            body.update(json.loads(extra))
        except json.JSONDecodeError:
            return f"Error: 'extra' must be valid JSON. Got: {extra}"
    return json.dumps(_ha_request("POST", f"/services/{quote(domain)}/{quote(service)}", body), indent=2)


@mcp.tool()
def get_services(domain: str = "") -> str:
    """List available services (domain, service, description), optionally for one domain."""
    services = _ha_request("GET", "/services")
    if domain:
        services = [s for s in services if s.get("domain") == domain]
    summary = [
        {"domain": svc.get("domain", ""), "service": name, "description": info.get("description", "")}
        for svc in services
        for name, info in svc.get("services", {}).items()
    ]
    return json.dumps(summary, indent=2)


# -- Automation tools --------------------------------------------------------

@mcp.tool()
def list_automations() -> str:
    """List automations with entity_id, friendly name, state (on/off) and last_triggered."""
    states = _ha_request("GET", "/states")
    automations = [
        {
            "entity_id": s["entity_id"],
            "friendly_name": s.get("attributes", {}).get("friendly_name", s["entity_id"]),
            "state": s["state"],
            "last_triggered": s.get("attributes", {}).get("last_triggered"),
        }
        for s in states
        if s["entity_id"].startswith("automation.")
    ]
    return json.dumps(automations, indent=2)


@mcp.tool()
def trigger_automation(entity_id: str) -> str:
    """Manually trigger an automation, e.g. automation.morning_routine."""
    return json.dumps(_ha_request("POST", "/services/automation/trigger", {"entity_id": entity_id}), indent=2)


@mcp.tool()
def enable_automation(entity_id: str) -> str:
    """Enable an automation that is currently disabled."""
    return json.dumps(_ha_request("POST", "/services/automation/turn_on", {"entity_id": entity_id}), indent=2)


@mcp.tool()
def disable_automation(entity_id: str) -> str:
    """Disable an automation so it no longer runs automatically."""
    return json.dumps(_ha_request("POST", "/services/automation/turn_off", {"entity_id": entity_id}), indent=2)


# -- Notification tool -------------------------------------------------------

@mcp.tool()
def send_notification(message: str, title: str = "Assistant", target: str = "") -> str:
    """Send a notification through Home Assistant's notify service.
    target is the notify service suffix, e.g. mobile_app_my_phone. Blank uses notify.notify."""
    service = target or "notify"
    body = {"message": message, "title": title}
    return json.dumps(_ha_request("POST", f"/services/notify/{quote(service)}", body), indent=2)


# -- History tool ------------------------------------------------------------

@mcp.tool()
def get_history(entity_id: str, hours: int = 24) -> str:
    """State history for one entity over the last N hours (default 24)."""
    start = (datetime.now(timezone.utc) - timedelta(hours=hours)).isoformat()
    path = f"/history/period/{quote(start)}?filter_entity_id={quote(entity_id)}&minimal_response=true"
    return json.dumps(_ha_request("GET", path), indent=2)


if __name__ == "__main__":
    mcp.run()
