# -*- coding: utf-8 -*-
"""
宏观事件搜索脚本 - Market Predictor V2
用于搜索地缘政治、央行政策、重大事件等宏观信息
"""

import urllib.request
import urllib.parse
import json
import time
import sys
import os
import argparse

# UTF-8 output fix for Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

PORT = os.environ.get('AUTH_GATEWAY_PORT', '19000')
API_URL = f'http://localhost:{PORT}/proxy/prosearch/search'

# 宏观主题关键词
MACRO_THEMES = {
    '地缘政治-中东': '中东冲突 霍尔木兹海峡 伊朗',
    '地缘政治-俄乌': '俄乌冲突最新',
    '地缘政治-黄金': '黄金价格 {date}',
    '地缘政治-原油': '原油价格 WTI布伦特 {date}',
    '央行政策-美联储': '美联储利率 降息预期 {date}',
    '央行政策-中国': '央行政策 LPR 降准 {date}',
    '中美关系': '中美关系 经贸 {date}',
    '国内政策': '两会政策 产业支持 {date}',
}


def search(keyword: str, from_time: int = None, mode: int = 2) -> dict:
    """执行单次搜索"""
    body = {
        'keyword': keyword,
        'mode': mode,
    }
    if from_time:
        body['from_time'] = from_time
    
    try:
        req = urllib.request.Request(
            API_URL,
            data=json.dumps(body, ensure_ascii=False).encode('utf-8'),
            headers={'Content-Type': 'application/json'},
            method='POST'
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        return {'success': False, 'error': str(e)}


def search_macro(date_str: str, from_time: int = None, themes: list = None) -> dict:
    """搜索宏观事件"""
    results = {}
    
    search_themes = themes if themes else list(MACRO_THEMES.keys())
    
    for theme in search_themes:
        if theme not in MACRO_THEMES:
            print(f"Warning: Unknown theme '{theme}', skipping...")
            continue
            
        keyword_template = MACRO_THEMES[theme]
        keyword = keyword_template.format(date=date_str)
        
        print(f"\n{'='*60}")
        print(f'Searching: {theme}')
        print(f'Keyword: {keyword}')
        print(f'{"="*60}')
        
        result = search(keyword, from_time)
        
        if result.get('success'):
            results[theme] = result
            print(result.get('message', '(无消息)'))
        else:
            results[theme] = {'error': result.get('error', result.get('message', 'Unknown error'))}
            print(f"ERROR: {results[theme]['error']}")
    
    return results


def main():
    parser = argparse.ArgumentParser(description='搜索宏观事件')
    parser.add_argument('--date', type=str, required=True, help='搜索日期')
    parser.add_argument('--from-time', type=int, help='起始时间戳（秒）')
    parser.add_argument('--themes', type=str, nargs='*', help='要搜索的主题')
    parser.add_argument('--output', type=str, help='输出文件路径（JSON）')
    
    args = parser.parse_args()
    
    # 计算from_time（默认过去3小时）
    from_time = args.from_time or (int(time.time()) - 10800)
    
    print(f"Search Date: {args.date}")
    print(f"From Time: {from_time}")
    
    results = search_macro(args.date, from_time, args.themes)
    
    # 统计
    success_count = sum(1 for v in results.values() if 'success' in v or 'data' in v)
    error_count = sum(1 for v in results.values() if 'error' in v)
    
    print(f'\n\n{"="*60}')
    print('MACRO SEARCH COMPLETE')
    print(f'Total: {len(results)} | Success: {success_count} | Failed: {error_count}')
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f'Results saved to: {args.output}')


if __name__ == '__main__':
    main()