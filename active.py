import time
import requests

def ping_website(url):
    while True:
        try:
            response = requests.get(url)
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error: {e}")
        
        # Wait for 30 seconds before the next ping
        time.sleep(30)

if __name__ == "__main__":
    url = "https://storywriting-ai.onrender.com/"
    print(f"Starting to ping {url} every 30 seconds...")
    ping_website(url)
