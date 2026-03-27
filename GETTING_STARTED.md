# EvoShield AI - Getting Started Guide

## Welcome to EvoShield AI 🛡️

This guide will walk you through setting up and using your new cybersecurity defense system.

---

## 📋 Prerequisites

- **Python**: 3.8 or higher
- **Operating System**: Windows 7+, macOS 10.12+, or Linux (Ubuntu 16.04+)
- **RAM**: 2 GB minimum (4 GB recommended)
- **Disk Space**: 500 MB for dependencies + application

---

## Step 1: Installation (5 minutes)

### Option A: Standard Installation (Recommended)

```bash
# Navigate to project directory
cd evoshield

# Create virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Option B: Quick Installation

```bash
cd evoshield
pip install -r requirements.txt
python main.py
```

### Option C: Automated Setup

```bash
cd evoshield
python setup.py
```

---

## Step 2: First Launch

When you run `python main.py`, the EvoShield AI window will open:

```
┌─────────────────────────────────────────────────────────────┐
│  EvoShield AI - Cyber Defense System                    □ □ ✕│
├──────────────────────────┬────────────────────────────────┤
│                          │ EvoShield AI Cyber Defense     │
│ Dashboard                │───────────────────────────────│
│                          │                                │
│ Scan System              │ Risk Score  │ Threat Level   │
│                          │ ╔════════╗  │ ● SAFE         │
│ AI Analysis              │ ║        ║  │                │
│                          │ ║  45 %  ║  │ Active Process │
│ Logs                     │ ║        ║  │ 156            │
│                          │ ╚════════╝  │                │
│ Settings                 │                │ AI Prediction│
│                          │ Threat Trend   │ Analyzing... │
│ ● System Active          │ ╭─────────╮   │                │
│                          │ │ ╱╲  ╱╲  │   │                │
│                          │ │╱  ╲╱  ╲ │   │                │
│                          │ ╰─────────╯   │                │
│                          │                │                │
│                          │ Recent Events              │
│                          │ ├─ [14:32] Risk: 45        │
│                          │ ├─ [14:30] Risk: 42        │
│                          │ └─ [14:28] Risk: 40        │
└──────────────────────────┴────────────────────────────────┘
```

---

## Step 3: Dashboard Tour

### Main Dashboard (Default View)

The dashboard displays:

1. **Risk Score Card** (Top Left)
   - Circular progress indicator
   - Shows current risk (0-100%)
   - Updates every 2 seconds

2. **Threat Level Card** (Top Middle)
   - Color-coded threat status
   - Shows: SAFE, LOW, MEDIUM, HIGH, CRITICAL
   - Real-time indicator

3. **Active Processes Card** (Top Right)
   - Current process count
   - System monitoring
   - Large number display

4. **AI Prediction Card** (Far Right)
   - ML model inference
   - Confidence percentage
   - Recommended action

5. **Threat Trend Graph** (Bottom)
   - Real-time line chart
   - Shows risk history
   - 50-point rolling window

6. **Event Log** (Bottom)
   - Recent security events
   - Timestamps included
   - Scrollable history

### Sidebar Navigation

Click any button in the sidebar to switch views:

```
┌─────────────────────┐
│  SIDEBAR OPTIONS    │
├─────────────────────┤
│ ▶ Dashboard         │ ← Main UI view
│ ▶ Scan System       │ ← Run vulnerability scans
│ ▶ AI Analysis       │ ← View threat analysis
│ ▶ Logs              │ ← System event logs
│ ▶ Settings          │ ← Configuration options
├─────────────────────┤
│ ● System Active     │ ← Status indicator
└─────────────────────┘
```

---

## Step 4: Understanding the Threat Levels

```
Risk Score  Threat Level  Color      Meaning            Action
──────────────────────────────────────────────────────────────
0-20        SAFE          Green      No threats         Monitor
20-40       LOW           Yellow     Minor issues       Observe
40-60       MEDIUM        Orange     Notable risks      Alert
60-80       HIGH          Orange-Red Significant risk   Investigate
80-100      CRITICAL      Red        Severe threat      Respond
```

---

## Step 5: Exploring Features

### 1. Dashboard Tab
- **Purpose**: Main security status overview
- **Updates**: Every 2 seconds
- **Shows**: Risk score, threats, processes, AI predictions
- **Graph**: Real-time threat trend visualization

### 2. Scan System Tab
- **Full System Scan**: Comprehensive vulnerability analysis
- **Quick Scan**: Faster scan of critical areas
- **Results**: Detailed scan findings

### 3. AI Analysis Tab
- **Threat Table**: Detailed threat breakdown
- **Model Performance**: ML model statistics
- **Confidence Scores**: ML model prediction confidence

### 4. Logs Tab
- **Event Log**: Complete system events
- **Timestamps**: When events occurred
- **Clear Button**: Reset log display
- **Search**: (Future feature)

### 5. Settings Tab
- **Configuration**: System settings
- **Status**: Build information
- **Version**: Application version

---

## Step 6: Understanding the Core Systems

### Anomaly Detection
Monitors for unusual system patterns:
- **CPU Usage**: Detects abnormal spikes
- **Memory Usage**: Identifies memory leaks/hogging
- **Process Creation**: Tracks unusual process spawning
- **Baseline**: Compares to normal behavior

### Malware Detection
Identifies suspicious patterns:
- **Keyword Matching**: Known malware keywords
- **Signature Database**: 8+ malware types
- **Custom Signatures**: Add your own
- **Severity Scoring**: Risk assessment

### AI Threat Detection
Recognizes behavioral chains:
- **Pattern Recognition**: Detects suspicious sequences
- **Correlation Analysis**: Links related activities
- **Process Monitoring**: Tracks process behavior
- **Adaptive Learning**: Improves over time

### ML Model
Machine learning classification:
- **Text Analysis**: TF-IDF vectorization
- **Classification**: Logistic regression
- **Predictions**: Threat probability
- **Confidence**: Accuracy metrics

### Risk Engine
Unified scoring system:
- **Weighted Scoring**: Combines all modules
- **0-100 Scale**: Easy to understand
- **Threat Mapping**: Associates with threat levels
- **Trend Analysis**: Historical pattern tracking

### Defense System
Response mechanisms:
- **Monitoring**: Continuous system watching
- **Alerts**: Security notifications
- **Blocking**: Threat prevention (simulated)
- **Quarantine**: Isolate suspicious items

---

## Step 7: Real-Time Monitoring

The application updates automatically every 2 seconds:

```
Timeline of Operations:
─────────────────────────────────────────────────
T=0.0s  → Risk score calculated
T=0.1s  → Graph updated
T=0.2s  → Anomaly detection run
T=0.3s  → Malware scanning
T=0.4s  → AI analysis
T=0.5s  → ML prediction
T=1.0s  → Event logged
T=2.0s  → UI refresh complete
        → Cycle repeats
