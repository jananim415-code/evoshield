# EvoShield AI - Advanced Cybersecurity Defense System

A modern, professional desktop cybersecurity application with AI/ML-based threat detection, real-time system monitoring, and a futuristic dark-themed dashboard.

## 🎯 Features

✅ **Modern Cybersecurity Dashboard**  
- Professional PyQt5 UI with dark theme (neon blue/green)
- Real-time threat monitoring and visualization
- Multiple dashboard views (Dashboard, Scan, Analysis, Logs, Settings)

✅ **AI/ML Threat Detection**
- TensorFlow-based threat prediction
- LogisticRegression with TF-IDF vectorization for text analysis
- Trained on sample safe/suspicious activity data
- Real-time model inference

✅ **Multi-Module Detection System**
- Anomaly Detection: CPU/Memory/Process anomalies
- Malware Simulator: Keyword-based threat pattern detection
- AI Threat Detector: Behavioral pattern recognition
- Adaptive ML Model: Machine learning-based classification
- Risk Engine: Unified risk scoring (0-100 scale)
- Defense System: Alert generation and threat logging

✅ **Real-Time System Monitoring**
- Process count monitoring (using psutil)
- CPU and memory anomaly detection
- Network anomaly simulation
- Live updates every 2 seconds

✅ **Visualization**
- Real-time line chart (threat trend)
- Circular progress bar (risk score)
- Threat level indicators with color coding
- Event log with timestamp

✅ **Safety First**
- No system modifications
- No process termination
- No file deletion
- Simulation-based threat detection
- Read-only monitoring

## 📁 Project Structure

```
evoshield/
│
├── core/                          # AI/ML and detection modules
│   ├── __init__.py
│   ├── anomaly_detector.py        # Anomaly pattern detection
│   ├── malware_simulator.py       # Keyword-based malware detection
│   ├── ai_threat_detector.py      # Behavioral threat detection
│   ├── adaptive_model.py          # ML-based threat prediction
│   ├── risk_engine.py             # Risk score calculation
│   └── defense_system.py          # Alert/response system
│
├── ui/                            # User Interface components
│   ├── __init__.py
│   ├── main_window.py             # Main window and all UI components
│   └── styles.qss                 # Dark theme stylesheet
│
├── assets/                        # Application assets
│   └── icons/                     # Icon files
│
├── main.py                        # Application entry point
├── requirements.txt               # Python dependencies
├── README.md                      # This file
└── .gitignore                    # Git ignore file
```

## 🚀 Installation

### Requirements
- Python 3.8+
- Windows 7+ / macOS 10.12+ / Linux (Ubuntu 16.04+)

### Step 1: Clone or Download the Project

```bash
cd evoshield
```

### Step 2: Create Virtual Environment (Optional but Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

If you encounter issues with the environment being managed by uv:
```bash
pip install --break-system-packages -r requirements.txt
```

### Step 4: Run the Application

```bash
python main.py
```

## 📦 Dependencies

```
PyQt5==5.15.9               # Desktop UI framework
psutil==5.9.6               # System monitoring
scikit-learn==1.3.2         # Machine learning
matplotlib==3.8.2           # Data visualization
numpy==1.24.3               # Numerical computing
```

## 🖥️ UI Components

### Dashboard Layout
- **Sidebar**: Navigation between Dashboard, Scan, Analysis, Logs, Settings
- **Header**: Application title and status
- **Dashboard Cards**:
  - Risk Score (circular progress 0-100%)
  - Threat Level (SAFE/LOW/MEDIUM/HIGH/CRITICAL)
  - Active Processes (count)
  - AI Prediction (model inference results)
- **Graph**: Real-time threat trend line chart
- **Event Log**: Recent security events with timestamps

### Color Scheme
- Background: `#0f0f1e` (very dark blue)
- Primary: `#1a1a2e` (dark blue)
- Accent: `#0f3460` (blue)
- Highlight: `#00ffff` (cyan)
- Success: `#00ff00` (green)
- Alert: `#ff0000` (red)

### Theme
- Dark mode with neon cyan/green accents
- Rounded corners on all cards
- Smooth animations and transitions
- Professional, futuristic appearance

## 🧠 Core Modules

### 1. **Anomaly Detector** (`core/anomaly_detector.py`)
Detects unusual patterns in system behavior:
- CPU spike detection
- Memory spike detection
- Process creation anomalies
- Baseline deviation analysis

```python
from core import AnomalyDetector
detector = AnomalyDetector()
result = detector.analyze_cpu_spike(cpu_percent=85.0)
```

### 2. **Malware Simulator** (`core/malware_simulator.py`)
Keyword-based threat pattern detection:
- Ransomware detection
- Trojan identification
- Custom signature database
- Process classification

```python
from core import MalwareSimulator
scanner = MalwareSimulator()
result = scanner.scan_text("ransomware cryptolocker detected")
```

### 3. **AI Threat Detector** (`core/ai_threat_detector.py`)
Behavioral pattern recognition:
- Repeated pattern detection
- Behavior chain analysis
- Process-activity correlation
- Custom threat indicators

