#!/usr/bin/env python3
"""
Rumor Scanner - Early Signal Detection
"""

import yfinance as yf
from datetime import datetime, timedelta

def scan_unusual_activity(tickers=None):
    """
    Scan for unusual trading activity that might indicate rumors or early signals
    
    Args:
        tickers: List of tickers to scan (default: popular stocks)
    
    Returns:
        list: Stocks with unusual activity
    """
    if tickers is None:
        tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "AMD"]
    
    signals = []
    
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="10d")
            info = stock.info
            
            if len(hist) < 5:
                continue
            
            # Calculate unusual metrics
            avg_volume = hist['Volume'][:-1].mean()
            current_volume = hist['Volume'][-1]
            volume_spike = current_volume / avg_volume if avg_volume > 0 else 0
            
            price_volatility = hist['Close'].pct_change().std() * 100
            
            # Detect unusual patterns
            if volume_spike > 3.0 or price_volatility > 5.0:
                signals.append({
                    "ticker": ticker,
                    "signal_type": "volume_spike" if volume_spike > 3.0 else "high_volatility",
                    "volume_spike": round(volume_spike, 2),
                    "volatility": round(price_volatility, 2),
                    "company": info.get('longName', ticker),
                    "sector": info.get('sector', 'Unknown')
                })
        except Exception:
            continue
    
    return signals

def get_news_sentiment(ticker):
    """Get news sentiment for a ticker"""
    try:
        stock = yf.Ticker(ticker)
        news = stock.news
        
        return {
            "ticker": ticker,
            "news_count": len(news),
            "recent_headlines": [item.get('title', '') for item in news[:5]]
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import sys
    ticker = sys.argv[1] if len(sys.argv) > 1 else None
    
    if ticker:
        print(json.dumps(get_news_sentiment(ticker), indent=2))
    else:
        print("Scanning for unusual activity...")
        signals = scan_unusual_activity()
        print(json.dumps(signals, indent=2))