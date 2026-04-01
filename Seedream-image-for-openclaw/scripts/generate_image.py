#!/usr/bin/env python3
"""
Seedream Image Generator - Volcano Engine API
"""

import json
import requests

class SeedreamGenerator:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.base_url = "https://ark.cn-beijing.volces.com/api/v3"
    
    def generate_image(self, prompt, **kwargs):
        """
        Generate image from text prompt
        
        Args:
            prompt: Image description
            **kwargs: Additional parameters (size, style, etc.)
        
        Returns:
            dict: API response with image URL
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "seedream",
            "prompt": prompt,
            **kwargs
        }
        
        response = requests.post(
            f"{self.base_url}/images",
            headers=headers,
            json=data
        )
        
        return response.json()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        prompt = sys.argv[1]
        generator = SeedreamGenerator()
        result = generator.generate_image(prompt)
        print(json.dumps(result, indent=2, ensure_ascii=False))