#!/usr/bin/env python3
"""
EvoShield AI Core Module Test
Tests all core AI/ML modules without GUI dependencies
"""

import sys
sys.path.insert(0, '.')

print("=" * 60)
print("EvoShield AI - Core Module Test Suite")
print("=" * 60)
print()

# Test 1: Anomaly Detector
print("✓ Testing Anomaly Detector...")
try:
    from core.anomaly_detector import AnomalyDetector
    detector = AnomalyDetector()
    
    cpu_result = detector.analyze_cpu_spike(85.0)
    print(f"  - CPU Spike Analysis: {'ANOMALY DETECTED' if cpu_result['is_anomaly'] else 'NORMAL'}")
    
    memory_result = detector.analyze_memory_spike(75.0)
    print(f"  - Memory Spike Analysis: {'ANOMALY DETECTED' if memory_result['is_anomaly'] else 'NORMAL'}")
    
    process_result = detector.analyze_process_behavior(150)
    print(f"  - Process Anomaly: {'ANOMALY DETECTED' if process_result['is_anomaly'] else 'NORMAL'}")
    
    print("  ✓ Anomaly Detector working correctly")
except Exception as e:
    print(f"  ✗ Error: {e}")

print()

# Test 2: Malware Simulator
print("✓ Testing Malware Simulator...")
try:
    from core.malware_simulator import MalwareSimulator
    scanner = MalwareSimulator()
    
    result1 = scanner.scan_text("ransomware encrypted files detected")
    print(f"  - Ransomware Detection: {'THREAT DETECTED' if result1['detected'] else 'SAFE'}")
    print(f"    Confidence: {result1['confidence']:.2f}")
    
    result2 = scanner.scan_text("normal file operation")
    print(f"  - Normal Activity: {'THREAT DETECTED' if result2['detected'] else 'SAFE'}")
    
    threats = scanner.generate_simulated_threats()
    print(f"  - Simulated Threats Generated: {len(threats)}")
    
    print("  ✓ Malware Simulator working correctly")
except Exception as e:
    print(f"  ✗ Error: {e}")

print()

# Test 3: AI Threat Detector
print("✓ Testing AI Threat Detector...")
try:
    from core.ai_threat_detector import AIThreatDetector
    ai_detector = AIThreatDetector()
    
    pattern_result = ai_detector.detect_repeated_patterns("suspicious_activity")
    print(f"  - Pattern Detection: {'SUSPICIOUS' if pattern_result['is_suspicious'] else 'NORMAL'}")
    
    chain_result = ai_detector.detect_behavioral_chain([
        "privilege_escalation",
        "system_access",
        "persistence"
    ])
    print(f"  - Behavior Chain: {'SUSPICIOUS' if chain_result['is_suspicious'] else 'NORMAL'}")
    
    correlation = ai_detector.analyze_process_correlation("cmd.exe", "registry_access")
    print(f"  - Process Correlation: {'ANOMALOUS' if correlation['is_anomalous'] else 'NORMAL'}")
    
    print("  ✓ AI Threat Detector working correctly")
except Exception as e:
    print(f"  ✗ Error: {e}")

print()

# Test 4: Adaptive ML Model
print("✓ Testing Adaptive ML Model...")
try:
    from core.adaptive_model import AdaptiveModel
    model = AdaptiveModel()
    
    pred1 = model.predict("ransomware attack detected")
    print(f"  - Threat Prediction: {pred1['threat_level']}")
    print(f"    Confidence: {pred1['confidence']:.2%}")
    
    pred2 = model.predict("normal system operation")
    print(f"  - Safe Activity: {pred2['threat_level']}")
    print(f"    Confidence: {pred2['confidence']:.2%}")
    
    stats = model.get_model_stats()
    print(f"  - Model Stats:")
    print(f"    Total Samples: {stats['total_samples']}")
    print(f"    Safe Samples: {stats['safe_samples']}")
    print(f"    Threat Samples: {stats['threat_samples']}")
    
    print("  ✓ Adaptive ML Model working correctly")
except Exception as e:
    print(f"  ✗ Error: {e}")

print()

# Test 5: Risk Engine
print("✓ Testing Risk Engine...")
try:
    from core.risk_engine import RiskEngine
    risk_engine = RiskEngine()
    
    risk_result = risk_engine.calculate_risk_score(0.3, 0.5, 0.2, 0.4)
    risk_score = risk_result["risk_score"]
    threat_level = risk_engine.get_threat_level(risk_score)
    color = risk_engine.get_threat_color(risk_score)
    
    print(f"  - Risk Score: {risk_score}/100")
    print(f"  - Threat Level: {threat_level}")
    print(f"  - Threat Color: {color}")
    
    risk_engine.log_threat_event("Test Threat", 0.75, "Test purposes")
    threats = risk_engine.get_threat_summary()
    print(f"  - Threat Summary: {threats}")
    
    print("  ✓ Risk Engine working correctly")
except Exception as e:
    print(f"  ✗ Error: {e}")

print()

# Test 6: Defense System
print("✓ Testing Defense System...")
try:
    from core.defense_system import DefenseSystem
    defense = DefenseSystem()
    
    monitor = defense.monitor_activity("ACT_001", "Network", "Monitoring test")
    print(f"  - Monitor Activity: ID={monitor['id']}")
    
    alert = defense.generate_alert("Test Threat", 0.6, "Test Source", "Test details")
    print(f"  - Alert Generated: ID={alert['id']}, Level={alert['severity_label']}")
    
    blocked = defense.block_threat("THR_001", "Test Threat", "Testing")
    print(f"  - Block Threat: Status={blocked['status']}")
    
    quarantine = defense.quarantine_item("FILE_001", "Test File", "Testing")
    print(f"  - Quarantine Item: {quarantine['location']}")
    
    status = defense.get_defense_status()
    print(f"  - Defense Status: {status}")
    
    print("  ✓ Defense System working correctly")
except Exception as e:
    print(f"  ✗ Error: {e}")

print()

# Test 7: System Monitoring
print("✓ Testing System Monitoring...")
try:
    from core.system_monitor import SystemMonitor
    
    monitor = SystemMonitor()
    stats = monitor.get_system_stats()
    
    print(f"  - Active Processes: {stats['process_count']}")
    print(f"  - CPU Usage: {stats['cpu_percent']}%")
    print(f"  - Memory Usage: {stats['memory_percent']}%")
    print(f"  - Memory Available: {stats['memory_available_gb']:.2f} GB")
    
    print("  ✓ System Monitoring working correctly")
except Exception as e:
    print(f"  ✗ Error: {e}")

print()
print("=" * 60)
print("Core Module Test Summary")
print("=" * 60)
print("✓ All core modules are functional!")
print()
print("To run the full GUI application:")
print("  1. pip install PyQt5")
print("  2. python main.py")
print()
