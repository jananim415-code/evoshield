"""
EvoShield AI Main Window and UI Components
"""
import sys
import random
from datetime import datetime
from typing import Dict, Any

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QFrame, QStackedWidget, QScrollArea, QTextEdit,
    QProgressBar, QGridLayout, QTableWidget, QTableWidgetItem, QHeaderView, QApplication
)
from PyQt5.QtCore import Qt, QTimer, QSize, pyqtProperty, QPropertyAnimation, QEasingCurve, QThread, pyqtSignal, QPointF
from PyQt5.QtGui import QFont, QColor, QIcon, QPixmap, QPainter, QBrush, QPen
from PyQt5.QtWidgets import QGraphicsOpacityEffect, QGraphicsDropShadowEffect

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from core import (
    AnomalyDetector, MalwareSimulator, AIThreatDetector,
    AdaptiveModel, RiskEngine, DefenseSystem, SystemMonitor
)

class UpdateWorker(QThread):
    """Background thread for processing heavy AI/ML and system fetching tasks"""
    # Signal emitted when processing is complete
    update_ready = pyqtSignal(dict)
    
    def __init__(self, main_window):
        super().__init__()
        self.mw = main_window
        
    def run(self):
        try:
            # 1. Fetch system stats
            stats = self.mw.system_monitor.get_system_stats()
            if stats["status"] == "OK":
                process_count = stats["process_count"]
                cpu_percent = stats["cpu_percent"]
                memory_percent = stats["memory_percent"]
            else:
                process_count = 0
                cpu_percent = 0.0
                memory_percent = 0.0
            
            # 2. Heavy ML Tasks
            anomaly_score = self.mw.anomaly_detector.simulate_anomaly_score()
            malware_threats = self.mw.malware_simulator.generate_simulated_threats()
            malware_score = max([t["severity"] for t in malware_threats]) if malware_threats else 0
            
            ai_analysis = self.mw.ai_threat_detector.simulate_threat_analysis()
            ai_threat_score = ai_analysis["risk_score"]
            model_result = self.mw.adaptive_model.simulate_inference()
            model_confidence = model_result["confidence"]
            
            # 3. Calculate final Risk Score
            risk_result = self.mw.risk_engine.calculate_risk_score(
                anomaly_score, malware_score, ai_threat_score, model_confidence
            )
            risk_score = risk_result["risk_score"]
            
            # Pack results into dictionary with breakdown for Bar Chart
            result_data = {
                "process_count": process_count,
                "cpu_percent": cpu_percent,
                "memory_percent": memory_percent,
                "model_result": model_result,
                "risk_score": risk_score,
                "malware_threats": malware_threats,
                "breakdown": {
                    "ML": model_confidence * 100,
                    "Anomaly": anomaly_score,
                    "Malware": malware_score,
                    "Behavior": ai_threat_score
                }
            }
            
            self.update_ready.emit(result_data)
        except Exception as e:
            print(f"UpdateWorker Error: {e}")


class MplCanvas(FigureCanvas):
    """Custom Matplotlib canvas for PyQt5"""
    def __init__(self, parent=None, width=5, height=3, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi, facecolor='#0f0f1e')
        self.axes = self.fig.add_subplot(111)
        self.axes.set_facecolor('#0a0a14')
        for spine in self.axes.spines.values():
            spine.set_edgecolor('#0f3460')
        self.fig.tight_layout()
        super().__init__(self.fig)


