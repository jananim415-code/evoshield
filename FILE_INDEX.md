# 📑 EvoShield AI Desktop Application - File Index

## 🎯 START HERE

### First Time? Read This Order:
1. **DESKTOP_APP_README.md** ← Start here! (5 min read)
2. **LAUNCH_READY.md** ← Launch procedures (10 min read)
3. **DESKTOP_APP_GUIDE.md** ← Feature details (15 min read)
4. **SUMMARY.md** ← Technical overview (10 min read)

### Quick Launch:
```bash
python main.py
```

---

## 📁 File Structure Overview

### 🚀 Entry Points (How to Launch)

| File | Purpose | How to Run |
|------|---------|-----------|
| **main.py** | 🌟 **PRIMARY LAUNCHER** | `python main.py` |
| launch_verify.py | Verify setup | `python launch_verify.py` |
| launch.bat | Windows batch launcher | Double-click or `launch.bat` |
| launch.ps1 | PowerShell launcher | `powershell -ExecutionPolicy Bypass -File launch.ps1` |

---

### 🎨 User Interface (Windows & Components)

| File | Purpose | Language |
|------|---------|----------|
| **ui/main_window.py** | 🖥️ Main PyQt5 window + dashboard | Python |
| ui/styles.qss | Dark theme styling | QSS (Qt) |
| ui/__init__.py | Module exports | Python |

**Key Classes in main_window.py:**
- `EvoShieldWindow(QMainWindow)` - Main application window
- `DashboardCard` - Reusable card widget
- `ThreatIndicator` - Threat level display
- `CircularProgressBar` - Risk score indicator

---

### 🧠 Core Threat Detection (Backend)

| File | Purpose | Functionality |
|------|---------|-----------------|
| core/anomaly_detector.py | CPU/memory pattern detection | 25% weight |
| core/malware_simulator.py | Signature-based threats | 30% weight |
| core/ai_threat_detector.py | AI pattern analysis | 25% weight |
| core/adaptive_model.py | ML threat classification | 20% weight |
| core/risk_engine.py | Risk score calculation | Combines all |
| core/defense_system.py | Response simulation | Alerting & logging |
| core/__init__.py | Module exports | Python |

---

### 📚 Documentation (Everything You Need to Know)

#### Getting Started
| File | Topic | Read Time |
|------|-------|-----------|
| **DESKTOP_APP_README.md** | Quick start guide | 5 min |
| **LAUNCH_READY.md** | Detailed launch procedures | 10 min |
| **SUMMARY.md** | Technical overview | 10 min |

#### Feature Guides
| File | Topic | Read Time |
|------|-------|-----------|
| **DESKTOP_APP_GUIDE.md** | Complete features & customization | 15 min |
| README.md | Technical architecture | 20 min |
| GETTING_STARTED.md | Advanced setup | 15 min |
| QUICK_REFERENCE.md | API & command reference | 10 min |
| BUILD_SUMMARY.md | Project statistics | 5 min |

#### Other Documentation
| File | Topic |
|------|-------|
| RUN_GUIDE.md | CLI mode guide |
| ISSUE_RESOLVED.md | Problem resolution doc |
| STATUS.md | Overall status report |
| START.txt | Plain text quick start |

---

### 🧪 Testing & Utilities

| File | Purpose | Run With |
|------|---------|----------|
| test_core.py | Test all core modules | `python test_core.py` |
| demo.py | Feature demonstration | `python demo.py` |
| setup.py | Dependency installer | `python setup.py` |
| cli.py | Terminal UI (fallback) | `python cli.py` |

---

### ⚙️ Configuration Files

| File | Purpose |
|------|---------|
| requirements.txt | Python package dependencies |
| .gitignore | Git ignore rules |

---

## 🎯 What Each Change Does

### main.py (Updated)
**Previous**: Tried GUI first, fell back to CLI
**Now**: Direct desktop application launcher
**Key Features**:
- Proper QApplication initialization
- Clear startup messages
- Comprehensive error handling
- Window creation and display
- Event loop management

### ui/main_window.py (Enhanced)
**Added**:
- Fixed widget layout bugs
- `run_full_scan()` method - Comprehensive scans
- `run_quick_scan()` method - Fast scans
- Better error handling
- Connected backend to UI widgets
- Real-time updates via QTimer

**Fixed**:
- Process card now in correct grid position
- Scan buttons now functional

### requirements.txt (Updated)
**Added**: `PyQtChart==5.15.7` (for graphs)

### New Launcher Scripts
**Created**:
- `launch.bat` - Windows batch launcher
- `launch.ps1` - PowerShell launcher

### New Documentation
**Created**:
- `DESKTOP_APP_README.md` - Quick start
- `LAUNCH_READY.md` - Launch guide
- `DESKTOP_APP_GUIDE.md` - Features guide
- `SUMMARY.md` - Technical summary
- `FILE_INDEX.md` - This file

### New Utilities
**Created**:
- `launch_verify.py` - Pre-launch verification

---

## 🔄 Architecture Overview

```
User starts: python main.py
         ↓
   main.py (Entry Point)
         ↓
   Create QApplication
         ↓
   Show EvoShieldWindow
         ↓
   QTimer starts (2-second updates)
         ↓
   ┌─────────────────────────────┐
   │ Every 2 seconds:            │
   │ 1. Call core modules        │
   │ 2. Calculate risk score     │
   │ 3. Update UI widgets        │
   │ 4. Update graph             │
   │ 5. Log events               │
   └─────────────────────────────┘
```

