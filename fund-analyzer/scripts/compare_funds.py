#!/usr/bin/env python3
"""
Compare Funds - Compare multiple funds
"""

import json
from query_fund_nav import get_fund_nav

def compare_funds(fund_codes):
    """
    Compare multiple funds
    
    Args:
        fund_codes: List of fund codes
    
    Returns:
        dict: Comparison results
    """
    funds = []
    for code in fund_codes:
        fund = get_fund_nav(code)
        if "error" not in fund:
            funds.append(fund)
    
    return {
        "comparison_date": datetime.now().isoformat(),
        "funds": funds,
        "count": len(funds)
    }

if __name__ == "__main__":
    import sys
    from datetime import datetime
    fund_codes = sys.argv[1:] if len(sys.argv) > 1 else ["000001", "000002", "000003"]
    result = compare_funds(fund_codes)
    print(json.dumps(result, indent=2, ensure_ascii=False))