class CircularProgressBar(QFrame):
    """Custom circular progress bar widget"""
    
    def __init__(self, parent=None, size=200):
        super().__init__(parent)
        self.size = size
        self.value = 0
        self.max_value = 100
        self.setStyleSheet("""
            CircularProgressBar {
                background: transparent;
                border: none;
            }
        """)
    
    @pyqtProperty(float)
    def progressValue(self):
        return self.value

    @progressValue.setter
    def progressValue(self, val):
        self.value = val
        self.update()
        
    def setValue(self, value):
        """Set progress value with animation"""
        target_val = max(0, min(100, float(value)))
        self.anim = QPropertyAnimation(self, b"progressValue")
        self.anim.setDuration(800)
        self.anim.setStartValue(self.value)
        self.anim.setEndValue(target_val)
        self.anim.setEasingCurve(QEasingCurve.OutCubic)
        self.anim.start()
    
    def paintEvent(self, event):
        """Paint the circular progress bar"""
        from PyQt5.QtGui import QPainter, QBrush, QPen
        from PyQt5.QtCore import Qt
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Calculate dimensions
        margin = 20
        x = margin
        y = margin
        w = self.width() - 2 * margin
        h = self.height() - 2 * margin
        
        # Draw background circle
        painter.setPen(QPen(QColor("#1a1a2e"), 3))
        painter.drawEllipse(x, y, w, h)
        
        # Draw progress arc (pulsing cyan)
        angle = int((self.value / self.max_value) * 360 * 16)
        pen = QPen(QColor("#00ffff"), 8)
        pen.setCapStyle(Qt.RoundCap)
        painter.setPen(pen)
        painter.drawArc(x, y, w, h, 90 * 16, -angle)
        
        # Draw text
        painter.setFont(QFont("Segoe UI", 24, QFont.Bold))
        painter.setPen(QColor("#00ffff"))
        text_rect = self.rect()
        painter.drawText(text_rect, Qt.AlignCenter, f"{int(self.value)}%")


class DashboardCard(QFrame):
    """Reusable dashboard card widget"""
    
    def __init__(self, title: str, parent=None, delay_ms: int = 0):
        super().__init__(parent)
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
        self.setStyleSheet("""
            DashboardCard {
                background-color: rgba(15, 20, 45, 180);
                border: 1px solid rgba(0, 255, 255, 60);
                border-radius: 12px;
                padding: 15px;
            }
            DashboardCard:hover {
                border: 1px solid rgba(0, 255, 255, 150);
                background-color: rgba(20, 30, 60, 200);
            }
        """)
        
        # Fade-in animation setup
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)
        self.opacity_effect.setOpacity(0.0)
        
        self.anim = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.anim.setDuration(800)
        self.anim.setStartValue(0.0)
        self.anim.setEndValue(1.0)
        self.anim.setEasingCurve(QEasingCurve.OutCubic)
        
        if delay_ms > 0:
            QTimer.singleShot(delay_ms, self.anim.start)
        else:
            self.anim.start()
        
        self.layout = QVBoxLayout()
        
        # Title
        title_label = QLabel(title)
        title_label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        title_label.setStyleSheet("color: #00ffff;")
        self.layout.addWidget(title_label)
        
        # Content area
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout()
        self.content_widget.setLayout(self.content_layout)
        self.layout.addWidget(self.content_widget)
        
        self.setLayout(self.layout)
    
    def add_content(self, widget):
        """Add widget to card content"""
        self.content_layout.addWidget(widget)


class ThreatIndicator(QFrame):
    """Threat level indicator widget"""
    
    def __init__(self, threat_level: str = "SAFE", parent=None):
        super().__init__(parent)
        self.threat_level = threat_level
        self.setStyleSheet("""
            ThreatIndicator {
                background-color: transparent;
                border: none;
            }
        """)
        
        layout = QHBoxLayout()
        
        self.indicator = QLabel("●")
        self.indicator.setStyleSheet(f"color: {self._get_threat_color()};")
        self.indicator.setFont(QFont("Arial", 28))
        
        # Level text
        self.label = QLabel(threat_level)
        self.label.setFont(QFont("Segoe UI", 14, QFont.Bold))
        self.label.setStyleSheet("color: #ffffff;")
        
        layout.addWidget(self.indicator)
        layout.addWidget(self.label)
        layout.addStretch()
        
        self.setLayout(layout)
        
        # Pulse animation setup
        self.opacity_effect = QGraphicsOpacityEffect(self.indicator)
        self.indicator.setGraphicsEffect(self.opacity_effect)
        self.anim = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.anim.setDuration(1200)
        self.anim.setLoopCount(-1) # Infinite loop
        self.anim.setStartValue(1.0)
        self.anim.setKeyValueAt(0.5, 0.2)
        self.anim.setEndValue(1.0)
        
        # Default stop
        self.anim.stop()
        self.opacity_effect.setOpacity(1.0)
    
    def set_threat_level(self, level: str):
        """Update threat level and trigger pulse if high"""
        self.threat_level = level
        color = self._get_threat_color()
        
        self.indicator.setStyleSheet(f"color: {color};")
        self.label.setText(level)
        
        # Only pulse if threat is high/critical
        if level in ["HIGH", "CRITICAL", "High Risk", "Alert"]:
            if self.anim.state() != QPropertyAnimation.Running:
                self.anim.setDuration(800 if level in ["CRITICAL", "High Risk"] else 1200)
                self.anim.start()
        else:
            self.anim.stop()
            self.opacity_effect.setOpacity(1.0)
    
    def _get_threat_color(self) -> str:
        """Get color for threat level"""
        colors = {
            "SAFE": "#00ff00",
            "LOW": "#ffff00",
            "MEDIUM": "#ffa500",
            "HIGH": "#ff4500",
            "CRITICAL": "#ff0000"
        }
        return colors.get(self.threat_level, "#00ff00")


