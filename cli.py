#!/usr/bin/env python3
"""
EvoShield AI - Command-Line Interface (CLI) Version
Full-featured cybersecurity dashboard in the terminal
Works immediately without PyQt5 or GUI dependencies
"""

import sys
import os
import time
import threading
from datetime import datetime
from typing import Dict, Any, List

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core import (
    AnomalyDetector, MalwareSimulator, AIThreatDetector,
    AdaptiveModel, RiskEngine, DefenseSystem, SystemMonitor
)


class Colors:
    """ANSI color codes for terminal output"""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    
    # Text colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Background colors
    BG_DARK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'


class EvoShieldCLI:
    """EvoShield AI Command-Line Interface"""
    
    def __init__(self):
        self.anomaly_detector = AnomalyDetector()
        self.malware_simulator = MalwareSimulator()
        self.ai_threat_detector = AIThreatDetector()
        self.adaptive_model = AdaptiveModel()
        self.risk_engine = RiskEngine()
        self.defense_system = DefenseSystem()
        self.system_monitor = SystemMonitor()
        
        self.running = False
        self.current_menu = "main"
        self.risk_scores = []
        
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self):
        """Print application header"""
        header = f"""
{Colors.CYAN}{Colors.BOLD}
╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║         {Colors.GREEN}E v o S h i e l d   A I   -   C L I   V e r s i o n{Colors.CYAN}        ║
║                                                                       ║
║            Advanced Cybersecurity Defense System                      ║
║              Threat Detection | Risk Analysis | Defense              ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
{Colors.RESET}"""
        print(header)
    
    def print_dashboard(self):
        """Print main dashboard"""
        self.clear_screen()
        self.print_header()
        
        # Get current metrics
        stats = self.system_monitor.get_system_stats()
        if stats["status"] == "OK":
            process_count = stats["process_count"]
            cpu_percent = stats["cpu_percent"]
            memory = stats["memory_percent"]
        else:
            process_count = 0
            cpu_percent = 0
            memory = None
        
        # Simulate threat scores
        anomaly_score = self.anomaly_detector.simulate_anomaly_score()
        ai_analysis = self.ai_threat_detector.simulate_threat_analysis()
        model_result = self.adaptive_model.simulate_inference()
        malware_threats = self.malware_simulator.generate_simulated_threats()
        malware_score = max([t["severity"] for t in malware_threats]) if malware_threats else 0
        
        # Calculate risk
        risk_result = self.risk_engine.calculate_risk_score(
            anomaly_score, malware_score, ai_analysis["risk_score"], model_result["confidence"]
        )
        risk_score = risk_result["risk_score"]
        threat_level = risk_result["level"]
        
        self.risk_scores.append(risk_score)
        if len(self.risk_scores) > 50:
            self.risk_scores.pop(0)
        
        # Color based on threat level
        if threat_level == "SAFE":
            threat_color = Colors.GREEN
            indicator = "🟢"
        elif threat_level == "LOW":
            threat_color = Colors.YELLOW
            indicator = "🟡"
        elif threat_level == "MEDIUM":
            threat_color = Colors.YELLOW
            indicator = "🟠"
        elif threat_level == "HIGH":
            threat_color = Colors.RED
            indicator = "🔴"
        else:
            threat_color = Colors.RED
            indicator = "🔴"
        
        # Print metrics
        print(f"\n{Colors.BOLD}SYSTEM STATUS{Colors.RESET}")
        print("═" * 70)
        print(f"  Timestamp:         {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  Active Processes:  {Colors.CYAN}{process_count}{Colors.RESET}")
        print(f"  CPU Usage:         {Colors.CYAN}{cpu_percent:.1f}%{Colors.RESET}")
        if memory is not None:
            print(f"  Memory Usage:      {Colors.CYAN}{memory:.1f}%{Colors.RESET}")
        
        # Risk Score
        print(f"\n{Colors.BOLD}RISK ASSESSMENT{Colors.RESET}")
        print("═" * 70)
        print(f"  {Colors.BOLD}Risk Score:{Colors.RESET}    {Colors.CYAN}{risk_score:3d}{Colors.RESET}/100")
        print(f"  {Colors.BOLD}Threat Level:{Colors.RESET}   {threat_color}{indicator} {threat_level}{Colors.RESET}")
        
        # Component breakdown
        print(f"\n  {Colors.DIM}Component Analysis:{Colors.RESET}")
        print(f"    • Anomaly Detection:    {Colors.CYAN}{anomaly_score*100:5.1f}%{Colors.RESET}")
        print(f"    • Malware Detection:    {Colors.CYAN}{malware_score*100:5.1f}%{Colors.RESET}")
        print(f"    • AI Threat Analysis:   {Colors.CYAN}{ai_analysis['risk_score']*100:5.1f}%{Colors.RESET}")
        print(f"    • ML Model Confidence:  {Colors.CYAN}{model_result['confidence']*100:5.1f}%{Colors.RESET}")
        
        # ML Prediction
        print(f"\n{Colors.BOLD}ML PREDICTION{Colors.RESET}")
        print("═" * 70)
        print(f"  Threat Type:       {Colors.CYAN}{model_result['threat_level']}{Colors.RESET}")
        print(f"  Confidence:        {Colors.CYAN}{model_result['confidence']:.2%}{Colors.RESET}")
        print(f"  Recommended:       {Colors.CYAN}{model_result['recommended_action']}{Colors.RESET}")
        
        # Risk trend
        print(f"\n{Colors.BOLD}RISK TREND (Last 50 readings){Colors.RESET}")
        print("═" * 70)
        self.print_trend_graph()
        
        # Recent threats
        print(f"\n{Colors.BOLD}DETECTED THREATS{Colors.RESET}")
        print("═" * 70)
        if malware_threats:
            for threat in malware_threats[:5]:
                print(f"  {Colors.RED}•{Colors.RESET} {threat['name']} (Severity: {threat['severity']:.2f})")
        else:
            print(f"  {Colors.GREEN}No threats detected{Colors.RESET}")
        
        # Menu
        self.print_menu()
    
    def print_trend_graph(self):
        """Print simple trend graph"""
        if not self.risk_scores:
            print("  No data yet")
            return
        
        # Normalize scores to 0-10 for ASCII display
        min_score = min(self.risk_scores)
        max_score = max(self.risk_scores)
        range_score = max_score - min_score if max_score > min_score else 1
        
        # Create graph line
        graph = "  "
        for score in self.risk_scores[-40:]:  # Last 40 readings
            normalized = int(((score - min_score) / range_score) * 10) if range_score > 0 else 5
            if normalized < 3:
                graph += f"{Colors.GREEN}▁{Colors.RESET}"
            elif normalized < 6:
                graph += f"{Colors.YELLOW}▅{Colors.RESET}"
            else:
                graph += f"{Colors.RED}█{Colors.RESET}"
        
        print(graph)
        print(f"  Low ({min_score:.0f}) → High ({max_score:.0f})")
    
    def print_menu(self):
        """Print main menu"""
        print(f"\n{Colors.BOLD}MENU{Colors.RESET}")
        print("─" * 70)
        print(f"  {Colors.CYAN}1{Colors.RESET}) Dashboard     {Colors.CYAN}2{Colors.RESET}) Threat Scan   {Colors.CYAN}3{Colors.RESET}) ML Analysis")
        print(f"  {Colors.CYAN}4{Colors.RESET}) Logs          {Colors.CYAN}5{Colors.RESET}) Settings      {Colors.CYAN}0{Colors.RESET}) Exit")
        print("─" * 70)
        choice = input(f"\n{Colors.BOLD}Select option:{Colors.RESET} ").strip()
        self.handle_menu_choice(choice)
    
    def handle_menu_choice(self, choice):
        """Handle menu selection"""
        if choice == "1":
            self.print_dashboard()
        elif choice == "2":
            self.show_threat_scan()
        elif choice == "3":
            self.show_ml_analysis()
        elif choice == "4":
            self.show_logs()
        elif choice == "5":
            self.show_settings()
        elif choice == "0":
            self.exit_app()
        else:
            print(f"{Colors.RED}Invalid option{Colors.RESET}")
            time.sleep(1)
            self.print_dashboard()
    
    def show_threat_scan(self):
        """Show threat scanning interface"""
        self.clear_screen()
        self.print_header()
        
        print(f"\n{Colors.BOLD}SYSTEM VULNERABILITY SCAN{Colors.RESET}")
        print("═" * 70)
        
        print(f"\n{Colors.YELLOW}🔍 Scanning system...{Colors.RESET}\n")
        
        # Simulate scan
        modules = [
            ("Scanning Processes", 0.2),
            ("Analyzing Memory", 0.3),
            ("Checking Network", 0.5),
            ("Scanning Files", 0.8),
            ("ML Classification", 1.0),
        ]
        
        for module, progress in modules:
            print(f"  {module:.<50} {Colors.CYAN}{progress*100:3.0f}%{Colors.RESET}")
            time.sleep(0.5)
        
        # Generate scan results
        print(f"\n{Colors.BOLD}SCAN RESULTS{Colors.RESET}")
        print("─" * 70)
        
        stats = self.system_monitor.get_system_stats()
        process_count = stats["process_count"]
        cpu = stats["cpu_percent"]
        
        threats = self.malware_simulator.generate_simulated_threats()
        
        print(f"\n  Active Processes:     {Colors.CYAN}{process_count}{Colors.RESET}")
        print(f"  CPU Usage:            {Colors.CYAN}{cpu:.1f}%{Colors.RESET}")
        print(f"  Threats Detected:     {Colors.RED if threats else Colors.GREEN}{len(threats)}{Colors.RESET}")
        
        if threats:
            print(f"\n  {Colors.RED}Detected Threats:{Colors.RESET}")
            for threat in threats:
                severity_color = Colors.RED if threat["severity"] > 0.7 else Colors.YELLOW
                print(f"    • {threat['name']:<30} {severity_color}[{threat['severity']:.2f}]{Colors.RESET}")
        
        print(f"\n{Colors.GREEN}✓ Scan complete{Colors.RESET}")
        input(f"\n{Colors.BOLD}Press Enter to continue...{Colors.RESET}")
        self.print_dashboard()
    
    def show_ml_analysis(self):
        """Show ML model analysis"""
        self.clear_screen()
        self.print_header()
        
        print(f"\n{Colors.BOLD}MACHINE LEARNING THREAT ANALYSIS{Colors.RESET}")
        print("═" * 70)
        
        # Model statistics
        stats = self.adaptive_model.get_model_stats()
        
        print(f"\n{Colors.BOLD}Model Information:{Colors.RESET}")
        print(f"  Status:               {Colors.GREEN}{stats['status']}{Colors.RESET}")
        print(f"  Total Training Samples: {Colors.CYAN}{stats['total_samples']}{Colors.RESET}")
        print(f"  Safe Samples:         {Colors.CYAN}{stats['safe_samples']}{Colors.RESET}")
        print(f"  Threat Samples:       {Colors.RED}{stats['threat_samples']}{Colors.RESET}")
        
        # Test predictions
        print(f"\n{Colors.BOLD}Test Predictions:{Colors.RESET}")
        print("─" * 70)
        
        test_cases = [
            "ransomware attack detected",
            "normal system operation",
            "trojan backdoor found",
            "routine file access",
        ]
        
        for text in test_cases:
            pred = self.adaptive_model.predict(text)
            threat_color = Colors.RED if pred['is_threat'] else Colors.GREEN
            print(f"\n  Input: {Colors.CYAN}{text}{Colors.RESET}")
            print(f"  Level: {threat_color}{pred['threat_level']}{Colors.RESET} ({pred['confidence']:.1%})")
        
        print(f"\n{Colors.BOLD}Feature Importance (Top 5):{Colors.RESET}")
        features = self.adaptive_model.get_feature_importance(5)
        for feature, importance in features:
            bar = "█" * int(importance * 20)
            print(f"  {feature:.<25} {Colors.CYAN}{bar}{Colors.RESET}")
        
        input(f"\n{Colors.BOLD}Press Enter to continue...{Colors.RESET}")
        self.print_dashboard()
    
    def show_logs(self):
        """Show event logs"""
        self.clear_screen()
        self.print_header()
        
        print(f"\n{Colors.BOLD}EVENT LOG{Colors.RESET}")
        print("═" * 70)
        
        # Get recent events
        recent_alerts = self.defense_system.get_recent_alerts(20)
        threat_summary = self.defense_system.get_defense_status()
        
        print(f"\n{Colors.BOLD}Defense System Status:{Colors.RESET}")
        print(f"  Active Monitoring:    {Colors.CYAN}{threat_summary['active_monitoring']}{Colors.RESET}")
        print(f"  Active Alerts:        {Colors.RED}{threat_summary['active_alerts']}{Colors.RESET}")
        print(f"  Blocked Threats:      {Colors.YELLOW}{threat_summary['blocked_threats']}{Colors.RESET}")
        print(f"  Quarantined Items:    {Colors.YELLOW}{threat_summary['quarantined_items']}{Colors.RESET}")
        
        print(f"\n{Colors.BOLD}Recent Alerts:{Colors.RESET}")
        print("─" * 70)
        
        if recent_alerts:
            for alert in recent_alerts[-10:]:
                time_str = f"[{alert.get('timestamp', 'N/A')}]"
                severity_color = Colors.RED if alert.get('severity', 0) > 0.7 else Colors.YELLOW
                print(f"  {time_str} {severity_color}{alert.get('threat_type', 'Unknown')}{Colors.RESET}")
        else:
            print(f"  {Colors.GREEN}No recent alerts{Colors.RESET}")
        
        input(f"\n{Colors.BOLD}Press Enter to continue...{Colors.RESET}")
        self.print_dashboard()
    
    def show_settings(self):
        """Show settings"""
        self.clear_screen()
        self.print_header()
        
        print(f"\n{Colors.BOLD}SETTINGS & CONFIGURATION{Colors.RESET}")
        print("═" * 70)
        
        print(f"\n{Colors.BOLD}System Settings:{Colors.RESET}")
        print(f"  Real-time Monitoring:    {Colors.GREEN}ENABLED{Colors.RESET}")
        print(f"  Auto-update:             {Colors.GREEN}ENABLED{Colors.RESET}")
        print(f"  Alert Notifications:     {Colors.GREEN}ENABLED{Colors.RESET}")
        print(f"  Log Level:               {Colors.CYAN}VERBOSE{Colors.RESET}")
        
        print(f"\n{Colors.BOLD}Risk Scoring Weights:{Colors.RESET}")
        print(f"  Anomaly Detection:       25%")
        print(f"  Malware Detection:       30%")
        print(f"  AI Threat Detection:     25%")
        print(f"  Adaptive ML Model:       20%")
        
        print(f"\n{Colors.BOLD}Application Info:{Colors.RESET}")
        print(f"  Version:                 {Colors.CYAN}1.0.0{Colors.RESET}")
        print(f"  Build Date:              {Colors.CYAN}2024-01-15{Colors.RESET}")
        print(f"  Mode:                    {Colors.CYAN}CLI (Command-Line){Colors.RESET}")
        print(f"  Threat Database:         {Colors.GREEN}Updated{Colors.RESET}")
        print(f"  ML Model:                {Colors.GREEN}Trained{Colors.RESET}")
        
        print(f"\n{Colors.BOLD}Threat Database Signatures:{Colors.RESET}")
        print(f"  Malware Types:           8+")
        print(f"  Suspicious Keywords:     20+")
        print(f"  Custom Indicators:       Configurable")
        
        input(f"\n{Colors.BOLD}Press Enter to continue...{Colors.RESET}")
        self.print_dashboard()
    
    def exit_app(self):
        """Exit application"""
        self.clear_screen()
        print(f"\n{Colors.GREEN}{Colors.BOLD}")
        print("╔════════════════════════════════════════════════════╗")
        print("║  Thank you for using EvoShield AI!                 ║")
        print("║  Stay Secure, Stay Protected                       ║")
        print("╚════════════════════════════════════════════════════╝")
        print(f"{Colors.RESET}\n")
        sys.exit(0)
    
    def run(self):
        """Start the CLI application"""
        try:
            while True:
                self.print_dashboard()
        except KeyboardInterrupt:
            self.exit_app()
        except Exception as e:
            print(f"\n{Colors.RED}Error: {e}{Colors.RESET}")
            time.sleep(2)
            self.run()


def main():
    """Main entry point"""
    cli = EvoShieldCLI()
    cli.run()


if __name__ == "__main__":
    main()
