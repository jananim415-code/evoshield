# 🖥️ EvoShield AI - Desktop Application Guide

## Quick Start

### Launch the Application
Simply run:
```bash
python main.py
```

A **new desktop window** will open with the full EvoShield AI dashboard.

---

## What Happens When You Run It

### 1. **Application Starts**
```bash
$ python main.py
======================================================================
 EvoShield AI - Launching Desktop Application
======================================================================

✓ Initializing application...
✓ Application initialized
✓ Creating main window...
✓ Showing window...

======================================================================
 Application is now running!
 Check the 'EvoShield AI' window that opened on your desktop
======================================================================
```

### 2. **Desktop Window Opens**
A new window titled **"EvoShield AI - Advanced Cyber Defense System"** appears with:
- Modern dark theme (dark blue/cyan colors)
- Left sidebar navigation
- Main dashboard with real-time metrics
- Multiple tabs for different functions

### 3. **Dashboard Shows Live Data**
The dashboard automatically displays:
- **Risk Score**: 0-100 circular progress indicator
- **Threat Level**: Color-coded status (🟢 SAFE, 🟡 MEDIUM, 🔴 CRITICAL)
- **Active Processes**: Number of running system processes
- **AI Prediction**: Current threat assessment
- **Real-time Graph**: Threat trend visualization (updates every 2 seconds)
- **Event Log**: Latest security events

---

## 🎮 Dashboard Features

### **Navigation Sidebar**
Click any button to navigate:
1. **Dashboard** - Main overview with real-time metrics
2. **Scan System** - Run threat scans
3. **AI Analysis** - Advanced threat analysis
4. **Logs** - View all security events
5. **Settings** - Application configuration

### **Dashboard Tab**
- **Risk Score Card**: Visual circular indicator showing current risk (0-100)
- **Threat Level Card**: Shows threat classification
- **Active Processes**: Number of running processes
- **AI Prediction**: ML model threat assessment
- **Threat Trend Graph**: Real-time chart of risk scores
- **Recent Events**: Latest security log entries

### **Scan System Tab**
Two scanning options:

#### Full System Scan
```
Scans all threat detection modules:
  ✓ Anomaly Detection
  ✓ Malware Analysis
  ✓ AI Threat Detection
  ✓ ML Model Analysis

Provides: Detailed threat report with severity scores
Time: 5-10 seconds
```

#### Quick Scan
```
Fast malware and anomaly check
Time: 2 seconds
Good for: Regular monitoring
```

**Click buttons to run scans** - Results appear in the panel below

### **AI Analysis Tab**
- Threat analysis results table
- ML model performance metrics
- Detection confidence scores
- Suggested actions for threats

### **Logs Tab**
- Complete security event history
- Timestamps for all activities
- Search and filter options
- Clear button to reset logs

### **Settings Tab**
- Application configuration
- Monitoring options
- Update information
- Model training status

---

## 🔄 Real-Time Updates

The dashboard automatically updates **every 2 seconds**:
- Risk score recalculates
- Graph adds new data point
- Event log shows new entries
- Threat indicators refresh

No manual action needed - everything updates automatically while the app runs.

---

## 🎯 Core Features in Action

### Threat Detection
The application monitors for:
1. **Anomalies** - Unusual CPU/memory patterns
2. **Malware** - Known threat signatures
3. **AI-Based Threats** - Behavioral pattern analysis
4. **ML Predictions** - Machine learning model assessment

### Risk Scoring
Each detection module contributes:
- Anomaly Detection: 25%
- Malware Detection: 30%
- AI Threat Analysis: 25%
- ML Model: 20%
- **Total: 0-100 Risk Score**

### Threat Levels
```
Risk Score 0-20   → 🟢 SAFE
Risk Score 21-40  → 🟡 LOW
Risk Score 41-60  → 🟡 MEDIUM
Risk Score 61-85  → 🟠 HIGH
Risk Score 86-100 → 🔴 CRITICAL
```

---

## 🖱️ Interactive Elements

### Buttons You Can Click
- **Start Full System Scan** - Run comprehensive threat analysis
- **Quick Scan** - Fast threat check
- **Clear Logs** - Reset event log display
- **Navigation buttons** - Switch between pages

### Real-Time Displays
- Risk score updates automatically
- Graph adds points every 2 seconds
- Event log shows new entries
- Threat level indicators change with risk

---

## 🔧 Technical Details

### Window Properties
- **Size**: 1600x1000 pixels (configurable)
- **Style**: Fusion (modern cross-platform)
- **Theme**: Dark mode with cyan accent colors
- **Rendering**: AntiAliasing enabled for smooth visuals

### Backend Integration
All UI components connect to core modules:
```
UI Dashboard
    ↓
┌─────────────────────────────────────┐
│ Risk Engine (calculates final score) │
└─────────────────────────────────────┘
    ↓
┌──────────────────────────────────────────────────────────┐
│ AnomalyDetector │ MalwareSimulator │ AIThreatDetector │
│      25%        │      30%         │       25%        │
└──────────────────────────────────────────────────────────┘
```

