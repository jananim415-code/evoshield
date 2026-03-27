"""
Adaptive Machine Learning Model
Production-grade ML-based threat prediction with model persistence and online learning
"""
import json
import os
import random
from typing import List, Dict, Tuple, Any
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import numpy as np
try:
    import joblib
except ImportError:
    # Fallback for older scikit-learn versions
    from sklearn.externals import joblib


class AdaptiveModel:
    """Advanced ML-based threat detection with model persistence and online learning"""
    
    def __init__(self, model_path: str = "data/model.pkl", history_path: str = "data/history.json"):
        self.model_path = Path(model_path)
        self.history_path = Path(history_path)
        self.input_count = 0
        self.RETRAIN_THRESHOLD = 10  # Retrain after 10 new samples
        self.is_trained = False
        
        # Create data directory
        os.makedirs(self.model_path.parent, exist_ok=True)
        
        # Load or create model
        if self.model_path.exists():
            try:
                self.model = joblib.load(self.model_path)
                self.is_trained = True
                print(f"✓ Loaded persisted ML model from {self.model_path}")
            except Exception as e:
                print(f"⚠ Failed to load model: {e}, creating new")
                self.model = self._create_pipeline()
                self._initialize_with_default_data()
        else:
            self.model = self._create_pipeline()
            self._initialize_with_default_data()
        
        # Load training history
        self.training_history = self._load_history()
    
    def _create_pipeline(self) -> Pipeline:
        """Create ML pipeline with TF-IDF vectorizer and Logistic Regression"""
        return Pipeline([
            ('tfidf', TfidfVectorizer(
                max_features=500,
                lowercase=True,
                stop_words='english',
                ngram_range=(1, 2),
                min_df=1,
                max_df=20
            )),
            ('logistic', LogisticRegression(
                random_state=42,
                max_iter=500,
                class_weight='balanced'
            ))
        ])
    
    def _initialize_with_default_data(self):
        """Initialize model with comprehensive safe and suspicious datasets"""
        
        # Safe activity samples (extensive)
        safe_texts = [
            "user opened file explorer", "system memory usage normal", "network connection to google.com",
            "process started explorer.exe", "disk read operation completed", "printer driver installed",
            "windows update installed successfully", "application launched normally", "file copied to documents",
            "browser opened google.com", "email synced successfully", "calendar updated", "system backup completed",
            "antivirus scan finished clean", "driver update checked", "system clock synchronized",
            "user logged in successfully", "password changed", "two factor authentication enabled",
            "backup restored from cloud", "files synchronized", "system restarted normally",
            "chrome extension installed", "plugin updated", "theme applied", "settings saved",
            "video player opened", "music player running", "photo library loaded", "document edited",
            "spreadsheet updated", "presentation loaded", "database queried", "api call successful",
        ]
        
        # Suspicious/malware samples (extensive)
        suspicious_texts = [
            "cmd.exe launched", "powershell.exe -noprofile -command", "base64 encoded payload",
            "system32 modified", "registry hive loaded", "dll injected into process",
            "privilege escalation detected", "unauthorized access attempt", "ransomware signature matched",
            "trojan dropped executable", "backdoor installed", "rootkit activated", "exploit successfully executed",
            "buffer overflow detected", "heap corruption detected", "stack pivot attempt",
            "process hollowing initiated", "code cave injection", "dll side loading detected",
            "cryptolocker spreading", "wannacry variant", "petya detected", "emotet command received",
            "c2 server communication", "malware traffic pattern", "suspicious dns request",
            "command injection payload", "sql injection attempt", "xss script embedded",
        ]
        
        # Train on safe (label=0) and suspicious (label=1)
        all_texts = safe_texts + suspicious_texts
        labels = [0] * len(safe_texts) + [1] * len(suspicious_texts)
        
        self.model.fit(all_texts, labels)
        self.is_trained = True
        print(f"✓ Initialized ML model with {len(safe_texts)} safe and {len(suspicious_texts)} suspicious samples")
        
        # Save initial model
        self._save_model()
    
    def predict(self, text: str) -> Dict[str, Any]:
        """
        Predict threat level with probability scores
        Returns: {"threat_level": "Critical/High/Medium/Low", "confidence": 0.0-1.0, "risk_score": 0-100}
        """
        if not self.is_trained:
            return {"threat_level": "Unknown", "confidence": 0.5, "risk_score": 50, "is_suspicious": False}
        
        try:
            # Get probability prediction
            proba = self.model.predict_proba([text])[0]
            threat_probability = float(proba[1])  # Probability of being suspicious (class 1)
            
            # Map probability to risk score
            risk_score = int(threat_probability * 100)
            
            # Determine threat level
            if threat_probability >= 0.7:
                threat_level = "Critical"
            elif threat_probability >= 0.5:
                threat_level = "High"
            elif threat_probability >= 0.3:
                threat_level = "Medium"
            else:
                threat_level = "Low"
            
            return {
                "threat_level": threat_level,
                "confidence": threat_probability,
                "risk_score": risk_score,
                "is_suspicious": threat_probability > 0.5
            }
        except Exception as e:
            print(f"⚠ Prediction error: {e}")
            return {"threat_level": "Unknown", "confidence": 0.5, "risk_score": 50, "is_suspicious": False}
    
    def simulate_inference(self) -> Dict[str, Any]:
        """Simulate inference on random input"""
        sample_texts = [
            "system normal operation",
            "network connectivity good",
            "user activity logged",
            "suspicious process detected",
            "malware signature found",
        ]
        text = random.choice(sample_texts)
        result = self.predict(text)
        result['input'] = text
        return result
    
    def add_sample(self, text: str, is_suspicious: bool) -> None:
        """
        Add new sample for online learning
        After RETRAIN_THRESHOLD samples, automatically retrain
        """
        self.input_count += 1
        
        # Store in history
        self.training_history.append({
            "timestamp": str(__import__('datetime').datetime.now()),
            "text": text,
            "is_suspicious": is_suspicious,
            "count": self.input_count
        })
        
        # Save history
        self._save_history()
        
        # Retrain if threshold reached
        if self.input_count % self.RETRAIN_THRESHOLD == 0:
            self._retrain_from_history()
    
    def _retrain_from_history(self) -> None:
        """Retrain model using stored history"""
        if len(self.training_history) < 3:
            return
        
        try:
            texts = [entry["text"] for entry in self.training_history]
            labels = [1 if entry["is_suspicious"] else 0 for entry in self.training_history]
            
            # Retrain model
            self.model.fit(texts, labels)
            self._save_model()
            print(f"✓ Retrained ML model with {len(texts)} samples from history")
        except Exception as e:
            print(f"⚠ Retraining failed: {e}")
    
    def _save_model(self) -> None:
        """Persist model to disk using joblib"""
        try:
            joblib.dump(self.model, str(self.model_path))
        except Exception as e:
            print(f"⚠ Failed to save model: {e}")
    
    def _save_history(self) -> None:
        """Save training history to JSON"""
        try:
            with open(self.history_path, 'w') as f:
                json.dump(self.training_history, f, indent=2)
        except Exception as e:
            print(f"⚠ Failed to save history: {e}")
    
    def _load_history(self) -> List[Dict]:
        """Load training history from JSON"""
        try:
            if self.history_path.exists():
                with open(self.history_path, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"⚠ Failed to load history: {e}")
        return []
    
    def get_model_stats(self) -> Dict[str, Any]:
        """Get model statistics"""
        return {
            "samples_processed": self.input_count,
            "history_size": len(self.training_history),
            "model_path": str(self.model_path),
            "model_exists": self.model_path.exists(),
            "is_trained": self.is_trained,
        }
