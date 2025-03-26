import psutil
import requests
import time

# Set your Telegram bot token and chat ID
telegram_bot_token = "Your Telegram Bot Token"
chat_id = "Your Telegram Bot Chat ID"

# Threshold for RAM usage in GB
ram_threshold_gb = 4 

def send_telegram_message(message):
    api_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    try:
        response = requests.post(api_url, params=params)
        if response.status_code == 200:
            print("Telegram message sent successfully.")
        else:
            print("Failed to send Telegram message. Status code:", response.status_code)
    except requests.RequestException as e:
        print("Error sending Telegram message:", e)

send_telegram_message("The nextcloud server program has started")

def monitor_ram():
    last_status_update = time.time()

    while True:
        current_time = time.time()
        # Send a status update every 12 hours
        if current_time - last_status_update >= 12 * 60 * 60:
            ram_info = psutil.virtual_memory()
            ram_used_gb = ram_info.used / (1024 ** 3)
            message = f"NextCloud server is on. Current RAM usage: {ram_used_gb:.2f} GB"
            send_telegram_message(message)
            last_status_update = current_time

        ram_info = psutil.virtual_memory()
        ram_used_gb = ram_info.used / (1024 ** 3)

        if ram_used_gb < ram_threshold_gb:
            message = f"NextCloud server RAM usage is below the recommended value. Current usage: {ram_used_gb:.2f} GB"
            send_telegram_message(message)

        # Check every 5 minutes (adjust the interval as needed)
        time.sleep(300)

if __name__ == "__main__":
    monitor_ram()
