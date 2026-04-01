#!/usr/bin/env python3
"""
Fund NAV Query - Get fund net asset value
"""

import requests
import json
from datetime import datetime

def get_fund_nav(fund_code):
    """
    Query fund NAV from Alipay fund data
    
    Args:
        fund_code: Fund code (e.g., 000001)
    
    Returns:
        dict: Fund NAV information
    """
    url = f"https://fundgz.1234567.com.cn/js/{fund_code}.js"
    
    try:
        response = requests.get(url, timeout=10)
        # Parse JSON from JavaScript response
        data = response.text.replace('jsonpgz(', '').replace(');', '')
        fund_data = json.loads(data)
        
        return {
            "fund_code": fund_code,
            "name": fund_data.get("name", ""),
            "nav": fund_data.get("dwjz", ""),
            "accumulated_nav": fund_data.get("ljjz", ""),
            "date": fund_data.get("jzrq", ""),
            "change": fund_data.get("jzrq", ""),
            "change_percent": fund_data.get("gszzl", "")
        }
    except Exception as e:
        return {"error": str(e), "fund_code": fund_code}

if __name__ == "__main__":
    import sys
    fund_code = sys.argv[1] if len(sys.argv) > 1 else "000001"
    result = get_fund_nav(fund_code)
    print(json.dumps(result, indent=2, ensure_ascii=False))