# Home Assistant MCP server

The tool server used by the `control-devices`, `manage-automations` and `query-status` skills. It wraps the Home Assistant REST API.

## Tools

`get_all_states`, `get_state`, `call_service`, `get_services`, `list_automations`, `trigger_automation`, `enable_automation`, `disable_automation`, `send_notification`, `get_history`.

## Setup

1. Install: `pip install -r requirements.txt`
2. In Home Assistant, open your profile and create a **long-lived access token**.
3. Set two environment variables where your MCP client runs the server:
   - `HA_URL`, for example `http://homeassistant.local:8123`
   - `HA_TOKEN`, the token from step 2
4. Add the server to your MCP client. Example (`claude_desktop_config.json` / `.mcp.json` style):

```json
{
  "mcpServers": {
    "home-assistant": {
      "command": "python",
      "args": ["/path/to/ai-skills/tools/home-assistant-mcp/ha_server.py"],
      "env": {
        "HA_URL": "http://homeassistant.local:8123",
        "HA_TOKEN": "<your-long-lived-token>"
      }
    }
  }
}
```

## Security

- The token gives full access to your Home Assistant. Keep it in environment variables or your client's secret store. Never commit it, paste it into chat, or save it in a file in a repo.
- `call_service` with no `entity_id` affects every entity in that domain. The skills ask for confirmation first; keep that behaviour.
- Revoke the token in your Home Assistant profile if it is ever exposed.
