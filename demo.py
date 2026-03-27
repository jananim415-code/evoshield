#!/usr/bin/env python3
"""
EvoShield AI - Quick Start Demo
Demonstrates core functionality without GUI
Run this to verify your installation
"""

def demo():
    print("\n" + "="*70)
    print(" EvoShield AI - Quick Start Demo")
    print("="*70 + "\n")
    
    # Demo 1: Malware Detection
    print("1️⃣  MALWARE DETECTION DEMO")
    print("-" * 70)
    try:
        from core.malware_simulator import MalwareSimulator
        scanner = MalwareSimulator()
        
        test_cases = [
            "ransomware attack detected on system",
            "normal file operation executing",
            "trojan backdoor installed",
            "routine system scan completed"
        ]
        
        for text in test_cases:
            result = scanner.scan_text(text)
            status = "🚨 THREAT" if result['detected'] else "✅ SAFE"
            confidence = result['confidence']
            print(f"  Input: '{text}'")
            print(f"  Result: {status} (Confidence: {confidence:.2f})\n")
    except Exception as e:
        print(f"  Error: {e}\n")
    
    # Demo 2: Risk Scoring
    print("\n2️⃣  RISK SCORING DEMO")
    print("-" * 70)
    try:
        from core.risk_engine import RiskEngine
        engine = RiskEngine()
        
        scenarios = [
            ("Low Risk", 0.1, 0.1, 0.1, 0.1),
            ("Medium Risk", 0.3, 0.4, 0.3, 0.4),
            ("High Risk", 0.7, 0.8, 0.6, 0.7),
        ]
        
        for name, anomaly, malware, ai, model in scenarios:
            risk_result = engine.calculate_risk_score(anomaly, malware, ai, model)
            risk_score = risk_result["risk_score"]
            threat_level = risk_result["level"]
            color = engine.get_threat_color(risk_score)
            
            print(f"  Scenario: {name}")
            print(f"  Risk Score: {risk_score}/100")
            print(f"  Threat Level: {threat_level}")
            print(f"  Color: {color}\n")
    except Exception as e:
        print(f"  Error: {e}\n")
    
    # Demo 3: Threat Detection
    print("\n3️⃣  THREAT PATTERN DETECTION DEMO")
    print("-" * 70)
    try:
        from core.ai_threat_detector import AIThreatDetector
        detector = AIThreatDetector()
        
        behavior_chain = [
            "privilege_escalation",
            "system_access",
            "persistence"
        ]
        
        result = detector.detect_behavioral_chain(behavior_chain)
        print(f"  Behavior Chain: {' → '.join(behavior_chain)}")
        print(f"  Threat Status: {'🚨 SUSPICIOUS' if result['is_suspicious'] else '✅ NORMAL'}")
        print(f"  Threat Level: {result['threat_level']}")
        print(f"  Risk Score: {result['risk_score']:.2f}\n")
    except Exception as e:
        print(f"  Error: {e}\n")
    
    # Demo 4: System Monitoring
    print("\n4️⃣  SYSTEM MONITORING DEMO")
    print("-" * 70)
    try:
        from core.system_monitor import SystemMonitor
        
        monitor = SystemMonitor()
        stats = monitor.get_system_stats()
        
        print(f"  Active Processes: {stats['process_count']}")
        print(f"  CPU Usage: {stats['cpu_percent']}%")
        print(f"  Memory Usage: {stats['memory_percent']}%")
        print(f"  Available Memory: {stats['memory_available_gb']:.2f} GB\n")
    except Exception as e:
        print(f"  Error: {e}\n")
    
    # Demo 5: ML Model
    print("\n5️⃣  MACHINE LEARNING MODEL DEMO")
    print("-" * 70)
    try:
        from core.adaptive_model import AdaptiveModel
        model = AdaptiveModel()
        
        predictions = [
            "ransomware encryption attack",
            "normal user activity",
            "unauthorized privilege escalation",
            "system startup complete"
        ]
        
        for text in predictions:
            result = model.predict(text)
            print(f"  Input: '{text}'")
            print(f"  Prediction: {result['threat_level']} ({result['confidence']:.2%})")
            print(f"  Action: {result['recommended_action']}\n")
        
        print(f"  Model Stats:")
        stats = model.get_model_stats()
        print(f"    Status: {stats['status']}")
        print(f"    Total Samples: {stats['total_samples']}")
        print(f"    Safe Samples: {stats['safe_samples']}")
        print(f"    Threat Samples: {stats['threat_samples']}\n")
    except Exception as e:
        print(f"  Error: {e}\n")
    
    # Demo 6: Defense System
    print("\n6️⃣  DEFENSE SYSTEM DEMO")
    print("-" * 70)
    try:
        from core.defense_system import DefenseSystem
        defense = DefenseSystem()
        
        # Generate various defense actions
        monitor = defense.monitor_activity("PROC_1234", "Process", "cmd.exe launched")
        print(f"  Monitor: {monitor['id']} - {monitor['status']}")
        
        alert = defense.generate_alert("Suspicious Process", 0.85, "PID_1234", "cmd.exe with unusual arguments")
        print(f"  Alert: {alert['id']} - Level: {alert['severity_label']}")
        
        block = defense.block_threat("THR_001", "Malicious File", "Detected ransomware pattern")
        print(f"  Block: {block['id']} - Status: {block['status']}")
        
        quarantine = defense.quarantine_item("FILE_001", "Executable", "Trojan trojan.exe")
        print(f"  Quarantine: {quarantine['location']} - Status: {quarantine['status']}\n")
        
        status = defense.get_defense_status()
        print(f"  Defense Status:")
        print(f"    Active Monitoring: {status['active_monitoring']}")
        print(f"    Active Alerts: {status['active_alerts']}")
        print(f"    Blocked Threats: {status['blocked_threats']}")
        print(f"    Quarantined Items: {status['quarantined_items']}\n")
    except Exception as e:
        print(f"  Error: {e}\n")
    
    # Final summary
    print("\n" + "="*70)
    print(" Demo Complete! ✅")
    print("="*70)
    print("\nTo run the full GUI application:")
    print("  1. Install all dependencies: pip install -r requirements.txt")
    print("  2. Run: python main.py")
    print("\nFor more information, see README.md")
    print("="*70 + "\n")


if __name__ == "__main__":
    demo()
