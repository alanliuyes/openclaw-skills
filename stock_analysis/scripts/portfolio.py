#!/usr/bin/env python3
"""
Portfolio Management
"""

import json
import os
from datetime import datetime

PORTFOLIO_FILE = "portfolio.json"

def load_portfolio():
    """Load portfolio from file"""
    if os.path.exists(PORTFOLIO_FILE):
        with open(PORTFOLIO_FILE, 'r') as f:
            return json.load(f)
    return {"holdings": {}, "cash": 0}

def save_portfolio(portfolio):
    """Save portfolio to file"""
    with open(PORTFOLIO_FILE, 'w') as f:
        json.dump(portfolio, f, indent=2)

def add_position(ticker, shares, avg_price):
    """Add a position to portfolio"""
    portfolio = load_portfolio()
    if ticker not in portfolio["holdings"]:
        portfolio["holdings"][ticker] = {"shares": 0, "avg_price": 0}
    
    position = portfolio["holdings"][ticker]
    total_shares = position["shares"] + shares
    total_cost = position["shares"] * position["avg_price"] + shares * avg_price
    position["shares"] = total_shares
    position["avg_price"] = total_cost / total_shares if total_shares > 0 else 0
    position["added_date"] = datetime.now().isoformat()
    
    save_portfolio(portfolio)
    return f"Added {shares} shares of {ticker} at ${avg_price}"

def remove_position(ticker, shares):
    """Remove shares from a position"""
    portfolio = load_portfolio()
    if ticker in portfolio["holdings"]:
        position = portfolio["holdings"][ticker]
        if position["shares"] >= shares:
            position["shares"] -= shares
            if position["shares"] == 0:
                del portfolio["holdings"][ticker]
            save_portfolio(portfolio)
            return f"Removed {shares} shares of {ticker}"
    return f"Position not found or insufficient shares"

def get_portfolio():
    """Get complete portfolio"""
    return load_portfolio()

if __name__ == "__main__":
    import sys
    command = sys.argv[1] if len(sys.argv) > 1 else "show"
    
    if command == "add" and len(sys.argv) > 4:
        print(add_position(sys.argv[2], float(sys.argv[3]), float(sys.argv[4])))
    elif command == "remove" and len(sys.argv) > 3:
        print(remove_position(sys.argv[2], float(sys.argv[3])))
    else:
        print(json.dumps(get_portfolio(), indent=2))