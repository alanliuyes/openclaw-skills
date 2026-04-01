#!/usr/bin/env python3
"""
Seedance Video Generator - Volcano Engine API
"""

import json
import requests
import time

class SeedanceGenerator:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.base_url = "https://ark.cn-beijing.volces.com/api/v3"
    
    def generate_video(self, prompt, image_url=None, **kwargs):
        """
        Generate video from text prompt or image
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "seedance",
            "prompt": prompt,
            "image_url": image_url,
            **kwargs
        }
        
        response = requests.post(
            f"{self.base_url}/videos",
            headers=headers,
            json=data
        )
        
        return response.json()
    
    def get_video_status(self, task_id):
        """
        Get video generation status
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        
        response = requests.get(
            f"{self.base_url}/videos/{task_id}",
            headers=headers
        )
        
        return response.json()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        prompt = sys.argv[1]
        generator = SeedanceGenerator()
        result = generator.generate_video(prompt)
        print(json.dumps(result, indent=2, ensure_ascii=False))