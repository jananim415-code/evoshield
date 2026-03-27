# EvoShield AI - Quick Reference Guide

## 🚀 Getting Started (2 Minutes)

### Installation
```bash
cd evoshield
pip install -r requirements.txt
python main.py
```

### If Installation Fails
```bash
pip install --user -r requirements.txt
python main.py
```

---

## 📁 Files & Modules Reference

### Core AI/ML Modules (`core/`)
| File | Purpose | Key Features |
|------|---------|--------------|
| `anomaly_detector.py` | Detects unusual patterns | CPU/Memory/Process anomalies |
| `malware_simulator.py` | Keyword-based detection | 8+ malware types, 20+ keywords |
| `ai_threat_detector.py` | Behavioral analysis | Pattern chains, correlations |
| `adaptive_model.py` | ML classification | TF-IDF + Logistic Regression |
| `risk_engine.py` | Risk scoring | 0-100 scale, threat mapping |
| `defense_system.py` | Alert & response | Monitor, Alert, Block, Quarantine |

### UI Components (`ui/`)
| File | Purpose |
|------|---------|
| `main_window.py` | Dashboard, all UI components |
| `styles.qss` | Dark theme styling |
| `__init__.py` | Module initialization |

### Main Application Files
| File | Purpose |
|------|---------|
| `main.py` | Entry point - run this! |
| `demo.py` | Feature demonstration |
| `test_core.py` | Module testing |
| `setup.py` | Automated setup helper |

### Documentation
| File | Purpose |
|------|---------|
| `README.md` | Complete guide (API, features, usage) |
| `BUILD_SUMMARY.md` | Build details & statistics |
| `requirements.txt` | Python dependencies |

---

## 🎮 Running Different Modes

### Full GUI Application
```bash
python main.py
```

### Run Demo (No GUI needed)
```bash
python demo.py
```

### Test Core Modules
```bash
python test_core.py
```

### Automated Setup
```bash
python setup.py
```

---

## 🔍 Module Usage Examples

### Detect Anomalies
```python
from core.anomaly_detector import AnomalyDetector
detector = AnomalyDetector()
result = detector.analyze_cpu_spike(85.0)
print(f"Anomaly: {result['is_anomaly']}, Severity: {result['severity']}")
```

### Scan for Malware
```python
from core.malware_simulator import MalwareSimulator
scanner = MalwareSimulator()
result = scanner.scan_text("ransomware detected")
print(f"Threat: {result['is_threat']}, Severity: {result['severity']}")
```

### Detect Threat Patterns
```python
from core.ai_threat_detector import AIThreatDetector
detector = AIThreatDetector()
result = detector.detect_repeated_patterns("suspicious_activity")
print(f"Suspicious: {result['is_suspicious']}")
```

### ML Prediction
```python
from core.adaptive_model import AdaptiveModel
model = AdaptiveModel()
pred = model.predict("ransomware attack")
print(f"Threat Level: {pred['threat_level']}, Confidence: {pred['confidence']}")
```

### Calculate Risk Score
```python
from core.risk_engine import RiskEngine
engine = RiskEngine()
risk = engine.calculate_risk_score(0.3, 0.5, 0.2, 0.4)
level = engine.get_threat_level(risk)
print(f"Risk: {risk}/100, Level: {level}")
```

### Generate Alerts
```python
from core.defense_system import DefenseSystem
defense = DefenseSystem()
alert = defense.generate_alert("Trojan", 0.9, "System", "Detected malware")
print(f"Alert: {alert['id']}, Severity: {alert['severity_label']}")
```

---

## 🎨 Dashboard Views

### Main Dashboard
- Risk Score (circular progress 0-100%)
- Threat Level indicator
- Active processes count
- AI prediction results
- Real-time threat graph
- Event log

### Scan System
- Start Full System Scan
- Quick Scan option
- Scan results display

### AI Analysis
- Threat analysis table
- ML model performance
- Detailed threat information

### Logs
- Complete event log
- Timestamps
- Threat categorization
- Clear logs button

### Settings
- System configuration
- Build version
- Update information

---

## ⚙️ Configuration Options

### Update Frequency (main_window.py)
```python
self.timer.start(2000)  # 2 seconds
```

### Risk Weights (risk_engine.py)
```python
self.component_weights = {
    "anomaly_detection": 0.25,
    "malware_detection": 0.30,
    "ai_threat_detection": 0.25,
    "adaptive_model": 0.20
}
```

### Anomaly Threshold (anomaly_detector.py)
```python
def __init__(self, threshold: float = 0.6):
```

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: PyQt5` | `pip install PyQt5` |
| `ModuleNotFoundError: sklearn` | `pip install scikit-learn` |
| `ModuleNotFoundError: psutil` | `pip install psutil` |
| `matplotlib` error | `pip install matplotlib` |
| Permission denied | Use `--user` flag: `pip install --user` |
| Environment locked | Use `--break-system-packages` |

---

## 📊 Risk Scoring Reference

```
Risk Score Calculation:
Risk = (Anomaly × 0.25) + (Malware × 0.30) + (AI × 0.25) + (ML × 0.20)

Threat Levels:
  0-20:   SAFE    ✅ (Green #00ff00)
  20-40:  LOW     ⚠️  (Yellow #ffff00)
  40-60:  MEDIUM  ⚠️  (Orange #ffa500)
  60-80:  HIGH    🔴  (Orange-Red #ff4500)
  80-100: CRITICAL 🔴  (Red #ff0000)
```

---

## 🎯 Component Weights

| Component | Weight | Details |
|-----------|--------|---------|
| Anomaly Detection | 25% | CPU/Memory/Process anomalies |
| Malware Detection | 30% | Keyword-based pattern matching |
| AI Threat Detection | 25% | Behavioral pattern recognition |
| Adaptive ML Model | 20% | Machine learning classification |

---

## 💾 Data Retention

| Data Type | Retention | Limit |
|-----------|-----------|-------|
| Risk Scores | Unlimited | 1000 rolling window |
| Threat Events | Unlimited | 500 most recent |
| Alerts | Unlimited | 500 most recent |
| Quarantined Items | Unlimited | 200 most recent |
| Anomalies | Unlimited | 100 most recent |

---

## 🔐 Security Assurances

✅ **Safe Operations**
- No system modifications
- Read-only monitoring
- No process termination
- No file deletion
- No registry changes

✅ **Detection Only**
- Threat identification
- Pattern recognition
- Risk assessment
- Logging and alerting

---

## 📞 Quick Help

### Check Installation
```bash
python -c "import PyQt5, psutil, sklearn; print('OK')"
```

### View Dependencies
```bash
pip list | grep -E "PyQt5|psutil|scikit|matplotlib|numpy"
```

### Verify Project Structure
```bash
python -c "from core import *; from ui import *; print('Project OK')"
```

---

## 🚀 Next Steps

1. **Install Dependencies**: `pip install -r requirements.txt`
2. **Run Application**: `python main.py`
3. **Explore Features**: Use sidebar to navigate
4. **Review Code**: Check individual modules
5. **Customize**: Modify weights, thresholds, colors

---

## 📚 Further Reading

- **Full Guide**: See `README.md`
- **Build Details**: See `BUILD_SUMMARY.md`
- **Code Docs**: Check module docstrings
- **Examples**: Look at `demo.py` and `test_core.py`

---

**EvoShield AI v1.0.0** | Advanced Cybersecurity Defense System
