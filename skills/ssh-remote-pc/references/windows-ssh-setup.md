# Setting up SSH access to a Windows PC

Walk the user through these steps in order when they need SSH set up for the
first time. Each step happens on the Windows PC itself (the user will need to
be sitting at it, or connected some other way the first time -- SSH isn't
available yet).

## 1. Enable OpenSSH Server on Windows

1. Open **Settings > System > Optional Features**.
2. Click **Add a feature**, search for "OpenSSH Server", install it.
3. Open **Services** (`services.msc`), find **OpenSSH SSH Server**, set
   **Startup type** to **Automatic**, and start it. Or from an admin
   PowerShell prompt:
   ```powershell
   Set-Service -Name sshd -StartupType Automatic
   Start-Service sshd
   ```
4. Confirm the firewall rule exists (Windows usually adds it automatically):
   ```powershell
   Get-NetFirewallRule -Name *ssh*
   ```
   If missing:
   ```powershell
   New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
   ```

## 2. Find the PC's IP address and username

On the Windows PC, in PowerShell:
```powershell
ipconfig | findstr /i "IPv4"
whoami
```
The IPv4 address is `SSH_HOST` (use the address of your PC on your home network,
since this setup assumes the PC is reachable directly on the same network).
`whoami` gives `SSH_USER` -- typically `DOMAIN\user` or `PCNAME\user`; use just
the part after the backslash.

## 3. Generate an SSH key pair (on the machine that will run Claude/this plugin)

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -C "claude-ssh-remote-pc"
```
Leave a passphrase empty for unattended use, or set one and put it in
`SSH_KEY_PASSPHRASE`.

## 4. Authorize the public key on the Windows PC

Copy the contents of the generated `~/.ssh/id_ed25519.pub`. On the Windows PC,
in an **admin** PowerShell prompt (admin accounts use a different
authorized_keys location than standard users):

For an **administrator** account:
```powershell
Add-Content -Path "$env:ProgramData\ssh\administrators_authorized_keys" -Value "PASTE_PUBLIC_KEY_HERE"
icacls "$env:ProgramData\ssh\administrators_authorized_keys" /inheritance:r /grant "Administrators:F" /grant "SYSTEM:F"
```

For a **standard** account:
```powershell
New-Item -Force -ItemType Directory -Path "$env:USERPROFILE\.ssh"
Add-Content -Path "$env:USERPROFILE\.ssh\authorized_keys" -Value "PASTE_PUBLIC_KEY_HERE"
```

Restart the sshd service after this:
```powershell
Restart-Service sshd
```

## 5. First connection (accepts the host key)

From the machine running Claude/this plugin:
```bash
ssh -i ~/.ssh/id_ed25519 USER@HOST
```
Accept the host key prompt (`yes`) the first time -- this stores it in
`~/.ssh/known_hosts`, which the MCP server requires before it will connect
(it refuses unknown hosts for safety). If this step is skipped, the plugin's
tools will fail with a message asking for it.

## 6. Set the plugin's environment variables

Set these wherever the plugin's MCP server config is configured (see the
plugin README): `SSH_HOST`, `SSH_USER`, `SSH_KEY_PATH` (defaults to
`~/.ssh/id_ed25519`), and optionally `SSH_PORT` (default `22`) and
`SSH_KEY_PASSPHRASE`.

## Troubleshooting

- **Connection refused**: sshd isn't running, or the firewall rule is
  missing -- redo step 1.
- **Permission denied (publickey)**: the public key wasn't added correctly,
  or file permissions on `authorized_keys` are wrong (Windows OpenSSH is
  strict about this for the administrators file -- redo the `icacls` command).
- **Host key verification failed / unknown host**: redo step 5 from the
  correct machine (the one actually running the MCP server, not a different
  laptop).
- **Dynamic IP changing**: if the PC's local IP changes after a reboot, either
  set a static IP/DHCP reservation on the router, or update `SSH_HOST` when it
  changes.
