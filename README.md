# 📡 Arduino Radar with HC-SR04 & Python Visualization

A real-time radar system using Arduino, HC-SR04 ultrasonic sensor, servo motor, and Python visualization. This project creates an interactive radar display that detects objects and visualizes them in a PyGame interface.

## 🎥 Demo Video
**Watch the project in action!** Our TikTok video showing the radar system detecting objects has gained over 50,000 views!

👉 [Watch on TikTok](https://vm.tiktok.com/ZMDdjPMwC/)


## ✨ Features
- **Real-time Object Detection**: HC-SR04 sensor detects objects within 20cm range
- **180° Scanning**: Servo motor provides full horizontal scanning
- **Interactive Visualization**: PyGame radar display with sweep animation
- **Fading History**: Object detection points fade over time for tracking
- **Serial Communication**: Real-time data transfer between Arduino and Python

## 🛠️ Hardware Requirements
- Arduino Uno (or compatible)
- HC-SR04 Ultrasonic Sensor
- SG90 Servo Motor
- Jumper Wires
- Breadboard

## 📦 Software Requirements
- Arduino IDE
- Python 3.8+
- Required Python packages:
  ```bash
  pip install pygame pyserial
  ```

## 🔧 Installation & Setup

### 1. Arduino Setup
Connect the hardware:
- **Servo**: Signal → Pin 9, VCC → 5V, GND → GND
- **HC-SR04**: TRIG → Pin 10, ECHO → Pin 11, VCC → 5V, GND → GND

Upload `servo_and_hcsr04.ino` to your Arduino.

Open Serial Monitor (9600 baud) to verify readings.

### 2. Python Setup
Install dependencies:
```bash
pip install -r requirements.txt
```

Update the COM port in `radar_display.py`:
```python
PORT_NAME = "COM3"  # Change to your Arduino port
```

Run the visualization:
```bash
python radar_code.py
```

## 📁 Project Structure
```
├── arduino/
│   └── servo_and_hcsr04.ino      # Arduino code for sensor & servo control
├── python/
│   └── radar_code.py          # Python PyGame radar visualization
├── requirements.txt              # Python dependencies
├── LICENSE                       # Project license
└── README.md                     # This documentation
```

## 🚀 How It Works

### Arduino Side:
- Servo motor sweeps from 0° to 180°
- At each angle, HC-SR04 measures distance
- Data (angle,distance) is sent via Serial
- Format: "45,15" (angle in degrees, distance in cm)

### Python Side:
- Reads serial data from Arduino
- Displays real-time radar interface
- Shows sweep line and detected objects
- Maintains fading history of detections

## 🎮 Controls
- The radar runs automatically
- Close the PyGame window to exit
- No manual controls needed

## 📊 Technical Details
- **Scan Range**: 0° to 180°
- **Detection Range**: 2cm to 20cm
- **Update Rate**: 30 FPS visualization
- **Communication**: 9600 baud serial
- **Resolution**: 800×450 display

## 🤝 Contributing
Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Submit a Pull Request

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments
- Thanks to all 50K+ viewers on TikTok for your amazing support!
- Arduino community for excellent documentation
- PyGame developers for the game framework

## 📬 Contact
Have questions or suggestions? Reach out via:

- **Email**: 📧 victoria.ashford54@gmail.com
- **WhatsApp**: 📱 +380-99-792-43-19
- **Telegram**: 💬 @Victory_Overflow

You can also open an issue in the repository for technical questions.