### Performance
- Dashboard updates: Every 2 seconds
- Memory usage: ~100-150 MB
- CPU impact: < 5% (minimal)
- Responsive UI: Smooth interactions

---

## ⚠️ Troubleshooting

### Window Doesn't Open
**Problem**: Application starts but no window appears
**Solution**:
1. Check that PyQt5 is installed: `pip install PyQt5`
2. Check that PyQtChart is installed: `pip install PyQtChart`
3. Try running with: `python main.py`

### Application Crashes
**Problem**: Window opens but closes immediately
**Solution**:
```bash
# Test imports
python -c "from ui.main_window import EvoShieldWindow; print('OK')"

# Check core modules
python -c "from core import *; print('OK')"

# Run with error details
python main.py  # Check error output
```

### Missing Dependencies
**Solution**: **Install all required packages**:
```bash
pip install PyQt5 PyQtChart psutil scikit-learn matplotlib numpy
```

Or use the setup script:
```bash
python setup.py
```

### Slow Updates
**Problem**: Dashboard updates slowly or freezes
**Solution**:
1. Close other applications to free resources
2. The 2-second update interval is intentional
3. Application should be responsive despite updates

---

## 🎨 Customization

### Change Update Speed
Edit `ui/main_window.py`, find:
```python
self.timer.start(2000)  # Update every 2000ms
```

Change to:
```python
self.timer.start(1000)  # Update every 1000ms (1 second)
```

### Change Window Size
Edit `ui/main_window.py`, find:
```python
self.setGeometry(100, 100, 1600, 1000)
```

Change dimensions (width x height):
```python
self.setGeometry(100, 100, 1920, 1080)  # Larger
self.setGeometry(100, 100, 1280, 800)   # Smaller
```

### Change Dark Theme Colors
Edit `ui/main_window.py` and adjust these colors:
```python
# Background
background-color: #0f0f1e;  # Dark blue

# Highlight
color: #00ffff;  # Cyan

# Success
color: #00ff00;  # Green
```

---

## 📊 Understanding the Dashboard

### Risk Score Visualization
The circular progress bar shows:
- **Center number**: Risk score (0-100)
- **Blue circle**: Background
- **Cyan arc**: Current risk level
- Updates every 2 seconds

### Threat Trend Graph
The line chart displays:
- **X-axis**: Time (latest 50 measurements)
- **Y-axis**: Risk score (0-100)
- **Line**: Risk trend over time
- **Updates**: Every 2 seconds

### Event Log
Shows recent events in format:
```
[14:32:45] Risk: 45 | Processes: 276 | Detected: Trojan.Win32
[14:32:43] Risk: 42 | Processes: 274
[14:32:41] Risk: 40 | Processes: 273
```

---

## 🚀 Advanced Usage

### Run with Python Debug Output
```bash
python -u main.py
```

### Run in Separate Terminal
```bash
# Terminal 1: Monitor output
python main.py

# Terminal 2: Check logs programmatically
python -c "import os; print(open('logs/system.log').read())"
```

### Integrate with Scripts
```python
from ui.main_window import EvoShieldWindow
from PyQt5.QtWidgets import QApplication

app = QApplication([])
window = EvoShieldWindow()
window.show()

# Access core modules from your code
print(window.risk_engine.calculate_risk_score(30, 40, 35, 0.8))
```

---

## ✅ Verification Checklist

Before running the application, ensure:

- [ ] PyQt5 is installed: `pip install PyQt5`
- [ ] PyQtChart is installed: `pip install PyQtChart`
- [ ] Core modules exist: `ls core/*.py`
- [ ] UI module exists: `ls ui/*.py`
- [ ] All imports work: `python -c "from ui.main_window import EvoShieldWindow"`

All checked? Then run:
```bash
python main.py
```

And enjoy your EvoShield AI desktop application! 🛡️

---

## 📝 Notes

- The application runs in the foreground (terminal stays active)
- All threat detection is simulated (safe read-only operation)
- No system permissions required (pure monitoring)
- Close the window to exit the application

---

## 🆘 Support

If you encounter issues:

1. Read this guide completely
2. Check troubleshooting section above
3. Verify all dependencies: `python setup.py`
4. Look at error messages in terminal
5. Try the CLI version: `python cli.py` (if GUI fails)

---

## 🎉 Success!

When working correctly, you should see:
- ✅ Application window opens immediately
- ✅ Dashboard shows risk score and threat level
- ✅ Real-time graph updates every 2 seconds
- ✅ Event log shows new entries
- ✅ All buttons respond to clicks
- ✅ No terminal errors

**Enjoy your professional cybersecurity dashboard!** 🛡️
