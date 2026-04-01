#!/usr/bin/env python3
"""
Fund Screener - Screen and rank funds
"""

import requests
import json

def screen_funds(category="all", sort_by="return", limit=20):
    """
    Screen funds based on criteria
    
    Args:
        category: Fund category (all, equity, bond, mixed, etc.)
        sort_by: Sort criteria (return, risk, scale)
        limit: Number of results
    
    Returns:
        list: Screened funds
    """
    url = "https://fundapi.eastmoney.com/fundrankranking.html"
    
    try:
        response = requests.get(url, timeout=10)
        # Parse data from response
        data = response.json()
        
        funds = []
        for item in data.get("Data", [])[:limit]:
            funds.append({
                "code": item.get("CODE"),
                "name": item.get("NAME"),
                "category": item.get("FTYPE"),
                "return_1y": item.get("SYL_1N"),
                "return_6m": item.get("SYL_6Y"),
                "return_3m": item.get("SYL_3Y"),
                "risk": item.get("RISKLEVEL")
            })
        
        return funds
    except Exception as e:
        return [{"error": str(e)}]

if __name__ == "__main__":
    import sys
    category = sys.argv[1] if len(sys.argv) > 1 else "all"
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    result = screen_funds(category, limit=limit)
    print(json.dumps(result, indent=2, ensure_ascii=False))