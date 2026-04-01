#!/usr/bin/env python3
"""
Fund History - Get fund historical NAV data
"""

import requests
import json
from datetime import datetime, timedelta

def get_fund_history(fund_code, days=30):
    """
    Get fund historical NAV data
    
    Args:
        fund_code: Fund code
        days: Number of days of history to retrieve
    
    Returns:
        dict: Historical NAV data
    """
    url = f"https://fundmobapi.eastmoney.com/FundMApi/FundNetDiagram.ashx"
    params = {
        "FCODE": fund_code,
        "deviceid": "",
        "plat": "Iphone",
        "product": "EFund",
        "version": "6.3.0"
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        return {
            "fund_code": fund_code,
            "name": data.get("Expansion", ""),
            "history": data.get("NetDiagramData", [])[-days:]
        }
    except Exception as e:
        return {"error": str(e), "fund_code": fund_code}

if __name__ == "__main__":
    import sys
    fund_code = sys.argv[1] if len(sys.argv) > 1 else "000001"
    days = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    result = get_fund_history(fund_code, days)
    print(json.dumps(result, indent=2, ensure_ascii=False))