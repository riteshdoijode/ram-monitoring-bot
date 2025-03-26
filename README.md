# Ram-Monitoring-Bot

This Python script monitors the RAM usage of a NextCloud server and sends alerts via Telegram when memory usage is below a specified threshold. It also sends periodic status updates every 12 hours.

## Features
1. Real-time RAM Monitoring: Continuously checks system memory usage.
2. Telegram Notifications: Sends alerts when RAM usage drops below the defined threshold.
3. Scheduled Status Updates: Every 12 hours, the bot sends a report on current RAM usage.

## Requirements
Ensure you have the following installed
Python 3.x
pustil (pip install psutil)
requests (pip install requests)

## Configuration

Update the following variales in the Scirpt

```
telegram_bot_token = "YOUR_TELEGRAM_BOT_TOKEN"  
chat_id = "YOUR_TELEGRAM_CHAT_ID"  
ram_threshold_gb = 4  # Adjust as needed  
```

## Usage

Clone this repositroy: 
```
git clone https://github.com/your-username/your-repo-name.git  
cd your-repo-name  
```

## Install Dependencies:
```
pip install -r requirements.txt
```

## Security Note
Do not share your bot token publicly. Use Environment vairales or a .env file to store sensitive information.
