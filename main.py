import requests
import serial
import time

# -------- CONFIG --------
API_KEY = "30f1320d-31f5-44fd-8d52-0e02a9963edc"
API_URL = f"https://api.cricapi.com/v1/currentMatches?apikey={API_KEY}&offset=0"

SERIAL_PORT = "COM9"   # change this
BAUD_RATE = 9600

# ------------------------

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # wait for Arduino reset

def fetch_score():
    response = requests.get(API_URL)
    data = response.json()

    if "data" not in data or len(data["data"]) == 0:
        return "No Live Match"

    match = data["data"][0]

    team1 = match["teams"][0]
    team2 = match["teams"][1]
    status = match["status"]

    return f"{team1} vs {team2} | {status}"

while True:
    try:
        score = fetch_score()
        print("Sending:", score)
        ser.write((score + "\n").encode())
        time.sleep(20)
    except Exception as e:
        print("Error:", e)
        time.sleep(5)
