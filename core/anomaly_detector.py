"""
Anomaly Detector Module
Detects unusual patterns using entropy calculation, character analysis, and behavioral anomalies
"""
import math
import random
from typing import Dict, Any, List


class AnomalyDetector:
    """Detects anomalies using entropy, character ratios, and behavioral analysis"""
    
    def __init__(self, threshold: float = 0.6):
        self.threshold = threshold
        self.anomaly_history: List[Dict[str, Any]] = []
    
    @staticmethod
    def calculate_entropy(text: str) -> float:
        """
        Calculate Shannon entropy of text
        High entropy = more randomness/unusual patterns
        Returns: entropy score (0.0-8.0, typically)
        """
        if not text:
            return 0.0
        
        # Calculate frequency of each character
        char_counts = {}
        for char in text:
            char_counts[char] = char_counts.get(char, 0) + 1
        
        # Calculate entropy
        entropy = 0.0
        text_len = len(text)
        
        for count in char_counts.values():
            probability = count / text_len
            if probability > 0:
                entropy -= probability * math.log2(probability)
        
        return entropy
    
    @staticmethod
    def calculate_unusual_character_ratio(text: str) -> float:
        """
        Calculate ratio of unusual characters (special chars, control chars, etc.)
        Returns: ratio (0.0-1.0)
        """
        if not text:
            return 0.0
        
        # Define normal characters
        normal_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ')
        
        unusual_count = sum(1 for char in text if char not in normal_chars)
        return unusual_count / len(text) if text else 0.0
    
    @staticmethod
    def calculate_length_anomaly(text_length: int, baseline: int = 100) -> float:
        """
        Calculate length anomaly score
        Returns: anomaly score (0.0-1.0)
        """
        if text_length == 0:
            return 1.0
        
        # Extreme length counts as anomaly
        if text_length < 10 or text_length > 10000:
            return 0.8
        
        # Calculate deviation from baseline
        deviation = abs(text_length - baseline) / baseline
        return min(1.0, deviation)
    
    def analyze_input(self, text: str) -> Dict[str, Any]:
        """
        Comprehensive anomaly analysis of input text
        Returns: {"score": 0.0-1.0, "reasons": [...], "details": {...}}
        """
        # Calculate individual anomaly metrics
        entropy = self.calculate_entropy(text)
        unusual_char_ratio = self.calculate_unusual_character_ratio(text)
        length_anomaly = self.calculate_length_anomaly(len(text))
        
        # Normalize entropy (8.0 is max, anything >6 is suspicious)
        entropy_score = min(1.0, entropy / 8.0)
        
        # Combine scores (weighted)
        anomaly_score = (
            entropy_score * 0.4 +  # 40% weight
            unusual_char_ratio * 0.35 +  # 35% weight
            length_anomaly * 0.25  # 25% weight
        )
        
        # Identify reasons
        reasons = []
        if entropy > 6.0:
            reasons.append(f"High entropy detected ({entropy:.2f})")
        if unusual_char_ratio > 0.3:
            reasons.append(f"Unusual characters ({unusual_char_ratio*100:.1f}%)")
        if length_anomaly > 0.5:
            reasons.append(f"Abnormal length ({len(text)} chars)")
        
        reason_str = ", ".join(reasons) if reasons else "No anomalies detected"
        result = {
            "score": float(anomaly_score),
            "reason": reason_str,
            "is_anomaly": anomaly_score > self.threshold,
            "details": {
                "entropy": entropy,
                "entropy_score": entropy_score,
                "unusual_char_ratio": unusual_char_ratio,
                "length_anomaly": length_anomaly,
                "text_length": len(text)
            }
        }
        
        # Log if anomaly
        if result["is_anomaly"]:
            self.anomaly_history.append(result)
            if len(self.anomaly_history) > 100:
                self.anomaly_history.pop(0)
        
        return result
    
    def analyze_cpu_spike(self, cpu_percent: float, baseline: float = 20.0) -> Dict[str, Any]:
        """Detect anomalous CPU usage spikes"""
        deviation = abs(cpu_percent - baseline) / baseline if baseline > 0 else 0
        is_anomaly = deviation > self.threshold
        
        return {
            "type": "CPU_SPIKE",
            "is_anomaly": is_anomaly,
            "severity": min(1.0, deviation),
            "cpu_percent": cpu_percent,
            "baseline": baseline,
            "deviation_percent": deviation * 100
        }
    
    def analyze_memory_spike(self, memory_usage: float, baseline: float = 40.0) -> Dict[str, Any]:
        """Detect anomalous memory usage spikes"""
        deviation = abs(memory_usage - baseline) / baseline if baseline > 0 else 0
        is_anomaly = deviation > self.threshold
        
        return {
            "type": "MEMORY_SPIKE",
            "is_anomaly": is_anomaly,
            "severity": min(1.0, deviation),
            "memory_usage": memory_usage,
            "baseline": baseline,
            "deviation_percent": deviation * 100
        }
    
    def analyze_process_behavior(self, process_count: int, baseline: int = 50) -> Dict[str, Any]:
        """Detect unusual process creation patterns"""
        deviation = abs(process_count - baseline) / baseline if baseline > 0 else 0
        is_anomaly = deviation > self.threshold
        
        return {
            "type": "PROCESS_ANOMALY",
            "is_anomaly": is_anomaly,
            "severity": min(1.0, deviation),
            "process_count": process_count,
            "baseline": baseline,
            "deviation_percent": deviation * 100
        }
    
    def simulate_anomaly_score(self) -> float:
        """Generate simulated anomaly score (0-1)"""
        return random.gauss(0.3, 0.25) if random.random() > 0.7 else random.uniform(0.0, 0.4)
    
    def get_anomaly_summary(self) -> Dict[str, int]:
        """Get summary of anomalies detected"""
        return {
            "total_anomalies": len(self.anomaly_history),
            "recent_count": len([a for a in self.anomaly_history[-10:] if a.get("is_anomaly")])
        }
    
    def detect_obfuscation(self, text: str) -> Dict[str, Any]:
        """
        Detect obfuscation patterns (hex-encoded, ROT13, Unicode escapes, etc.)
        Returns: {"detected": bool, "patterns": [...], "confidence": float}
        """
        obfuscation_patterns = []
        
        # Hex encoding detection (\\x followed by hex digits)
        if len([m for m in __import__('re').findall(r'\\x[0-9a-fA-F]{2}', text)]) > 3:
            obfuscation_patterns.append("hex_encoding")
        
        # Unicode escapes detection (\\u followed by 4 hex digits)
        if len([m for m in __import__('re').findall(r'\\u[0-9a-fA-F]{4}', text)]) > 3:
            obfuscation_patterns.append("unicode_escapes")
        
        # Long sequences of numbers (often used in obfuscation)
        if len([m for m in __import__('re').findall(r'\d{8,}', text)]) > 1:
            obfuscation_patterns.append("numeric_sequences")
        
        # Repeated special characters
        if len([m for m in __import__('re').findall(r'[!@#$%^&*]{3,}', text)]) > 0:
            obfuscation_patterns.append("special_char_patterns")
        
        return {
            "detected": len(obfuscation_patterns) > 0,
            "patterns": obfuscation_patterns,
            "pattern_count": len(obfuscation_patterns),
            "confidence": min(1.0, len(obfuscation_patterns) * 0.25)
        }
    
    def detect_behavioral_clustering(self, activities: List[str], cluster_threshold: float = 0.7) -> Dict[str, Any]:
        """
        Detect if activities cluster into suspicious groups
        Returns: {"clusters": [...], "is_suspicious": bool, "confidence": float}
        """
        if not activities:
            return {"clusters": [], "is_suspicious": False, "confidence": 0.0}
        
        # Suspicious activity keywords
        suspicious_keywords = {
            "file_ops": ["encrypt", "compress", "delete", "write", "modify"],
            "network": ["connect", "send", "receive", "transmit", "upload", "download"],
            "system": ["privilege", "admin", "kernel", "system", "registry"],
            "process": ["inject", "spawn", "create", "execute", "hide"],
        }
        
        # Categorize activities
        activity_categories = {}
        for activity in activities:
            activity_lower = activity.lower()
            for category, keywords in suspicious_keywords.items():
                if any(kw in activity_lower for kw in keywords):
                    if category not in activity_categories:
                        activity_categories[category] = []
                    activity_categories[category].append(activity)
                    break
        
        # Check for clustering (multiple categories active)
        suspicious_clusters = [cat for cat, acts in activity_categories.items() if len(acts) >= 2]
        is_suspicious = len(suspicious_clusters) >= 2
        
        return {
            "clusters": activity_categories,
            "suspicious_clusters": suspicious_clusters,
            "is_suspicious": is_suspicious,
            "cluster_count": len(activity_categories),
            "confidence": min(1.0, len(suspicious_clusters) * 0.4) if suspicious_clusters else 0.0
        }
