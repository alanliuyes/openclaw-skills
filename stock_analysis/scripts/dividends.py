#!/usr/bin/env python3
"""
Dividend Analysis
"""

import yfinance as yf
import pandas as pd

def get_dividend_history(ticker):
    """
    Get dividend history for a stock
    
    Args:
        ticker: Stock ticker symbol
    
    Returns:
        dict: Dividend history and analysis
    """
    try:
        stock = yf.Ticker(ticker)
        dividends = stock.dividends
        info = stock.info
        
        if dividends.empty:
            return {
                "ticker": ticker,
                "dividend_yield": info.get('dividendYield', 0) * 100 if info.get('dividendYield') else 0,
                "history": []
            }
        
        # Calculate metrics
        avg_annual_dividend = dividends.resample('Y').sum().mean()
        current_yield = info.get('dividendYield', 0) * 100 if info.get('dividendYield') else 0
        
        return {
            "ticker": ticker,
            "company_name": info.get('longName', 'N/A'),
            "current_yield": round(current_yield, 2),
            "avg_annual_dividend": round(avg_annual_dividend, 2),
            "ex_dividend_date": info.get('exDividendDate', 'N/A'),
            "payout_ratio": info.get('payoutRatio', 'N/A'),
            "recent_dividends": dividends.tail(10).to_dict()
        }
    except Exception as e:
        return {"error": str(e)}

def analyze_dividend_growth(ticker, years=5):
    """Analyze dividend growth over time"""
    try:
        stock = yf.Ticker(ticker)
        dividends = stock.dividends
        
        if dividends.empty:
            return {"error": "No dividend data available"}
        
        annual_dividends = dividends.resample('Y').sum()
        growth_rates = annual_dividends.pct_change().dropna()
        
        return {
            "ticker": ticker,
            "avg_growth_rate": round(growth_rates.mean() * 100, 2),
            "total_years": len(annual_dividends),
            "annual_dividends": annual_dividends.to_dict()
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import sys
    ticker = sys.argv[1] if len(sys.argv) > 1 else "AAPL"
    result = get_dividend_history(ticker)
    print(json.dumps(result, indent=2, default=str))