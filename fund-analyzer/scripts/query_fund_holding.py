#!/usr/bin/env python3
"""
Fund Holding Query - Get fund portfolio holdings
"""

import requests
import json

def get_fund_holdings(fund_code):
    """
    Get fund portfolio holdings
    
    Args:
        fund_code: Fund code
    
    Returns:
        dict: Fund holdings information
    """
    url = f"https://fundmobapi.eastmoney.com/FundMApi/FundHoldings.ashx"
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
            "holdings": data.get("Holdings", [])
        }
    except Exception as e:
        return {"error": str(e), "fund_code": fund_code}

if __name__ == "__main__":
    import sys
    fund_code = sys.argv[1] if len(sys.argv) > 1 else "000001"
    result = get_fund_holdings(fund_code)
    print(json.dumps(result, indent=2, ensure_ascii=False))