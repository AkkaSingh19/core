import subprocess
import time

import requests
from decouple import config

BOT_TOKEN = config("BOT_TOKEN")


def start_django():
    print("Starting Django server...")
    return subprocess.Popen(["python", "manage.py", "runserver"])


def start_ngrok():
    print("Starting ngrok tunnel...")
    return subprocess.Popen(["ngrok", "http", "8000"])


def get_ngrok_url():
    retries = 0
    while retries < 10:
        try:
            response = requests.get("http://127.0.0.1:4040/api/tunnels")
            tunnels = response.json()["tunnels"]
            for tunnel in tunnels:
                if tunnel["proto"] == "https":
                    public_url = tunnel["public_url"]
                    return public_url
        except Exception:
            pass
        retries += 1
        print("Waiting for ngrok to be ready...")
        time.sleep(2)
    raise Exception("Ngrok tunnel not found after waiting.")


def set_webhook(public_url):
    webhook_url = f"{public_url}/webhook/"
    telegram_api = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"
    response = requests.get(telegram_api, params={"url": webhook_url})
    print("Webhook response:", response.json())


if __name__ == "__main__":
    django_proc = start_django()
    time.sleep(2)  # Give Django time to start

    ngrok_proc = start_ngrok()
    time.sleep(5)  # Give ngrok time to fully initialize

    try:
        public_url = get_ngrok_url()
        print(f"Ngrok URL detected: {public_url}")
        set_webhook(public_url)
        print("Webhook updated successfully.")

        print("Everything is up and running now!")

        # Keep running until user interrupts
        django_proc.wait()
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        ngrok_proc.terminate()
        django_proc.terminate()
