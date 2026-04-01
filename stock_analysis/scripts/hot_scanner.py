#!/usr/bin/env python3
"""
Hot Scanner - Viral Trend Detection
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def scan_hot_stocks(min_volume_ratio=2.0, min_price_change=5.0):
    """
    Scan for trending/hot stocks
    
    Args:
        min_volume_ratio: Minimum volume increase ratio
        min_price_change: Minimum price change percentage
    
    Returns:
        list: Hot stocks with metrics
    """
    # Popular tickers to scan
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "NFLX", "AMD", "INTC"]
    
    hot_stocks = []
    
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="5d")
            
            if len(hist) < 2:
                continue
            
            # Calculate metrics
            current_price = hist['Close'][-1]
            prev_price = hist['Close'][-2]
            price_change = ((current_price - prev_price) / prev_price) * 100
            
            avg_volume = hist['Volume'][:-1].mean()
            current_volume = hist['Volume'][-1]
            volume_ratio = current_volume / avg_volume if avg_volume > 0 else 0
            
            if abs(price_change) >= min_price_change or volume_ratio >= min_volume_ratio:
                hot_stocks.append({
                    "ticker": ticker,
                    "price_change_pct": round(price_change, 2),
                    "volume_ratio": round(volume_ratio, 2),
                    "current_price": round(current_price, 2),
                    "company_name": stock.info.get('longName', ticker)
                })
        except Exception:
            continue
    
    # Sort by price change
    hot_stocks.sort(key=lambda x: abs(x['price_change_pct']), reverse=True)
    return hot_stocks[:20]

def get_trending_sectors():
    """Get trending sectors"""
    sector_etfs = {
        "Technology": "XLK",
        "Healthcare": "XLV",
        "Financial": "XLF",
        "Energy": "XLE",
        "Consumer": "XLY"
    }
    
    trends = []
    for sector, etf in sector_etfs.items():
        try:
            data = yf.Ticker(etf).history(period="5d")
            if len(data) >= 2:
                change = ((data['Close'][-1] - data['Close'][-2]) / data['Close'][-2]) * 100
                trends.append({
                    "sector": sector,
                    "change_pct": round(change, 2),
                    "etf": etf
                })
        except Exception:
            continue
    
    trends.sort(key=lambda x: x['change_pct'], reverse=True)
    return trends

if __name__ == "__main__":
    import sys
    print("Scanning for hot stocks...")
    hot = scan_hot_stocks()
    print(json.dumps(hot, indent=2))