"""
Risk Engine Module
Combines all threat detection outputs into a single risk score (0-100)
"""
import random
from typing import Dict, Any, List


class RiskEngine:
    """Combines multiple threat signals into unified risk score"""
    
    def __init__(self):
        self.component_weights = {
            "anomaly_detection": 0.25,
            "malware_detection": 0.30,
            "ai_threat_detection": 0.25,
            "adaptive_model": 0.20
        }
        
        self.risk_history = []
        self.threat_events = []
    
    def calculate_risk_score(
        self, 
        anomaly_score: float,
        malware_score: float,
        ai_threat_score: float,
        model_confidence: float
    ) -> Dict[str, Any]:
        """
        Calculate unified risk score (0-100)
        
        Args:
            anomaly_score: Score from anomaly detector (0-1)
            malware_score: Score from malware simulator (0-1)
            ai_threat_score: Score from AI threat detector (0-1)
            model_confidence: Confidence from adaptive model (0-1)
            
        Returns:
            Dict containing risk_score and level
        """
        # Apply requested weights
        weights = {
            "anomaly_detection": 0.20,
            "malware_detection": 0.25,
            "ai_threat_detection": 0.15,
            "adaptive_model": 0.40
        }
        
        # Weighted combination
        weighted_score = (
            anomaly_score * weights["anomaly_detection"] +
            malware_score * weights["malware_detection"] +
            ai_threat_score * weights["ai_threat_detection"] +
            model_confidence * weights["adaptive_model"]
        )
        
        # Convert to 0-100 scale
        risk_score = int(weighted_score * 100)
        
        # Determine level for return shape
        if risk_score <= 30:
            level = "Low"     # Note: mapped closely to defense_system's "Safe" / "Low Risk" concept, but user wanted "Low/Medium/High" here
        elif risk_score <= 70:
            level = "Medium"
        else:
            level = "High"
        
        # Store in history
        self.risk_history.append(risk_score)
        if len(self.risk_history) > 1000:
            self.risk_history.pop(0)
        
        return {
            "risk_score": risk_score,
            "level": level
        }
    
    def get_threat_level(self, risk_score: int) -> str:
        """Convert risk score to threat level matching defense system"""
        if risk_score <= 30:
            return "Safe"
        elif risk_score <= 70:
            return "Alert"
        else:
            return "High Risk"
    
    def get_threat_color(self, risk_score: int) -> str:
        """Get color code for threat level"""
        if risk_score <= 30:
            return "#00FF00"  # Green
        elif risk_score <= 70:
            return "#FFA500"  # Orange
        else:
            return "#FF0000"  # Red
    
    def log_threat_event(self, threat_type: str, severity: float, details: str):
        """Log a threat event"""
        self.threat_events.append({
            "type": threat_type,
            "severity": severity,
            "details": details,
            "timestamp": len(self.threat_events)  # Simplified timestamp
        })
        
        if len(self.threat_events) > 500:
            self.threat_events.pop(0)
    
    def get_active_threats(self) -> List[Dict[str, Any]]:
        """Get currently active threats (recent events)"""
        # Return last 20 events
        return self.threat_events[-20:] if self.threat_events else []
    
    def get_threat_summary(self) -> Dict[str, Any]:
        """Get summary of threats"""
        if not self.threat_events:
            return {
                "total_events": 0,
                "critical_events": 0,
                "high_events": 0,
                "medium_events": 0,
                "low_events": 0
            }
        
        summary = {
            "total_events": len(self.threat_events),
            "critical_events": 0,
            "high_events": 0,
            "medium_events": 0,
            "low_events": 0
        }
        
        for event in self.threat_events:
            severity = event["severity"]
            if severity >= 0.8:
                summary["critical_events"] += 1
            elif severity >= 0.6:
                summary["high_events"] += 1
            elif severity >= 0.4:
                summary["medium_events"] += 1
            else:
                summary["low_events"] += 1
        
        return summary
    
    def simulate_risk_change(self) -> int:
        """Generate simulated risk score change"""
        base_score = 25
        trend = random.choice([-1, 0, 1])
        variation = random.randint(-15, 15)
        
        risk_score = max(0, min(100, base_score + (trend * 5) + variation))
        return risk_score
    
    def reset_risk_history(self):
        """Reset risk history"""
        self.risk_history = []
        self.threat_events = []
    
    def get_risk_trend(self, window_size: int = 50) -> List[int]:
        """Get risk trend over time"""
        if not self.risk_history:
            return []
        
        # Return last N values
        return self.risk_history[-window_size:]
    
    def analyze_risk_pattern(self) -> Dict[str, Any]:
        """Analyze patterns in risk scores"""
        if not self.risk_history:
            return {"trend": "stable", "average": 0}
        
        recent = self.risk_history[-10:] if len(self.risk_history) >= 10 else self.risk_history
        avg = sum(recent) / len(recent)
        
        # Determine trend
        if len(recent) > 1:
            trend_direction = recent[-1] - recent[0]
            if trend_direction > 10:
                trend = "increasing"
            elif trend_direction < -10:
                trend = "decreasing"
            else:
                trend = "stable"
        else:
            trend = "stable"
        
        return {
            "trend": trend,
            "average_recent": int(avg),
            "max_recent": max(recent),
            "min_recent": min(recent),
            "volatility": max(recent) - min(recent)
        }
    
    def generate_threat_report(self, risk_score: int, threat_details: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Generate comprehensive threat report
        
        Args:
            risk_score: Current risk score (0-100)
            threat_details: Additional threat information
            
        Returns:
            Detailed threat report with recommendations
        """
        threat_level = self.get_threat_level(risk_score)
        threat_color = self.get_threat_color(risk_score)
        
        # Generate recommendations based on threat level
        recommendations = {
            "SAFE": ["Continue monitoring", "No immediate action needed"],
            "LOW": ["Monitor system closely", "Review logs periodically"],
            "MEDIUM": ["Update security signatures", "Monitor for escalation", "Review suspicious activities"],
            "HIGH": ["Activate enhanced monitoring", "Review network traffic", "Check for compromises", "Prepare response plan"],
            "CRITICAL": ["Isolate system if possible", "Engage security team", "Preserve evidence", "Notify administrators", "Begin incident response"]
        }
        
        report = {
            "timestamp": len(self.threat_events),
            "risk_score": risk_score,
            "threat_level": threat_level,
            "threat_color": threat_color,
            "recommendations": recommendations.get(threat_level, []),
            "active_threats": len(self.threat_events),
            "trend_analysis": self.analyze_risk_pattern(),
        }
        
        if threat_details:
            report["threat_details"] = threat_details
        
        return report
