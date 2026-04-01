#!/usr/bin/env python3
"""
Stock Analysis - Core Analysis Module
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def analyze_stock(ticker, period="1y"):
    """
    Analyze a stock using Yahoo Finance data
    
    Args:
        ticker: Stock ticker symbol
        period: Analysis period (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
    
    Returns:
        dict: Stock analysis results
    """
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)
        info = stock.info
        
        if hist.empty:
            return {"error": "No data available for ticker"}
        
        # Calculate metrics
        current_price = hist['Close'][-1]
        price_change = hist['Close'][-1] - hist['Close'][0]
        price_change_pct = (price_change / hist['Close'][0]) * 100
        
        # Technical indicators
        sma_20 = hist['Close'].rolling(window=20).mean().iloc[-1]
        sma_50 = hist['Close'].rolling(window=50).mean().iloc[-1]
        
        analysis = {
            "ticker": ticker,
            "current_price": round(current_price, 2),
            "price_change": round(price_change, 2),
            "price_change_pct": round(price_change_pct, 2),
            "sma_20": round(sma_20, 2),
            "sma_50": round(sma_50, 2),
            "volume_avg": int(hist['Volume'].mean()),
            "company_name": info.get('longName', 'N/A'),
            "sector": info.get('sector', 'N/A'),
            "market_cap": info.get('marketCap', 'N/A'),
            "pe_ratio": info.get('trailingPE', 'N/A'),
            "dividend_yield": info.get('dividendYield', 'N/A'),
        }
        
        return analysis
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import sys
    ticker = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
    result = analyze_stock(ticker)
    print(json.dumps(result, indent=2, default=str))