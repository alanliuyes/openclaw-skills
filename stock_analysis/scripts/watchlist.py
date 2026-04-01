#!/usr/bin/env python3
"""
Stock Watchlist Management
"""

import json
import os
from datetime import datetime

WATCHLIST_FILE = "watchlist.json"

def load_watchlist():
    """Load watchlist from file"""
    if os.path.exists(WATCHLIST_FILE):
        with open(WATCHLIST_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_watchlist(watchlist):
    """Save watchlist to file"""
    with open(WATCHLIST_FILE, 'w') as f:
        json.dump(watchlist, f, indent=2)

def add_to_watchlist(ticker, notes=""):
    """Add a stock to watchlist"""
    watchlist = load_watchlist()
    watchlist[ticker] = {
        "added_date": datetime.now().isoformat(),
        "notes": notes
    }
    save_watchlist(watchlist)
    return f"Added {ticker} to watchlist"

def remove_from_watchlist(ticker):
    """Remove a stock from watchlist"""
    watchlist = load_watchlist()
    if ticker in watchlist:
        del watchlist[ticker]
        save_watchlist(watchlist)
        return f"Removed {ticker} from watchlist"
    return f"{ticker} not in watchlist"

def get_watchlist():
    """Get all watchlist items"""
    return load_watchlist()

if __name__ == "__main__":
    import sys
    command = sys.argv[1] if len(sys.argv) > 1 else "list"
    
    if command == "add" and len(sys.argv) > 2:
        ticker = sys.argv[2]
        notes = sys.argv[3] if len(sys.argv) > 3 else ""
        print(add_to_watchlist(ticker, notes))
    elif command == "remove" and len(sys.argv) > 2:
        print(remove_from_watchlist(sys.argv[2]))
    else:
        print(json.dumps(get_watchlist(), indent=2))