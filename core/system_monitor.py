"""
System Monitor Module
Safe, read-only system monitoring using psutil
"""
import psutil
from typing import Dict, Any

class SystemMonitor:
    """Read-only system monitoring for CPU, Memory, and Processes"""
    
    def __init__(self):
        # Initial call to cpu_percent to baseline
        psutil.cpu_percent(interval=None)
        
    def get_system_stats(self) -> Dict[str, Any]:
        """
        Safely retrieve system statistics
        Returns dictionary with CPU usage, memory usage, and process count
        """
        try:
            # Read-only fetch of process count
            process_count = len(psutil.pids())
            
            # Read-only fetch of CPU usage (non-blocking)
            cpu_usage = psutil.cpu_percent(interval=None)
            
            # Read-only fetch of Memory usage
            memory = psutil.virtual_memory()
            memory_usage = memory.percent
            memory_available_gb = memory.available / (1024**3)
            memory_total_gb = memory.total / (1024**3)
            
            return {
                "process_count": process_count,
                "cpu_percent": cpu_usage,
                "memory_percent": memory_usage,
                "memory_available_gb": memory_available_gb,
                "memory_total_gb": memory_total_gb,
                "status": "OK"
            }
        except Exception as e:
            return {
                "process_count": 0,
                "cpu_percent": 0.0,
                "memory_percent": 0.0,
                "memory_available_gb": 0.0,
                "memory_total_gb": 0.0,
                "status": f"ERROR: {str(e)}"
            }