```

---

## Step 8: Customization

### Change Update Frequency
Edit `ui/main_window.py`:
```python
self.timer.start(2000)  # Change 2000 to desired milliseconds
```

### Adjust Component Weights
Edit `core/risk_engine.py`:
```python
self.component_weights = {
    "anomaly_detection": 0.25,      # Adjust these
    "malware_detection": 0.30,
    "ai_threat_detection": 0.25,
    "adaptive_model": 0.20
}
```

### Modify Color Scheme
Edit `ui/styles.qss` or update in `ui/main_window.py`:
```python
background-color: #0f0f1e;  # Dark blue
color: #00ffff;            # Cyan
# ... more colors
```

---

## Step 9: Database & Logging

### What Gets Logged
- Risk scores (every 2 seconds)
- Threat events (when detected)
- Alerts generated
- Scans performed
- Actions taken

### Log Retention
- Risk Scores: 1000 entries (rolling window)
- Threat Events: 500 entries
- Alerts: 500 entries
- Anomalies: 100 entries

### Viewing Logs
1. Click "Logs" in sidebar
2. See complete event history
3. Click "Clear Logs" to reset

---

## Step 10: Troubleshooting

### Issue: Application Won't Start

**Solution 1**: Verify Python version
```bash
python --version  # Should be 3.8+
```

**Solution 2**: Check dependencies
```bash
python -c "import PyQt5, psutil, sklearn; print('OK')"
```

**Solution 3**: Reinstall dependencies
```bash
pip install --upgrade -r requirements.txt
```

### Issue: Missing Dependencies

```bash
pip install PyQt5
pip install psutil
pip install scikit-learn
pip install matplotlib
pip install numpy
```

### Issue: Permission Errors

```bash
pip install --user -r requirements.txt
```

### Issue: Environment Locked

```bash
pip install --break-system-packages -r requirements.txt
```

---

## Step 11: Testing Without GUI

To test core modules without PyQt5:

```bash
python demo.py
```

This runs:
- Malware detection
- Risk scoring
- Threat detection
- System monitoring
- ML model testing
- Defense system testing

---

## Step 12: Building Executable

To create a standalone .exe file:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "EvoShield AI" main.py
```

