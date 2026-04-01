#!/usr/bin/env python3
"""
PECO Loop - Perpetual Enhancement and Continuous Operation

Core orchestration system for managing PECO workers.
"""

import json
import time
import requests
from datetime import datetime
from typing import Optional, Dict, Any

class PECOWorker:
    def __init__(self, config_path: str = "config.json"):
        self.config = self._load_config(config_path)
        self.running = False
        self.desires = []
    
    def _load_config(self, path: str) -> Dict[str, Any]:
        """Load configuration from file"""
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return self._default_config()
    
    def _default_config(self) -> Dict[str, Any]:
        """Return default configuration"""
        return {
            "check_interval": 60,
            "feishu_webhook": None,
            "enable_hil": True
        }
    
    def inject_desire(self, desire: str) -> bool:
        """Inject a new desire into SOUL.md"""
        try:
            with open("SOUL.md", "a") as f:
                f.write(f"\n## {datetime.now().isoformat()}\n{desire}\n")
            self.desires.append({
                "timestamp": datetime.now().isoformat(),
                "desire": desire
            })
            return True
        except Exception as e:
            print(f"Error injecting desire: {e}")
            return False
    
    def notify_feishu(self, message: str) -> bool:
        """Send notification via Feishu"""
        webhook = self.config.get("feishu_webhook")
        if not webhook:
            return False
        
        try:
            response = requests.post(webhook, json={
                "msg_type": "text",
                "content": {"text": message}
            })
            return response.status_code == 200
        except Exception as e:
            print(f"Error notifying Feishu: {e}")
            return False
    
    def run_cycle(self):
        """Execute one PECO cycle"""
        print(f"[{datetime.now().isoformat()}] Running PECO cycle...")
        
        # Check for pending desires
        for desire in self.desires:
            if not desire.get("completed"):
                self.process_desire(desire)
        
        # Update SOUL.md
        self.update_soul()
    
    def process_desire(self, desire: Dict[str, Any]):
        """Process a single desire"""
        print(f"Processing desire: {desire['desire']}")
        
        # If HIL is enabled, ask for human confirmation
        if self.config.get("enable_hil"):
            self.notify_feishu(f"PECO Worker needs approval for: {desire['desire']}")
        
        desire["completed"] = True
    
    def update_soul(self):
        """Update SOUL.md with current state"""
        # Implementation would update SOUL.md
        pass
    
    def start(self):
        """Start the PECO worker"""
        self.running = True
        print("PECO Worker started")
        
        while self.running:
            self.run_cycle()
            time.sleep(self.config.get("check_interval", 60))
    
    def stop(self):
        """Stop the PECO worker"""
        self.running = False
        print("PECO Worker stopped")

if __name__ == "__main__":
    worker = PECOWorker()
    
    import signal
    signal.signal(signal.SIGINT, lambda s, f: worker.stop())
    
    worker.start()