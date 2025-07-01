
<h1>iTerm2 Discord Rich Presence</h1>

Terminal-Rich-Presence is a simple Python script that integrates your terminal activity with Discord Rich Presence. It updates your Discord status when iTerm2 is running, displaying details like the shell in use and the duration of the session.


  
![image](https://github.com/user-attachments/assets/8daccfad-09d7-4a7b-9258-421f486ce040)


## Features

- Automatically detects when iTerm2 is running
- Shows current shell (zsh, bash, etc.) and session duration
- Lightweight with minimal resource usage

## Installation

### Prerequisites

- macOS with iTerm2
- Python 3.x
- Discord application

### Setup

1. **Clone and install dependencies**
   ```bash
   git clone https://github.com/yourusername/iterm2-discord-rich-presence.git
   cd iterm2-discord-rich-presence
   pip3 install psutil pypresence
   ```

2. **Create shell wrapper**
   ```bash
   mkdir -p ~/bin
   cat > ~/bin/iterm2-discord.sh << 'EOF'
   #!/bin/bash
   cd ~/path/to/iterm2-discord-rich-presence
   python3 main.py &
   EOF
   chmod +x ~/bin/iterm2-discord.sh
   ```

3. **Auto-start on login**
   
   Add to your `~/.zprofile`:
   ```bash
   echo "~/bin/iterm2-discord.sh" >> ~/.zprofile
   ```

## Usage

The script runs automatically in the background once set up. Your Discord status will update when iTerm2 is active, showing:
- Current shell being used
- Session duration
- "Running on iTerm2" status

## Troubleshooting

**Discord not showing status:**
- Ensure Discord is running and not in invisible mode
- Check Discord Application ID is correct
- Enable Rich Presence in Discord settings

**Script not auto-starting:**
- Verify wrapper script path in `.zprofile`
- Test wrapper script manually: `~/bin/iterm2-discord.sh`
- Check script has execute permissions
