import time
import requests

def simulate_bot_input():
    url = "https://3d32-104-155-148-192.ngrok-free.app/demo"  # CHANGE this to your deployed URL if needed
    headers = {"Content-Type": "application/json"}

    dummy_payload = {
        "queryResult": {
            "queryText": "52.52,13.41",
            "intent": {
                "displayName": "Cloudcover"
            }
        }
    }

    while True:
        try:
            res = requests.post(url, json=dummy_payload, headers=headers)
            print(f"[Keep-Alive] Sent simulated input: {res.status_code}")
        except Exception as e:
            print(f"[Keep-Alive] Error: {e}")
        time.sleep(600)  # Every 10 minutes

if __name__ == "__main__":
    simulate_bot_input()
