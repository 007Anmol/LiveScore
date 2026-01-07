# Live Cricket Score & News Display

A Python-Arduino project that displays live cricket scores and breaking news headlines on an OLED display (128x64).

## 🏏 Features

- **Live Cricket Scores**: Fetches real-time cricket match data from CricAPI
- **Breaking News Headlines**: Displays top news headlines from NewsAPI
- **OLED Display**: Shows data on a 128x64 SSD1306 OLED screen
- **Serial Communication**: Python scripts send data to Arduino via serial port
- **Auto-Refresh**: Updates automatically at configurable intervals

## 📦 Hardware Requirements

- Arduino (Uno/Nano/Mega)
- SSD1306 OLED Display (128x64, I2C)
- USB cable for Arduino connection
- Jumper wires

### Wiring Diagram

| OLED Pin | Arduino Pin |
|----------|-------------|
| VCC      | 5V          |
| GND      | GND         |
| SCL      | A5 (SCL)    |
| SDA      | A4 (SDA)    |

## 💻 Software Requirements

### Python Dependencies

```bash
pip install requests pyserial
```

### Arduino Libraries

Install via Arduino Library Manager:
- Adafruit GFX Library
- Adafruit SSD1306

## 🚀 Setup Instructions

### 1. Arduino Setup

1. Open `score.ino` in Arduino IDE
2. Install required libraries (Adafruit_GFX, Adafruit_SSD1306)
3. Connect your Arduino board
4. Upload the sketch
5. Note the COM port (e.g., COM9)

### 2. Python Setup

1. Create a virtual environment:
   ```bash
   python -m venv env
   ```

2. Activate the virtual environment:
   - Windows:
     ```bash
     env\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source env/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install requests pyserial
   ```

### 3. API Keys Configuration

#### For Cricket Scores (`main.py`):
1. Get a free API key from [CricAPI](https://www.cricapi.com/)
2. Replace `API_KEY` in `main.py` with your key
3. Update `SERIAL_PORT` to match your Arduino port

#### For News Headlines (`alternate.py`):
1. Get a free API key from [NewsAPI](https://newsapi.org/)
2. Replace `API_KEY` in `alternate.py` with your key
3. Update `SERIAL_PORT` to match your Arduino port

## 🎮 Usage

### Run Cricket Score Display

```bash
python main.py
```

### Run News Headlines Display

```bash
python alternate.py
```

**Note**: Only run one script at a time, as both use the same serial port.

## 📁 Project Structure

```
IIOE project/
├── main.py           # Cricket score fetcher
├── alternate.py      # News headlines fetcher
├── score.ino         # Arduino OLED display code
├── .gitignore        # Git ignore file
└── README.md         # Project documentation
```

## ⚙️ Configuration

### main.py (Cricket Scores)
```python
API_KEY = "your_cricapi_key"
SERIAL_PORT = "COM9"    # Change to your port
BAUD_RATE = 9600
UPDATE_INTERVAL = 20    # seconds
```

### alternate.py (News Headlines)
```python
API_KEY = "your_newsapi_key"
SERIAL_PORT = "COM9"    # Change to your port
BAUD_RATE = 9600
UPDATE_INTERVAL = 20    # seconds
MAX_HEADLINES = 5       # Number of headlines to cycle
```

### score.ino (Arduino)
```cpp
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
Serial.begin(9600);
Serial.setTimeout(200);
```

## 🔧 Troubleshooting

### Serial Port Issues
- **Error: "Could not open port"**
  - Make sure Arduino is connected
  - Check COM port in Device Manager (Windows) or `/dev/tty*` (Linux/Mac)
  - Close Arduino IDE Serial Monitor if open
  - Update `SERIAL_PORT` in Python scripts

### OLED Display Issues
- **Nothing showing on OLED**
  - Check wiring connections
  - Verify I2C address (default: 0x3C)
  - Test with example sketch from Adafruit library

### API Issues
- **"No Live Match" or "No News"**
  - Verify API keys are correct
  - Check internet connection
  - Confirm API rate limits not exceeded

## 📊 Data Format

The Python scripts send data to Arduino in the format:
```
Line1 | Line2
```

Example:
- Cricket: `India vs Australia | India won by 5 wickets`
- News: `Breaking News | Major tech company announces breakthrough`

## 📸 Screenshots

*Add your OLED display photos here!*

---

**Happy Coding! 🎉**
