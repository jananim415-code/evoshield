"""
Defense System Module
Outputs monitoring alerts, and simulated blocking actions
"""
import random
from typing import Dict, Any, List
from enum import Enum
from datetime import datetime


class DefenseAction(Enum):
    """Available defense actions"""
    MONITOR = "MONITOR"
    ALERT = "ALERT"
    ISOLATE = "ISOLATE"
    BLOCK = "BLOCK"
    QUARANTINE = "QUARANTINE"


class DefenseSystem:
    """Advanced defense and response system"""
    
    def __init__(self):
        self.alerts = []
        self.blocked_items = []
        self.quarantine = []
        self.active_monitors = []
        self.defense_log = []
    
    def monitor_activity(self, activity_id: str, activity_type: str, details: str) -> Dict[str, Any]:
        """
        Monitor system activity
        
        Returns:
            Monitoring result with timestamp and details
        """
        monitor_event = {
            "id": activity_id,
            "type": activity_type,
            "details": details,
            "status": "MONITORING",
            "timestamp": len(self.defense_log)
        }
        
        self.active_monitors.append(monitor_event)
        self.defense_log.append(monitor_event)
        
        if len(self.active_monitors) > 100:
            self.active_monitors.pop(0)
        
        return monitor_event
    
    def generate_alert(self, threat_type: str, severity: float, source: str, details: str) -> Dict[str, Any]:
        """
        Generate security alert (simulation only - no real system actions)
        
        Args:
            threat_type: Type of threat detected
            severity: Severity level (0-1)
            source: Source of the threat
            details: Additional details
            
        Returns:
            Alert information
        """
        alert = {
            "id": f"ALERT_{len(self.alerts):04d}",
            "threat_type": threat_type,
            "severity": severity,
            "severity_label": self._severity_to_label(severity),
            "source": source,
            "details": details,
            "timestamp": len(self.defense_log),
            "status": "ACTIVE"
        }
        
        self.alerts.append(alert)
        self.defense_log.append(alert)
        
        if len(self.alerts) > 500:
            self.alerts.pop(0)
        
        return alert
    
    def block_threat(self, threat_id: str, threat_type: str, reason: str) -> Dict[str, Any]:
        """
        Simulate blocking a threat (does NOT actually modify system)
        
        Returns:
            Blocked threat information
        """
        blocked = {
            "id": threat_id,
            "type": threat_type,
            "reason": reason,
            "action": "BLOCKED",
            "timestamp": len(self.defense_log),
            "status": "BLOCKED"
        }
        
        self.blocked_items.append(blocked)
        self.defense_log.append(blocked)
        
        return blocked
    
    def quarantine_item(self, item_id: str, item_type: str, reason: str) -> Dict[str, Any]:
        """
        Quarantine suspicious item (simulation only)
        
        Returns:
            Quarantine information
        """
        quarantine = {
            "id": item_id,
            "type": item_type,
            "reason": reason,
            "status": "QUARANTINED",
            "timestamp": len(self.defense_log),
            "location": f"QUARANTINE/{item_id}"
        }
        
        self.quarantine.append(quarantine)
        self.defense_log.append(quarantine)
        
        if len(self.quarantine) > 200:
            self.quarantine.pop(0)
        
        return quarantine
    
    def isolate_process(self, process_id: str, process_name: str, reason: str) -> Dict[str, Any]:
        """
        Simulate process isolation (no actual termination)
        
        Returns:
            Isolation information
        """
        return self.block_threat(
            threat_id=process_id,
            threat_type=f"PROCESS_{process_name}",
            reason=reason
        )
    
    def get_defense_status(self) -> Dict[str, Any]:
        """Get overall defense system status"""
        return {
            "active_monitoring": len(self.active_monitors),
            "active_alerts": sum(1 for a in self.alerts if a.get("status") == "ACTIVE"),
            "blocked_threats": len(self.blocked_items),
            "quarantined_items": len(self.quarantine),
            "total_defense_actions": len(self.defense_log)
        }
    
    def get_recent_alerts(self, count: int = 10) -> List[Dict[str, Any]]:
        """Get recent alerts"""
        return self.alerts[-count:] if self.alerts else []
    
    def get_blocked_summary(self) -> Dict[str, Any]:
        """Get summary of blocked items"""
        summary = {"total_blocked": len(self.blocked_items)}
        
        # Count by type
        types = {}
        for item in self.blocked_items:
            item_type = item.get("type", "UNKNOWN")
            types[item_type] = types.get(item_type, 0) + 1
        
        summary["by_type"] = types
        return summary
    
    def get_quarantine_items(self) -> List[Dict[str, Any]]:
        """Get quarantined items"""
        return self.quarantine.copy()
    
    def restore_item(self, item_id: str) -> Dict[str, Any]:
        """Simulate restoring a quarantined item (simulation only)"""
        restored_item = None
        for item in self.quarantine:
            if item["id"] == item_id:
                restored_item = item
                self.quarantine.remove(item)
                break
        
        if restored_item:
            restored_item["status"] = "RESTORED"
            self.defense_log.append(restored_item)
        
        return restored_item or {"error": "Item not found"}
    
    def _severity_to_label(self, severity: float) -> str:
        """Convert severity float to label"""
        if severity >= 0.8:
            return "CRITICAL"
        elif severity >= 0.6:
            return "HIGH"
        elif severity >= 0.4:
            return "MEDIUM"
        elif severity >= 0.2:
            return "LOW"
        else:
            return "INFO"
    
    def simulate_defense_action(self) -> Dict[str, Any]:
        """Simulate a defense action"""
        actions = [
            ("Monitor", 0.4),
            ("Alert", 0.3),
            ("Block", 0.2),
            ("Quarantine", 0.1),
        ]
        
        action_choice = random.choices(
            [a[0] for a in actions],
            weights=[a[1] for a in actions],
            k=1
        )[0]
        
        if action_choice == "Monitor":
            return self.monitor_activity(
                f"SIM_{random.randint(1000, 9999)}",
                random.choice(["Network", "Process", "File", "Registry"]),
                f"Simulated {action_choice} activity"
            )
        elif action_choice == "Alert":
            return self.generate_alert(
                random.choice(["Suspicious Process", "Network Anomaly", "File Access"]),
                random.uniform(0.3, 0.9),
                "SIM_SOURCE",
                f"Simulated {action_choice}"
            )
        elif action_choice == "Block":
            return self.block_threat(
                f"THR_{random.randint(1000, 9999)}",
                "Simulated Threat",
                f"Simulated {action_choice} action"
            )
        else:  # Quarantine
            return self.quarantine_item(
                f"QAR_{random.randint(1000, 9999)}",
                "Suspicious File",
                f"Simulated {action_choice} action"
            )
    
    def clear_logs(self):
        """Clear all defense logs (reset system)"""
        self.alerts = []
        self.blocked_items = []
        self.quarantine = []
        self.active_monitors = []
        self.defense_log = []