class EvoShieldWindow(QMainWindow):
    """Main EvoShield AI Window"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EvoShield AI - Cyber Defense System")
        self.setGeometry(100, 100, 1600, 1000)
        self.setStyleSheet("""
            * { font-family: 'Segoe UI'; }
            QMainWindow { 
                background-color: #060913; 
            }
        """)
        
        # Initialize core systems
        self.anomaly_detector = AnomalyDetector()
        self.malware_simulator = MalwareSimulator()
        self.ai_threat_detector = AIThreatDetector()
        self.adaptive_model = AdaptiveModel()
        self.risk_engine = RiskEngine()
        self.defense_system = DefenseSystem()
        self.system_monitor = SystemMonitor()
        
        # Mandatory Font Fix
        QApplication.setFont(QFont("Segoe UI", 10))

        # History for real-time line graph (Last 20 updates)
        self.risk_history = []
        
        self.engine_active = True
        
        # Create UI
        self.create_ui()
        
        # Setup update timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_system)
        self.timer.start(2000)  # Update every 2 seconds
    
    def create_ui(self):
        """Create main UI layout"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QHBoxLayout()
        
        # Create sidebar
        sidebar = self.create_sidebar()
        main_layout.addWidget(sidebar)
        
        # Create stacked widget for pages
        self.stacked_widget = QStackedWidget()
        
        # Add pages
        self.stacked_widget.addWidget(self.create_dashboard_page())  # Page 0
        self.stacked_widget.addWidget(self.create_scan_page())       # Page 1
        self.stacked_widget.addWidget(self.create_analysis_page())   # Page 2
        self.stacked_widget.addWidget(self.create_logs_page())       # Page 3
        self.stacked_widget.addWidget(self.create_settings_page())   # Page 4
        
        main_layout.addWidget(self.stacked_widget, 1)
        
        central_widget.setLayout(main_layout)
    
    def create_sidebar(self) -> QFrame:
        """Create left sidebar"""
        sidebar = QFrame()
        sidebar.setStyleSheet("""
            QFrame {
                background-color: rgba(5, 5, 20, 220);
                border-right: 1px solid rgba(0, 255, 255, 40);
            }
        """)
        sidebar.setMaximumWidth(250)
        
        layout = QVBoxLayout()
        
        # Logo/Title
        title = QLabel("EvoShield AI")
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        title.setStyleSheet("color: #00ffff; padding: 20px; background-color: #0f3460;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Navigation buttons
        buttons_config = [
            ("Dashboard", 0),
            ("Scan System", 1),
            ("AI Analysis", 2),
            ("Logs", 3),
            ("Settings", 4),
        ]
        
        for button_text, page_index in buttons_config:
            btn = QPushButton(button_text)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #1a1a2e;
                    color: #00ffff;
                    border: 1px solid #0f3460;
                    padding: 12px;
                    border-radius: 6px;
                    font-weight: bold;
                    margin: 5px 15px;
                }
                QPushButton:hover {
                    background-color: #00ffff;
                    color: #0a0a14;
                    border: 1px solid #ffffff;
                }
                QPushButton:pressed {
                    background-color: #00cccc;
                    color: #0a0a14;
                }
            """)
            btn.clicked.connect(lambda checked, idx=page_index: self.stacked_widget.setCurrentIndex(idx))
            layout.addWidget(btn)
        
        layout.addStretch()
        
        # Status indicator / toggle at bottom
        self.toggle_engine_btn = QPushButton("● System Active")
        self.toggle_engine_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #00ff00;
                padding: 10px;
                border: none;
                font-weight: bold;
                text-align: center;
            }
            QPushButton:hover {
                background-color: #1a1a2e;
            }
        """)
        self.toggle_engine_btn.setFont(QFont("Segoe UI", 10))
        self.toggle_engine_btn.clicked.connect(self.toggle_realtime_engine)
        layout.addWidget(self.toggle_engine_btn)
        
        sidebar.setLayout(layout)
        return sidebar
    
    def create_dashboard_page(self) -> QWidget:
        """Create dashboard page"""
        page = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("EvoShield AI Cyber Defense")
        header.setFont(QFont("Segoe UI", 24, QFont.Bold))
        header.setStyleSheet("color: #00ffff; padding: 20px;")
        layout.addWidget(header)
        
        # Dashboard content
        dashboard_layout = QGridLayout()
        
        # Risk Score Card
        risk_card = DashboardCard("Risk Score", delay_ms=100)
        self.risk_progress = CircularProgressBar(size=200)
        self.risk_progress.setMaximumHeight(250)
        risk_card.add_content(self.risk_progress)
        dashboard_layout.addWidget(risk_card, 0, 0)
        
        # Threat Level Card
        threat_card = DashboardCard("Threat Level", delay_ms=250)
        self.threat_indicator = ThreatIndicator("SAFE")
        threat_card.add_content(self.threat_indicator)
        dashboard_layout.addWidget(threat_card, 0, 1)
        
        # System Stats Card (Upgraded from Active Processes Card)
        process_card = DashboardCard("System Status", delay_ms=400)
        process_layout = QVBoxLayout()
        
        # CPU
        self.cpu_label = QLabel("CPU: 0.0%")
        self.cpu_label.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.cpu_label.setStyleSheet("color: #00ff00;")
        process_layout.addWidget(self.cpu_label)
        
        # Memory
        self.mem_label = QLabel("RAM: 0.0%")
        self.mem_label.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.mem_label.setStyleSheet("color: #00ff00;")
        process_layout.addWidget(self.mem_label)
        
        # Procs
        self.process_label = QLabel("Procs: 0")
        self.process_label.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.process_label.setStyleSheet("color: #00ff00;")
        process_layout.addWidget(self.process_label)
        
        process_widget = QWidget()
        process_widget.setLayout(process_layout)
        process_card.add_content(process_widget)
        dashboard_layout.addWidget(process_card, 0, 2)
        
        # AI Prediction Card
        ai_card = DashboardCard("AI Prediction", delay_ms=550)
        self.ai_label = QLabel("Analyzing...")
        self.ai_label.setWordWrap(True)
        self.ai_label.setStyleSheet("color: #aaaaff;")
        ai_card.add_content(self.ai_label)
        dashboard_layout.addWidget(ai_card, 0, 3)
        
        layout.addLayout(dashboard_layout)
        
        # Integrated Chart Section (Matplotlib)
        graph_card = DashboardCard("Threat Intelligence & Contributions", delay_ms=800)
        chart_container = QWidget()
        chart_layout = QHBoxLayout(chart_container)
        chart_layout.setContentsMargins(0, 10, 0, 0)
        
        self.line_canvas = MplCanvas(self, width=5, height=3)
        self.bar_canvas = MplCanvas(self, width=5, height=3)
        
        chart_layout.addWidget(self.line_canvas)
        chart_layout.addWidget(self.bar_canvas)
        graph_card.add_content(chart_container)
        layout.addWidget(graph_card)
        
        # Bottom panel - Logs
        log_card = DashboardCard("Recent Events", delay_ms=1000)
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setMaximumHeight(150)
        self.log_output.setStyleSheet("""
            QTextEdit {
                background-color: #0a0a14;
                color: #00ff00;
                border: 1px solid #0f3460;
                border-radius: 5px;
            }
        """)
        log_card.add_content(self.log_output)
        layout.addWidget(log_card)
        
        page.setLayout(layout)
        return page
    
    def create_scan_page(self) -> QWidget:
        """Create system scan page"""
        page = QWidget()
        layout = QVBoxLayout()
        
        header = QLabel("System Vulnerability Scan")
        header.setFont(QFont("Segoe UI", 20, QFont.Bold))
        header.setStyleSheet("color: #00ffff; padding: 20px;")
        layout.addWidget(header)
        
        # Scan controls
        controls_frame = QFrame()
        controls_frame.setStyleSheet("""
            QFrame {
                background-color: #1a1a2e;
                border: 2px solid #0f3460;
                border-radius: 10px;
                padding: 15px;
            }
        """)
        controls_layout = QHBoxLayout()
        
        scan_btn = QPushButton("Start Full System Scan")
        scan_btn.setStyleSheet("""
            QPushButton {
                background-color: #0f3460;
                color: #00ffff;
                padding: 10px 20px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #00ffff;
                color: #0f3460;
            }
        """)
        scan_btn.clicked.connect(self.run_full_scan)
        controls_layout.addWidget(scan_btn)
        
        quick_scan_btn = QPushButton("Quick Scan")
        quick_scan_btn.setStyleSheet("""
            QPushButton {
                background-color: #1a1a2e;
                color: #00ffff;
                padding: 10px 20px;
                border: 2px solid #0f3460;
                border-radius: 5px;
                font-weight: bold;
            }
        """)
        quick_scan_btn.clicked.connect(self.run_quick_scan)
        controls_layout.addWidget(quick_scan_btn)
        
        self.scan_progress = QProgressBar()
        self.scan_progress.setVisible(False)
        self.scan_progress.setStyleSheet("QProgressBar::chunk { background-color: #00ffff; }")
        controls_layout.addWidget(self.scan_progress)
        controls_layout.addStretch()
        
        controls_frame.setLayout(controls_layout)
        layout.addWidget(controls_frame)
        
        # Scan results
        results_card = DashboardCard("Scan Results")
        self.scan_results = QTextEdit()
        self.scan_results.setReadOnly(True)
        self.scan_results.setStyleSheet("""
            QTextEdit {
                background-color: #0a0a14;
                color: #00ff00;
                border: 1px solid #0f3460;
                border-radius: 5px;
            }
        """)
        results_card.add_content(self.scan_results)
        layout.addWidget(results_card)
        
        layout.addStretch()
        page.setLayout(layout)
        return page
    
    def create_analysis_page(self) -> QWidget:
        """Create AI analysis page"""
        page = QWidget()
        layout = QVBoxLayout()
        
        header = QLabel("Advanced AI Threat Analysis")
        header.setFont(QFont("Segoe UI", 20, QFont.Bold))
        header.setStyleSheet("color: #00ffff; padding: 20px;")
        layout.addWidget(header)
        
        # Analysis results table
        card = DashboardCard("Threat Analysis Results")
        self.analysis_table = QTableWidget()
        self.analysis_table.setColumnCount(5)
        self.analysis_table.setHorizontalHeaderLabels([
            "Threat Type", "Confidence", "Severity", "Status", "Action"
        ])
        self.analysis_table.setStyleSheet("""
            QTableWidget {
                background-color: #0a0a14;
                color: #00ff00;
                gridline-color: #0f3460;
                border: 1px solid #0f3460;
            }
            QHeaderView::section {
                background-color: #1a1a2e;
                color: #00ffff;
                padding: 5px;
                border: 1px solid #0f3460;
            }
        """)
        self.analysis_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        card.add_content(self.analysis_table)
        layout.addWidget(card)
        
        # Model stats
        stats_card = DashboardCard("ML Model Performance")
        self.model_stats = QLabel("Initializing model...")
        self.model_stats.setStyleSheet("color: #aaaaff;")
        stats_card.add_content(self.model_stats)
        layout.addWidget(stats_card)
        
        page.setLayout(layout)
        return page
    
    def create_logs_page(self) -> QWidget:
        """Create logs page"""
        page = QWidget()
        layout = QVBoxLayout()
        
        header = QLabel("System Logs & Events")
        header.setFont(QFont("Segoe UI", 20, QFont.Bold))
        header.setStyleSheet("color: #00ffff; padding: 20px;")
        layout.addWidget(header)
        
        # Clear button
        btn_layout = QHBoxLayout()
        clear_btn = QPushButton("Clear Logs")
        clear_btn.setStyleSheet("""
            QPushButton {
                background-color: #0f3460;
                color: #ff6666;
                padding: 8px 16px;
                border-radius: 5px;
            }
        """)
        clear_btn.clicked.connect(self.clear_logs)
        btn_layout.addStretch()
        btn_layout.addWidget(clear_btn)
        layout.addLayout(btn_layout)
        
        # Logs text
        card = DashboardCard("Event Log")
        self.full_log = QTextEdit()
        self.full_log.setReadOnly(True)
        self.full_log.setStyleSheet("""
            QTextEdit {
                background-color: #0a0a14;
                color: #00ff00;
                border: 1px solid #0f3460;
                border-radius: 5px;
                font-family: Courier;
                font-size: 10px;
            }
        """)
        card.add_content(self.full_log)
        layout.addWidget(card)
        
        page.setLayout(layout)
        return page
    
    def create_settings_page(self) -> QWidget:
        """Create settings page"""
        page = QWidget()
        layout = QVBoxLayout()
        
        header = QLabel("Settings & Configuration")
        header.setFont(QFont("Segoe UI", 20, QFont.Bold))
        header.setStyleSheet("color: #00ffff; padding: 20px;")
        layout.addWidget(header)
        
        # Settings cards
        settings_card = DashboardCard("System Settings")
        settings_text = QLabel("""
        Real-time Monitoring: ENABLED
        Auto-update: ENABLED
        Alert Notifications: ENABLED
        Log Level: VERBOSE
        Threat Database: Updated
        ML Model: Fully Trained
        
        Build Version: 1.0.0
        Last Update: 2024-01-15
        """)
        settings_text.setStyleSheet("color: #aaaaff;")
        settings_card.add_content(settings_text)
        layout.addWidget(settings_card)
        
        layout.addStretch()
        page.setLayout(layout)
        return page
    
    def create_chart(self):
        # Removed in favor of Matplotlib integration
        pass

    def update_system(self):
        """Update system status (called every 2 seconds by QTimer)"""
        # Prevent starting a new thread if the previous is still busy
        if hasattr(self, 'worker') and self.worker.isRunning():
            return
            
        self.worker = UpdateWorker(self)
        self.worker.update_ready.connect(self.process_update_results)
        self.worker.start()
        
    def process_update_results(self, data: dict):
        """Handle results delivered from the background thread safely on UI thread"""
        self.update_dashboard(
            data["risk_score"], 
            data["process_count"], 
            data["cpu_percent"], 
            data["memory_percent"], 
            data["model_result"]
        )
        self.update_charts(data["risk_score"], data["breakdown"])
        self.generate_log_entry(data["risk_score"], data["process_count"], data["malware_threats"])
    
    def update_dashboard(self, risk_score: int, process_count: int, cpu: float, mem: float, model_result: Dict):
        """Update dashboard widgets dynamically"""
        # Circular Risk score animation
        self.risk_progress.setValue(risk_score)
        
        # Threat level & pulse
        threat_level = self.risk_engine.get_threat_level(risk_score)
        self.threat_indicator.set_threat_level(threat_level)
        
        # System status
        self.process_label.setText(f"Procs: {process_count}")
        self.cpu_label.setText(f"CPU: {cpu:.1f}%")
        self.mem_label.setText(f"RAM: {mem:.1f}%")
        
        # AI Prediction
        prediction_text = f"Threat: {model_result['threat_level']}\nConfidence: {model_result['confidence']:.1%}"
        self.ai_label.setText(prediction_text)
    
    def update_charts(self, score: int, breakdown: dict):
        """Update Matplotlib charts smoothly"""
        # Update Line History
        self.risk_history.append(score)
        if len(self.risk_history) > 20:
            self.risk_history.pop(0)
            
        # 1. Redraw Line Graph
        self.line_canvas.axes.clear()
        self.line_canvas.axes.plot(self.risk_history, color='#00ffff', marker='o', linewidth=2, markersize=4)
        self.line_canvas.axes.set_ylim(0, 100)
        self.line_canvas.axes.set_title("Risk History (Last 20)", color='#00ffff', fontsize=10, pad=10)
        self.line_canvas.axes.tick_params(colors='#00ffff', labelsize=8)
        self.line_canvas.axes.grid(True, color='#13244e', linestyle='--', alpha=0.5)
        self.line_canvas.draw()
        
        # 2. Redraw Bar Chart
        self.bar_canvas.axes.clear()
        labels = list(breakdown.keys())
        values = list(breakdown.values())
        self.bar_canvas.axes.bar(labels, values, color=['#00ffff', '#e94560', '#f9ed69', '#00ff00'], alpha=0.8)
        self.bar_canvas.axes.set_ylim(0, 100)
        self.bar_canvas.axes.set_title("Threat Contributions", color='#00ffff', fontsize=10, pad=10)
        self.bar_canvas.axes.tick_params(colors='#00ffff', labelsize=8)
        self.bar_canvas.draw()
    
    def generate_log_entry(self, risk_score: int, process_count: int, threats: list):
        """Generate and display log entry"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Color coded logging logic
        if risk_score > 70:
            color, tag = "#ff4500", "THREAT"
        elif risk_score > 30:
            color, tag = "#ffff00", "WARNING"
        else:
            color, tag = "#ffffff", "INFO"
            
        entry_text = f"[{timestamp}] {tag}: Risk {risk_score} | Procs {process_count}"
        if threats: entry_text += f" | Event: {threats[0]['name']}"
            
        html = f'<div style="color: {color}; font-family: Segoe UI; margin-bottom: 2px;">{entry_text}</div>'
        
        # Add to log output
        self.log_output.append(html)
        self.full_log.append(html)
        
        # Auto-scroll to bottom
        self.log_output.ensureCursorVisible()
        self.full_log.ensureCursorVisible()
    
    def toggle_realtime_engine(self):
        """Toggle the background polling engine"""
        self.engine_active = not self.engine_active
        if self.engine_active:
            self.timer.start(2000)
            self.toggle_engine_btn.setText("● System Active")
            self.toggle_engine_btn.setStyleSheet("""
                QPushButton { background-color: transparent; color: #00ff00; padding: 10px; border: none; font-weight: bold; text-align: center; }
                QPushButton:hover { background-color: #1a1a2e; }
            """)
        else:
            self.timer.stop()
            self.toggle_engine_btn.setText("● System Paused")
            self.toggle_engine_btn.setStyleSheet("""
                QPushButton { background-color: transparent; color: #ff0000; padding: 10px; border: none; font-weight: bold; text-align: center; }
                QPushButton:hover { background-color: #1a1a2e; }
            """)
    
    def clear_logs(self):
        """Clear log displays"""
        self.log_output.clear()
        self.full_log.clear()
        self.defense_system.clear_logs()
    
    def run_full_scan(self):
        """Scan button with animation and delay"""
        self.scan_results.setHtml('<p style="color: #00ffff; font-family: Segoe UI;">🚀 Initializing Deep Analysis Engine...</p>')
        self.scan_progress.setVisible(True)
        self.scan_progress.setRange(0, 0) # Pulsing animation
        
        sender = self.sender()
        if sender: sender.setEnabled(False)
        
        # Delay 1.5 seconds then execute
        QTimer.singleShot(1500, lambda: self.execute_full_scan(sender))

    def execute_full_scan(self, original_btn):
        if original_btn: original_btn.setEnabled(True)
        self.scan_progress.setVisible(False)
        
        try:
            # Run all detection modules
            anomaly_score = self.anomaly_detector.simulate_anomaly_score()
            malware_threats = self.malware_simulator.generate_simulated_threats()
            ai_analysis = self.ai_threat_detector.simulate_threat_analysis()
            model_result = self.adaptive_model.simulate_inference()
            
            # Calculate overall risk
            malware_score = max([t["severity"] for t in malware_threats]) if malware_threats else 0
            risk_result = self.risk_engine.calculate_risk_score(
                anomaly_score, malware_score, ai_analysis["risk_score"], model_result["confidence"]
            )
            risk_score = risk_result["risk_score"]
            threat_level = risk_result["level"]
            
            # Generate report
            report = f"""
╔════════════════════════════════════════════════════════════════╗
║                    FULL SYSTEM SCAN REPORT                    ║
╚════════════════════════════════════════════════════════════════╝

SCAN TIMESTAMP: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

├─ ANOMALY DETECTION
│  └─ Anomaly Score: {anomaly_score:.1f}/100
│     Status: {"⚠️ DETECTED" if anomaly_score > 30 else "✓ OK"}

├─ MALWARE ANALYSIS
│  └─ Threats Detected: {len(malware_threats)}
│  └─ Severity Score: {malware_score:.1f}/100
"""
            if malware_threats:
                report += "│  Threats Found:\n"
                for threat in malware_threats[:5]:
                    report += f"│     • {threat['name']} (Severity: {threat['severity']:.1f})\n"
            
            report += f"""
├─ AI THREAT ANALYSIS
│  └─ AI Risk Score: {ai_analysis['risk_score']:.1f}/100
│  └─ Pattern Detection: {ai_analysis['pattern_detected']}
│  └─ Confidence: {ai_analysis['threat_confidence']:.1%}

├─ ML MODEL ANALYSIS
│  └─ Threat Level: {model_result['threat_level']}
│  └─ Confidence: {model_result['confidence']:.1%}
│  └─ Suggested Action: {model_result['suggested_action']}

├─ OVERALL ASSESSMENT
│  └─ Risk Score: {risk_score}/100
│  └─ Threat Level: {threat_level}
│  └─ System Status: {"🔴 CRITICAL" if threat_level == "CRITICAL" else "🟠 HIGH RISK" if threat_level == "HIGH" else "🟡 MEDIUM RISK" if threat_level == "MEDIUM" else "🟢 SAFE"}

╠════════════════════════════════════════════════════════════════╣
║ SCAN COMPLETED                                                 ║
╚════════════════════════════════════════════════════════════════╝
"""
            self.scan_results.setText(report)
            
            # Log the scan
            timestamp = datetime.now().strftime("%H:%M:%S")
            log_entry = f"[{timestamp}] Full scan completed: Risk={risk_score}, Level={threat_level}"
            current_log = self.full_log.toPlainText()
            self.full_log.setText(log_entry + "\n" + current_log[:1000])
            
        except Exception as e:
            error_msg = f"❌ Scan Error: {str(e)}\n\nPlease check that all core modules are properly installed."
            self.scan_results.setText(error_msg)
    
    def run_quick_scan(self):
        """Run a quick system scan"""
        self.scan_results.setText("⚡ Running quick scan...\n")
        
        try:
            # Quick check - just malware simulation
            malware_threats = self.malware_simulator.generate_simulated_threats()
            anomaly_score = self.anomaly_detector.simulate_anomaly_score()
            
            report = f"""
╔════════════════════════════════════════════════════════════════╗
║                    QUICK SCAN REPORT                          ║
╚════════════════════════════════════════════════════════════════╝

SCAN TIMESTAMP: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

RESULTS:
─────────────────────────────────────────────────────────────────
  Malware Threats: {len(malware_threats)}
  Anomaly Level: {anomaly_score:.1f}/100
  Quick Status: {"⚠️  THREATS DETECTED" if len(malware_threats) > 0 or anomaly_score > 50 else "✓ SYSTEM OK"}

"""
            if malware_threats:
                report += "DETECTED THREATS:\n"
                for threat in malware_threats[:10]:
                    report += f"  • {threat['name']}\n"
            
            report += f"""
SCAN TIME: ~2 seconds
STATUS: ✓ Complete

Recommendation: Run full system scan for detailed analysis
"""
            self.scan_results.setText(report)
            
            # Log the quick scan
            timestamp = datetime.now().strftime("%H:%M:%S")
            threats = len(malware_threats)
            log_entry = f"[{timestamp}] Quick scan: {threats} threats, Anomaly={anomaly_score:.0f}"
            current_log = self.full_log.toPlainText()
            self.full_log.setText(log_entry + "\n" + current_log[:1000])
            
        except Exception as e:
            error_msg = f"❌ Quick Scan Error: {str(e)}"
            self.scan_results.setText(error_msg)

    def closeEvent(self, event):
        """Handle application exit gracefully and ensure stability"""
        try:
            if hasattr(self, 'timer'):
                self.timer.stop()
            
            # Stop the worker thread safely without crashing
            if hasattr(self, 'worker') and self.worker.isRunning():
                self.worker.quit()
                self.worker.wait(1000) # Wait up to 1000ms for thread to finish neatly
        except Exception as e:
            print(f"Cleanup error during shutdown: {e}")
            
        event.accept()


def main():
    """Main entry point"""
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    window = EvoShieldWindow()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    main()
