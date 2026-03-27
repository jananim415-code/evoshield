"""
AI Threat Detector Module
Detects repeated automated patterns, behavioral anomalies, and threat chains
"""
import random
import re
from typing import List, Dict, Any, Set
from collections import deque


class AIThreatDetector:
    """Detects threats using pattern recognition, behavior analysis, and threat chains"""
    
    # Common threat chain sequences
    THREAT_CHAINS = {
        "ransomware_chain": {
            "sequence": ["file_enumeration", "file_encryption", "ransom_note_creation", "network_communication"],
            "severity": 0.95,
            "name": "Ransomware Attack"
        },
        "lateral_movement": {
            "sequence": ["reconnaissance", "credential_theft", "lateral_movement", "privilege_escalation"],
            "severity": 0.90,
            "name": "Lateral Movement"
        },
        "data_exfiltration": {
            "sequence": ["data_collection", "compression", "encryption", "command_and_control"],
            "severity": 0.85,
            "name": "Data Exfiltration"
        }
    }
    
    # Behavioral signatures
    BEHAVIORAL_SIGNATURES = {
        "rapid_process_creation": {"pattern": r"process_creation.*process_creation", "severity": 0.7},
        "registry_persistence": {"pattern": r"registry_modification.*startup", "severity": 0.75},
        "memory_injection": {"pattern": r"process_injection.*code_execution", "severity": 0.85},
    }
    
    def __init__(self, pattern_window: int = 10):
        self.pattern_window = pattern_window
        self.behavior_history = deque(maxlen=pattern_window)
        self.pattern_library = {}
        self.threat_indicators = []
        self.threat_chains_detected = []
        
    def detect_repeated_patterns(self, activity: str) -> Dict[str, Any]:
        """Detect if activity repeats in automated patterns"""
        self.behavior_history.append(activity)
        
        # Count occurrences in window
        occurrence_count = sum(1 for a in self.behavior_history if a == activity)
        repetition_ratio = occurrence_count / len(self.behavior_history) if self.behavior_history else 0
        
        # Pattern is suspicious if repeated more than 30% of the time
        is_suspicious = repetition_ratio > 0.3
        
        # Additional check: rapid repetition suggests automation
        rapid_repeat = occurrence_count >= 3  # 3 or more in window of 10
        
        return {
            "activity": activity,
            "repetition_ratio": repetition_ratio,
            "is_suspicious": is_suspicious,
            "rapid_repeat": rapid_repeat,
            "risk_score": min(1.0, repetition_ratio * 1.2 if rapid_repeat else repetition_ratio),
            "occurrence_count": occurrence_count,
            "detection_type": "automated_pattern" if rapid_repeat else "pattern_anomaly"
        }
    
    def detect_behavioral_chain(self, sequence: List[str]) -> Dict[str, Any]:
        """Detect suspicious chains of behaviors"""
        suspicious_sequences = [
            ["network_access", "file_encryption", "data_exfiltration"],
            ["privilege_escalation", "system_access", "persistence"],
            ["reconnaissance", "exploitation", "lateral_movement"],
        ]
        
        sequence_str = " -> ".join(sequence)
        is_suspicious = False
        matched_pattern = None
        threat_chain_match = None
        max_severity = 0.1
        
        # Check against known threat chains
        for chain_key, chain_data in self.THREAT_CHAINS.items():
            chain_sequence = chain_data["sequence"]
            # Check if all behaviors in chain appear in sequence
            if all(behavior in sequence for behavior in chain_sequence):
                is_suspicious = True
                threat_chain_match = {
                    "chain": chain_key,
                    "name": chain_data["name"],
                    "severity": chain_data["severity"]
                }
                max_severity = max(max_severity, chain_data["severity"])
                self.threat_chains_detected.append(threat_chain_match)
                break
        
        # Check against suspicious sequences
        for pattern in suspicious_sequences:
            pattern_str = " -> ".join(pattern)
            if all(behavior in sequence for behavior in pattern):
                is_suspicious = True
                matched_pattern = pattern
                max_severity = max(max_severity, 0.8)
                break
        
        return {
            "sequence": sequence,
            "is_suspicious": is_suspicious,
            "matched_pattern": matched_pattern,
            "threat_chain": threat_chain_match,
            "threat_level": "CRITICAL" if is_suspicious else "LOW",
            "risk_score": max_severity
        }
    
    def analyze_process_correlation(self, process_name: str, activity_type: str) -> Dict[str, Any]:
        """Analyze correlation between processes and activities"""
        # Some processes are normally expected to perform certain activities
        expected_activities = {
            "explorer.exe": ["file_access", "ui_interaction", "memory_access"],
            "svchost.exe": ["network_access", "port_binding", "registry_access"],
            "chrome.exe": ["network_access", "plugin_execution", "cache_write"],
            "cmd.exe": ["file_access", "process_creation", "registry_access"],
        }
        
        # Suspicious activity combinations
        suspicious_combinations = {
            "explorer.exe": ["process_injection", "privilege_escalation", "registry_modification"],
            "svchost.exe": ["file_encryption", "network_data_exfiltration"],
            "cmd.exe": ["system_shutdown", "user_deletion"],
        }
        
        allowed_activities = expected_activities.get(process_name, [])
        suspicious_acts = suspicious_combinations.get(process_name, [])
        
        # Check if activity is allowed
        is_allowed = activity_type in allowed_activities
        is_suspicious_combo = activity_type in suspicious_acts
        is_anomalous = not is_allowed and is_suspicious_combo
        
        # Determine risk
        risk_score = 0.85 if is_suspicious_combo else (0.7 if is_anomalous else 0.1)
        
        return {
            "process": process_name,
            "activity": activity_type,
            "is_allowed": is_allowed,
            "is_suspicious_combo": is_suspicious_combo,
            "is_anomalous": is_anomalous,
            "expected_activities": allowed_activities,
            "risk_score": risk_score,
            "recommendation": "BLOCK" if is_suspicious_combo else ("MONITOR" if is_anomalous else "ALLOW")
        }
    
    def simulate_threat_analysis(self) -> Dict[str, Any]:
        """Generate simulated threat analysis"""
        threat_types = [
            "Suspicious Pattern",
            "Behavioral Anomaly",
            "Process Correlation",
            "Network Anomaly",
            "File System Anomaly"
        ]
        
        confidence = random.gauss(0.5, 0.2)
        confidence = max(0.0, min(1.0, confidence))
        
        return {
            "threat_type": random.choice(threat_types),
            "confidence": confidence,
            "risk_score": confidence,
            "details": f"Pattern detected in activity stream",
            "recommended_action": "MONITOR" if confidence < 0.5 else "ALERT"
        }
    
    def detect_behavioral_signature(self, behavior_sequence: str) -> Dict[str, Any]:
        """Detect behavioral signatures in activity sequences"""
        sequence_lower = behavior_sequence.lower()
        detected_signatures = []
        max_severity = 0.0
        
        for sig_name, sig_data in self.BEHAVIORAL_SIGNATURES.items():
            pattern = sig_data["pattern"]
            if re.search(pattern, sequence_lower):
                detected_signatures.append({
                    "signature": sig_name,
                    "severity": sig_data["severity"]
                })
                max_severity = max(max_severity, sig_data["severity"])
        
        return {
            "behavior_sequence": behavior_sequence,
            "detected_signatures": detected_signatures,
            "is_malicious": len(detected_signatures) > 0,
            "max_severity": max_severity,
            "confidence": min(1.0, len(detected_signatures) * 0.3) if detected_signatures else 0.0
        }
    
    def detect_evasion_techniques(self, process_data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect process evasion techniques"""
        evasion_indicators = []
        
        # Common evasion techniques
        evasion_checks = {
            "process_hollowing": lambda d: d.get("injection_detected", False),
            "dll_side_loading": lambda d: d.get("dll_load_from_unusual_path", False),
            "process_masquerading": lambda d: d.get("suspicious_name_match", False),
            "parent_process_spoofing": lambda d: d.get("parent_mismatch", False),
            "code_caves": lambda d: d.get("code_cave_detected", False),
        }
        
        for technique, check in evasion_checks.items():
            if check(process_data):
                evasion_indicators.append(technique)
        
        return {
            "process": process_data.get("name", "unknown"),
            "evasion_techniques": evasion_indicators,
            "is_evasion_detected": len(evasion_indicators) > 0,
            "risk_score": min(1.0, len(evasion_indicators) * 0.25),
            "indicators_count": len(evasion_indicators)
        }
    
    def add_threat_indicator(self, indicator: str, pattern: List[str], severity: float):
        """Add custom threat indicator"""
        self.threat_indicators.append({
            "indicator": indicator,
            "pattern": pattern,
            "severity": min(1.0, severity)
        })
    
    def get_threat_indicators(self) -> List[Dict[str, Any]]:
        """Get all registered threat indicators including detected threat chains"""
        indicators = self.threat_indicators.copy()
        
        # Include detected threat chains
        if self.threat_chains_detected:
            indicators.extend(self.threat_chains_detected)
        
        return indicators
    
    def evaluate_overall_threat(self) -> float:
        """Evaluate overall threat level (0-1)"""
        threat_scores = []
        
        # Add threat indicator scores
        if self.threat_indicators:
            threat_scores.extend([ind["severity"] for ind in self.threat_indicators])
        
        # Add threat chain scores
        if self.threat_chains_detected:
            threat_scores.extend([chain["severity"] for chain in self.threat_chains_detected])
        
        if not threat_scores:
            return random.uniform(0.0, 0.3)
        
        # Average severity of all indicators and chains
        avg_severity = sum(threat_scores) / len(threat_scores)
        return min(1.0, avg_severity)
