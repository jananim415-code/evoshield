# EvoShield AI - Running Guide (IMPORTANT)

## ✨ Good News!

Your EvoShield AI now has **TWO operational modes**:

### 1. **GUI Mode** (Beautiful Desktop Dashboard)
### 2. **CLI Mode** (Terminal Dashboard - Works Immediately)

If PyQt5 has issues, the application automatically falls back to CLI mode!

---

## 🚀 Quick Start (Choose One)

### Option A: Run Main Application (Auto-Smart Mode)
```bash
cd c:\Users\chandu\Downloads\evoshield
python main.py
```
**What happens:**
- ✅ Tries to launch GUI (PyQt5 dashboard)
- ✅ If GUI fails, automatically falls back to CLI
- ✅ Full features available in both modes

### Option B: Run CLI Mode Directly (Guaranteed to Work)
```bash
cd c:\Users\chandu\Downloads\evoshield
python cli.py
```
**Available Immediately:**
- ✅ Full terminal dashboard
- ✅ All threat detection features
- ✅ Real-time monitoring
- ✅ No GUI dependencies
- ✅ Works 100% on all systems

### Option C: Run Demo (No Installation Required)
```bash
python demo.py
```
**Quick feature demonstration without interactive dashboard**

---

## 📊 Both Modes Feature Comparison

| Feature | GUI Mode | CLI Mode |
|---------|----------|----------|
| **Threat Detection** | ✅ Full | ✅ Full |
| **Real-time Graphs** | ✅ Interactive | ✅ ASCII Trend |
| **Risk Scoring** | ✅ Circular Progress | ✅ Text Display |
| **ML Analysis** | ✅ Full | ✅ Full |
| **System Monitoring** | ✅ Live | ✅ Live |
| **Alert System** | ✅ Full | ✅ Full |
| **Logs Viewer** | ✅ Full | ✅ Full |
| **Settings** | ✅ Full | ✅ Full |
| **Works Immediately** | ❓ Requires PyQt5 | ✅ Always |

---

## 📖 CLI Mode - Menu Navigation

Once you run the CLI, you'll see:

```
╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║         E v o S h i e l d   A I   -   C L I   V e r s i o n        ║
║                                                                       ║
║            Advanced Cybersecurity Defense System                      ║
║              Threat Detection | Risk Analysis | Defense              ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝

SYSTEM STATUS
═══════════════════════════════════════════════════════════════════════
  Timestamp:         2024-01-15 14:32:45
  Active Processes:  276
  CPU Usage:         23.5%
  Memory Usage:      62.3%

... [More details] ...

MENU
─────────────────────────────────────────────────────────────────────
  1) Dashboard    2) Threat Scan   3) ML Analysis
  4) Logs         5) Settings      0) Exit
─────────────────────────────────────────────────────────────────────

Select option:
```

### Menu Options Explained

| Option | Feature | What It Does |
|--------|---------|--------------|
| **1** | Dashboard | Main status display (Risk, Threats, Metrics) |
| **2** | Threat Scan | Run system vulnerability scan |
| **3** | ML Analysis | View ML model predictions |
| **4** | Logs | Review security event logs |
| **5** | Settings | View configuration & system info |
| **0** | Exit | Safely exit application |

---

## 🖼️ What You'll See in CLI Dashboard

### Risk Assessment Section
```
RISK ASSESSMENT
═══════════════════════════════════════════════════════════════════════
  Risk Score:      45/100
  Threat Level:    🟡 MEDIUM

  Component Analysis:
    • Anomaly Detection:    30.2%
    • Malware Detection:    45.1%
    • AI Threat Analysis:   35.5%
    • ML Model Confidence:  40.3%
```

### Threat Trend Graph
```
RISK TREND (Last 50 readings)
═══════════════════════════════════════════════════════════════════════
  ▁▁▅▅██▆▆▅▅▄▄▃▃▂▂▁▁▂▂▃▃▄▄▅▅▆▆██░░░░░░░░░░░░
  Low (15) → High (78)
```

### Detected Threats
```
DETECTED THREATS
═══════════════════════════════════════════════════════════════════════
  • Ransomware (Severity: 0.85)
  • Spyware (Severity: 0.65)
```

---

## 🔧 Troubleshooting

### I'm Getting a DLL Error When Running `python main.py`

**This is expected!** The DLL error is a PyQt5 Windows compatibility issue.

**Solution:** Simply run the CLI version:
```bash
python cli.py
```

### I Want to Use GUI Mode Instead