---

## 📊 Component Relationships

### UI → Core Flow
```
Dashboard (main_window.py)
    ↓
┌─────────────────────────────────────────┐
│ Threat Detection (core/ modules):       │
│  1. AnomalyDetector                     │
│  2. MalwareSimulator                    │
│  3. AIThreatDetector                    │
│  4. AdaptiveModel (ML)                  │
└─────────────────────────────────────────┘
    ↓
RiskEngine (Combines 4 scores)
    ↓
Updates to UI:
  - Risk score display
  - Threat level indicator
  - Event log
  - Graph points
```

---

## 🚀 Launch Sequences

### Method 1: Direct Python
```bash
$ python main.py
→ QApplication initializes
→ Main window created
→ Window shown
→ Event loop starts
→ Dashboard displays
```

### Method 2: Batch Script (Windows)
```bash
$ launch.bat
→ Checks Python installed
→ Checks dependencies
→ Runs launch_verify.py
→ Launches python main.py
```

### Method 3: PowerShell (Windows)
```powershell
$ powershell -ExecutionPolicy Bypass -File launch.ps1
→ Same as batch script
→ With colored output
```

### Method 4: With Verification
```bash
$ python launch_verify.py
→ Checks all dependencies
→ Shows ✅ ALL CHECKS PASSED
$ python main.py
→ Then launches
```

---

## ✨ Key Features Implemented

### ✅ Desktop Window
- Modern PyQt5 application
- Dark theme with cyan accents
- Configurable size
- Professional appearance

### ✅ Real-Time Dashboard
- Risk score display
- Threat level indicator
- Process monitoring
- AI predictions
- Live threat graph

### ✅ Threat Detection
- 6 independent modules
- Weighted scoring (0-100)
- Real-time calculations
- Threat level classification

### ✅ Interactive UI
- Sidebar navigation (5 pages)
- Clickable scan buttons
- Event logging
- Settings panel

### ✅ Automatic Updates
- Every 2 seconds
- No manual refresh
- Smooth animations
- Non-blocking operations

### ✅ Error Handling
- Pre-launch verification
- Clear error messages
- Helpful troubleshooting
- Fallback to CLI if needed

---

## 📋 Verification Checklist

Before launching, confirm:
- ✅ Python 3.8+ installed
- ✅ PyQt5 installed: `pip install PyQt5`
- ✅ PyQtChart installed: `pip install PyQtChart`
- ✅ All core modules present in `core/`
- ✅ UI files present in `ui/`
- ✅ main.py exists in root directory

Quick check:
```bash
python launch_verify.py
# Should show: ✅ ALL CHECKS PASSED
```

---

## 🎬 Expected Behavior

### When Correct:
✅ Terminal shows startup messages
✅ Desktop window opens in 2-3 seconds
✅ Window has dark blue background
✅ Dashboard shows 5 cards with data
✅ Graph displays line chart
✅ Values update every 2 seconds
✅ Buttons are clickable
✅ No errors in terminal

### If Issues:
1. Read error message in terminal
2. Run `python launch_verify.py`
3. Install missing dependencies
4. Try again

---

## 📞 Quick Reference Commands

```bash
# LAUNCH APPLICATION
python main.py
launch.bat                           # Windows
powershell -ExecutionPolicy Bypass -File launch.ps1  # PowerShell

# VERIFY SETUP
python launch_verify.py

# INSTALL DEPENDENCIES
pip install PyQt5 PyQtChart psutil scikit-learn numpy
python setup.py                      # Or use setup script

# FALLBACK OPTIONS
python cli.py                        # Terminal version
python demo.py                       # See demo

# TESTING
python test_core.py                 # Test modules
python -c "from ui.main_window import EvoShieldWindow; print('OK')"
```

---

## 📈 File Statistics

| Category | Count | Type |
|----------|-------|------|
| Core modules | 6 | Python |
| UI modules | 3 | Python + QSS |
| Launchers | 3 | Batch, PowerShell, Python |
| Documentation | 9 | Markdown |
| Utilities | 4 | Python |
| Config | 2 | Text |
| **Total** | **30+** | **Files** |

---

## 🎯 Success Indicators

Your installation is successful when:
1. `python launch_verify.py` shows all ✓
2. `python main.py` opens a desktop window
3. Window displays dashboard with data
4. Values update every 2 seconds
5. Buttons respond to clicks
6. No terminal errors

---

## 🚀 Next Steps

1. **Read**: DESKTOP_APP_README.md (5 min)
2. **Verify**: `python launch_verify.py`
3. **Launch**: `python main.py`
4. **Explore**: Click sidebar buttons
5. **Scan**: Click "Start Full System Scan"
6. **Enjoy**: Watch real-time updates

---

## 🎉 Summary

EvoShield AI is now a **complete desktop application** with:

✅ Modern PyQt5 graphical interface
✅ Real-time threat detection system
✅ Professional dark-themed dashboard
✅ Live performance graphs
✅ Interactive scanning tools
✅ Comprehensive event logging
✅ Multiple launch methods
✅ Complete documentation

**Status**: 🟢 Production Ready
**Type**: Desktop Application (PyQt5)
**Version**: 1.0.0

---

**Ready to launch?** Run: `python main.py` 🚀