```python
from core import AIThreatDetector
detector = AIThreatDetector()
result = detector.detect_repeated_patterns("suspicious_activity")
```

### 4. **Adaptive ML Model** (`core/adaptive_model.py`)
Machine learning-based threat prediction:
- TF-IDF vectorization
- Logistic regression classification
- Real-time model inference
- Online learning capability

```python
from core import AdaptiveModel
model = AdaptiveModel()
prediction = model.predict("unusual network activity detected")
```

### 5. **Risk Engine** (`core/risk_engine.py`)
Unified risk scoring system:
- Component weight combination
- Risk trend analysis
- Threat level mapping
- Event logging

```python
from core import RiskEngine
engine = RiskEngine()
risk_score = engine.calculate_risk_score(
    anomaly_score=0.3,
    malware_score=0.5,
    ai_threat_score=0.2,
    model_confidence=0.4
)
```

### 6. **Defense System** (`core/defense_system.py`)
Alert generation and response:
- Real-time monitoring
- Alert generation
- Item quarantine (simulation)
- Action logging

```python
from core import DefenseSystem
defense = DefenseSystem()
alert = defense.generate_alert("Suspicious Process", 0.85, "PID_1234", "Details...")
```

## ⚙️ System Monitoring

The application uses `psutil` to safely monitor system activity:
- Process enumeration (no modification)
- CPU and memory metrics
- Safe read-only operations
- Real-time updates

**All monitoring is read-only - no system modifications occur.**

## 🔄 Real-Time Behavior

The application updates every 2 seconds:
1. **Risk Score Calculation** - All modules contribute to final score
2. **Graph Update** - Threat trend visualization
3. **Event Generation** - Simulated threat detections
4. **AI Analysis** - ML model inference
5. **Alert Generation** - Defense responses

## 📊 Threat Scoring

Risk Score Calculation:
```
Risk Score = (Anomaly × 0.25) + (Malware × 0.30) + (AI Threat × 0.25) + (Model × 0.20)

Threat Levels:
- 0-20:   SAFE    (Green)
- 20-40:  LOW     (Yellow)
- 40-60:  MEDIUM  (Orange)
- 60-80:  HIGH    (Orange-Red)
- 80-100: CRITICAL (Red)
```

## 🔧 Configuration

### Update Frequency
Edit the timer interval in `ui/main_window.py`:
```python
self.timer.start(2000)  # Milliseconds (2 seconds)
```

### Component Weights
Edit weights in `core/risk_engine.py`:
```python
self.component_weights = {
    "anomaly_detection": 0.25,
    "malware_detection": 0.30,
    "ai_threat_detection": 0.25,
    "adaptive_model": 0.20
}
```

### Anomaly Threshold
Edit in `core/anomaly_detector.py`:
```python
def __init__(self, threshold: float = 0.6):
```

## 🏗️ Building Executable

To create a standalone executable using PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "EvoShield AI" main.py
```

The executable will be in the `dist/` folder.

## 🔐 Security Features

✅ **Safe Operation**
- No actual threat execution
- No system modification
- No privilege escalation
- Read-only monitoring

✅ **Advanced Detection**
- Multi-layer threat detection
- ML-based classification
- Behavioral analysis
- Pattern recognition

✅ **Comprehensive Logging**
- All events logged
- Timestamp tracking
- Threat history
- Action audit trail

## 📝 Example Usage

```python
#!/usr/bin/env python3
from core import RiskEngine, DefenseSystem, AnomalyDetector

# Initialize systems
risk_engine = RiskEngine()
defense = DefenseSystem()
anomalies = AnomalyDetector()

# Analyze system
anomaly_score = anomalies.simulate_anomaly_score()
risk = risk_engine.calculate_risk_score(
    anomaly_score, 0.3, 0.2, 0.4
)

# Generate response
if risk > 60:
    alert = defense.generate_alert(
        "High-Risk Threat",
        risk / 100,
        "System",
        f"Risk score: {risk}"
    )
    print(f"Alert: {alert}")
```

## 🐛 Troubleshooting

### PyQt5 Import Error
```bash
# Ensure PyQt5 is installed
pip install --upgrade PyQt5

# For environment management by uv
pip install --break-system-packages PyQt5
```

### Missing Dependencies
```bash
# Reinstall all requirements
pip install -r requirements.txt --force-reinstall
```

### Application Won't Start
1. Verify Python 3.8+ is installed
2. Check all dependencies: `pip list`
3. Ensure you're in the correct directory
4. Try running with verbose output: `python -v main.py`

## 📄 License

This project is provided as-is for educational and demonstration purposes.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Add new threat detection modules
- Enhance the UI

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the code comments
3. Verify all dependencies are installed
4. Ensure Python version compatibility

## 🎓 Educational Value

This project demonstrates:
- Desktop application development with PyQt5
- Machine learning implementation (scikit-learn)
- Real-time system monitoring
- UI/UX design patterns
- Cybersecurity concepts
- Software architecture and design patterns

---

**EvoShield AI v1.0.0** - Advanced Cybersecurity Defense System

Built with Python, PyQt5, and Machine Learning 🚀
