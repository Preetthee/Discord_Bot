# Discord Bot - MICA

## Overview
This is a Discord bot named MICA designed to help with server management and moderation. The bot is written in Python using the discord.py library and runs on Python 3.11.

## Purpose
- Server moderation (content filtering)
- Member welcome messages
- Role assignment functionality
- Custom commands for server interaction

## Current State
The bot is fully functional and ready to use. It connects to Discord using a bot token stored in Replit Secrets.

## Recent Changes (October 8, 2025)
- Set up Python 3.11 environment
- Installed discord.py, python-dotenv, and Flask dependencies
- Fixed incomplete `assign` command with proper role assignment logic and error handling
- Added Flask web server on port 5000 for status monitoring and uptime pings
- Configured Discord Bot workflow to run with console output
- Updated .gitignore for Python project best practices
- Added DISCORD_TOKEN to Replit Secrets

## Project Architecture

### Main Components
- **main.py**: Main bot file containing all bot logic, events, commands, and Flask web server
- **requirements.txt**: Python dependencies (discord.py, python-dotenv, flask)
- **discord.log**: Bot logging output (gitignored)

### Bot Configuration
- **Command Prefix**: `+=`
- **Intents**: Default + Message Content + Members
- **Log Level**: DEBUG (written to discord.log)

### Features

#### Events
1. **on_ready**: Logs when bot successfully connects
2. **on_member_join**: Sends welcome DM to new members
3. **on_message**: Content moderation (filters inappropriate language)

#### Commands
1. **+=hello**: Greets the user who invoked the command
2. **+=assign <role_name>**: Assigns a specified role to the user
   - Validates role exists in the server
   - Handles permission errors gracefully
   - Only works in server channels (not DMs)

### Environment Variables
- **DISCORD_TOKEN**: Bot authentication token (stored in Replit Secrets)

### Workflows
- **Discord Bot**: Runs `python main.py` with console output
  - Status: Running
  - Output: Console logs showing bot status and events

### Web Server
- **Port**: 5000
- **Endpoint**: `/` - Returns "Bot is alive!" status message
- **Purpose**: Status monitoring and uptime ping endpoint for services like UptimeRobot
- **Implementation**: Flask server running in a separate thread alongside the Discord bot

## Dependencies
- discord.py (2.6.3): Discord API wrapper
- python-dotenv (1.1.1): Environment variable management
- flask (3.1.2): Web server for status endpoint
- Python 3.11: Runtime environment

## How to Use

### Running the Bot
The bot automatically starts via the configured workflow. To manually restart:
1. Stop the current workflow
2. Run `python main.py`

### Adding the Bot to Your Server
1. Go to Discord Developer Portal
2. Select your application
3. Navigate to OAuth2 → URL Generator
4. Select scopes: `bot`
5. Select permissions: `Manage Roles`, `Send Messages`, `Manage Messages`
6. Use the generated URL to invite the bot

### Using Commands
- `+=hello` - Bot will greet you
- `+=assign <role_name>` - Assigns the specified role to you (must match exact role name)

## User Preferences
None documented yet.

## Notes
- The bot requires Message Content Intent to be enabled in Discord Developer Portal
- The bot requires Members Intent for welcome messages to work
- Role assignment requires the bot's role to be higher than the role being assigned
- Content moderation is currently case-insensitive and filters specific words
