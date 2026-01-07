import requests
import serial
import time

# -------- CONFIG --------
API_KEY = "f95e691bf7264fa89b4ebd108935c92d"
NEWS_URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

SERIAL_PORT = "COM9"      # Change this to your Arduino COM port
BAUD_RATE = 9600
UPDATE_INTERVAL = 20      # seconds
MAX_HEADLINES = 5         # how many headlines to cycle
# ------------------------

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # wait for Arduino reset

headlines = []
current_index = 0


def fetch_headlines():
    response = requests.get(NEWS_URL)
    data = response.json()

    temp = []

    if "articles" not in data:
        return temp

    for article in data["articles"][:MAX_HEADLINES]:
        title = article["title"]
        if title:
            title = title.replace("\n", " ")
            title = title[:42]   # SAFE for Arduino UNO  # OLED-safe length
            temp.append(title)

    return temp


while True:
    try:
        # Fetch headlines if list is empty or fully used
        if not headlines or current_index >= len(headlines):
            headlines = fetch_headlines()
            current_index = 0

        if headlines:
            message = f"Breaking News | {headlines[current_index]}"
            print("Sending:", message)
            ser.write((message + "\n").encode())
            ser.flush()
            time.sleep(0.05)
            current_index += 1
        else:
            ser.write(b"No News | Try again\n")

        time.sleep(UPDATE_INTERVAL)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