**Option 1:** Try PyInstaller
```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

**Option 2:** Use alternative PyQt5 installation
```bash
pip uninstall PyQt5 -y
pip install PyQt5==5.15.6
python main.py
```

### CLI Mode is Freezing/Hanging

**Solution:** Press `Ctrl+C` to exit and try again

### Colors Not Working in Terminal

**This is normal!** The CLI auto-detects color support. If your terminal doesn't support ANSI colors, it will still work but without color coding.

---

## 💡 Tips for Best Experience

### GUI Mode
- Only use if PyQt5 is working properly
- More visually appealing
- Better for presentations
- Smoother animations

### CLI Mode
- Works immediately without issues
- Better for scripting/automation
- More reliable on all systems
- Perfect for remote connections (SSH)

### Recommended
> **For most users:** Use `python cli.py` for a guaranteed working experience!

---

## 🎯 Which Mode Should I Use?

```
Does PyQt5 work? (Try: python -c "from PyQt5 import QtWidgets")
    │
    ├─ YES → Try: python main.py
    │         If it works: Great! Use GUI
    │         If DLL error: Use python cli.py instead
    │
    └─ NO  → Use: python cli.py (Full functionality in terminal)
```

---

## 📝 Using the Application

### General Workflow

1. **Start Application**
   ```bash
   python main.py    # or python cli.py
   ```

2. **View Dashboard** (Option 1)
   - Shows current risk score, threats, system metrics
   - Updated in real-time every 2 seconds

3. **Run Scan** (Option 2)
   - Performs system vulnerability assessment
   - Shows detailed results
   - Takes 3-5 seconds

4. **ML Analysis** (Option 3)
   - View machine learning predictions
   - See model statistics
   - Test threat classification

5. **Review Logs** (Option 4)
   - See all security events
   - Review alerts and actions
   - Complete audit trail

6. **Settings** (Option 5)
   - Check configuration
   - View system information
   - Review threat database

---

## 🔍 Understanding the Metrics

### Risk Score (0-100)
- **0-20**: SAFE (Green) - Normal operation
- **20-40**: LOW (Yellow) - Minor warnings
- **40-60**: MEDIUM (Orange) - Notable activity
- **60-80**: HIGH (Red) - Significant threats
- **80-100**: CRITICAL (Red) - Severe warnings

### Component Breakdown
- **Anomaly Detection** (25%): CPU/Memory/Process anomalies
- **Malware Detection** (30%): Suspicious pattern matching
- **AI Threat** (25%): Behavioral analysis
- **ML Model** (20%): Machine learning prediction

### Threat Levels
- 🟢 SAFE - No threats detected
- 🟡 LOW - Minor issues, monitor
- 🟠 MEDIUM - Notable activity, investigate
- 🔴 HIGH - Significant threat, act
- 🔴 CRITICAL - Severe threat, urgent response

---

## ⌨️ Keyboard Controls (CLI)

| Key | Action |
|-----|--------|
| `0` | Exit application |
| `1` | View dashboard |
| `2` | Run scan |
| `3` | ML analysis |
| `4` | View logs |
| `5` | View settings |
| `Ctrl+C` | Emergency exit |

---

## 🚦 Performance Tips

### For Faster Response
1. Use CLI mode (lighter weight)
2. Close other applications
3. Increase update interval in settings
4. Use Quick Scan instead of Full Scan

### For Slower Systems
1. Definitely use CLI mode
2. Increase refresh interval (from 2s to 5s)
3. Run scans during off-peak hours
4. Monitor system resources separately

---

## 🐛 Debug Mode

To see detailed error messages:

```bash
# GUI Mode with debug output
python main.py --debug

# CLI Mode with debug output
python cli.py --debug

# Test core modules
python test_core.py
```

---

## 📞 Getting Help

### Common Issues

**Issue:** "ModuleNotFoundError"
```bash
Solution: pip install -r requirements.txt
```

**Issue:** "Application hangs"
```bash
Solution: Press Ctrl+C and try again with CLI mode
```

**Issue:** "No color output"
```bash
Solution: Terminal doesn't support colors (still works fine)
```

---

## 🎓 Advanced Usage

### Running Multiple Instances
```bash
# Terminal 1
python cli.py

# Terminal 2 (in different directory)
python cli.py
```

### Scripting with CLI
```python
from cli import EvoShieldCLI
cli = EvoShieldCLI()
cli.run()
```

### Custom Configuration
Edit these files:
- `core/risk_engine.py` - Risk weights
- `core/anomaly_detector.py` - Anomaly threshold
- `ui/styles.qss` - GUI theme colors

---

## ✅ Verification Checklist

Before running, make sure:
- ✅ You're in the correct directory: `c:\Users\chandu\Downloads\evoshield`
- ✅ Python 3.8+ is installed: `python --version`
- ✅ Dependencies installed: `pip install -r requirements.txt`
- ✅ Core modules available: `python -c "from core import *"`

---

## 🎉 You're All Set!

### Suggested First Steps:
1. Run: `python cli.py`
2. Select option 1 to view dashboard
3. Select option 2 to run a scan
4. Select option 5 to see settings
5. Select option 0 to exit

---

## 📚 Documentation

For more information:
- **README.md** - Complete technical guide
- **GETTING_STARTED.md** - Detailed setup tutorial
- **QUICK_REFERENCE.md** - Command reference
- **BUILD_SUMMARY.md** - Project statistics

---

**EvoShield AI v1.0.0** - Ready to Protect 🛡️

**Run Now:** `python cli.py`