The executable will be in the `dist/` folder.

---

## Step 13: Performance Tips

### For Low-End Systems
1. Increase timer interval (slower updates)
2. Reduce log retention
3. Disable graph animation
4. Use Quick Scan instead of Full Scan

### For High-Performance Systems
1. Decrease timer interval (faster updates)
2. Increase update frequency
3. Add more monitoring parameters
4. Enable all logging features

---

## Step 14: Security Best Practices

### Safe to Do
✅ Run the application as regular user
✅ Monitor system metrics
✅ View logs and alerts
✅ Adjust settings and weights
✅ Customize detection rules

### Not Needed
❌ Run as administrator (not required)
❌ Disable antivirus (safe to use with others)
❌ Modify system settings

---

## Step 15: Advanced Usage

### Custom Threat Detection
```python
from core import AIThreatDetector
detector = AIThreatDetector()
detector.add_threat_indicator(
    "custom_threat",
    ["pattern1", "pattern2"],
    severity=0.8
)
```

### Model Retraining
```python
from core import AdaptiveModel
model = AdaptiveModel()
model.retrain([
    ("suspicious activity", 1),
    ("normal operation", 0),
])
```

### Custom Signatures
```python
from core import MalwareSimulator
scanner = MalwareSimulator()
scanner.add_signature(
    "custom_malware",
    severity=0.9,
    name="Custom Threat Name"
)
```

---

## Getting Help

1. **Documentation**: Read `README.md`
2. **Quick Reference**: Check `QUICK_REFERENCE.md`
3. **Build Details**: See `BUILD_SUMMARY.md`
4. **Code Comments**: Check module docstrings
5. **Examples**: Run `demo.py`
6. **Testing**: Run `test_core.py`

---

## Keyboard Shortcuts (Future)

```
(Note: Shortcuts not yet implemented)
Ctrl+Q          Quit application
Ctrl+S          Start scan
Ctrl+L          Clear logs
Ctrl+,          Open settings
F1              Help
```

---

## Common Tasks

### View Current Risk Score
Dashboard tab → Risk Score card (top left)

### Run Vulnerability Scan
1. Click "Scan System" in sidebar
2. Click "Start Full System Scan"
3. View results below

### Check System Status
Dashboard tab → Active Processes (top right)

### Review Events
Logs tab → Event Log table

### Change Settings
Settings tab → Configure options

---

## Performance Monitoring

The application can monitor:
- Process count (real-time)
- CPU usage (real-time)
- Memory usage (real-time)
- Risk trends (historical)
- Threat patterns (historical)

All without impacting system performance!

---

## FAQ

**Q: Is this a real antivirus?**
A: No, it's an educational cybersecurity dashboard with simulated threat detection.

**Q: Does it modify my system?**
A: No, all operations are read-only and safe.

**Q: Can I use it with other antivirus software?**
A: Yes, completely safe to use alongside other security tools.

**Q: How often does it update?**
A: By default, every 2 seconds (configurable).

**Q: Can I customize the detection rules?**
A: Yes, all modules support custom configuration.

**Q: How much system resources does it use?**
A: Minimal - typically 50-100 MB RAM, <1% CPU idle.

**Q: Is the source code available?**
A: Yes, fully open-source with complete documentation.

---

## Next Steps

1. ✅ Install the application
2. ✅ Launch `python main.py`
3. ✅ Explore the dashboard
4. ✅ Run a system scan
5. ✅ Review alerts and logs
6. ✅ Customize settings
7. ✅ Read the documentation
8. ✅ Extend with custom modules

---

## Congratulations! 🎉

You now have EvoShield AI installed and ready to use.

**Quick Start:**
```bash
cd evoshield
pip install -r requirements.txt
python main.py
```

**Enjoy your advanced cybersecurity defense system!**

For more information, see the README.md file.

---

**EvoShield AI v1.0.0** - Advanced Cybersecurity Defense System
