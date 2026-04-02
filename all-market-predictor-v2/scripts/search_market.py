# -*- coding: utf-8 -*-
"""
市场数据批量搜索脚本 - Market Predictor V2
用于批量搜索ETF、LOF、QDII、场外基金等资产的市场数据
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

# 默认资产关键词映射
DEFAULT_ASSETS = {
    # 大宗商品
    '黄金ETF': ('黄金ETF 518880', '518880'),
    '原油QDII': ('原油QDII基金 石油LOF', '161129'),
    
    # 跨境ETF
    '纳斯达克ETF': ('纳斯达克ETF 513100', '513100'),
    '标普500ETF': ('标普500ETF 513500', '513500'),
    '恒生科技ETF': ('恒生科技ETF 513180', '513180'),
    '港美互联网ETF': ('港美互联网ETF 中概互联 513050', '513050'),
    '日经ETF': ('日经225ETF 513880', '513880'),
    '亚太精选ETF': ('亚太精选ETF 159687', '159687'),
    
    # 行业ETF
    '半导体ETF': ('半导体ETF 512480', '512480'),
    '军工ETF': ('军工ETF 512660', '512660'),
    '新能源ETF': ('新能源ETF 516160', '516160'),
    '银行ETF': ('银行ETF 512800', '512800'),
    '红利ETF': ('红利ETF 510880', '510880'),
    '医疗ETF': ('医疗ETF 512170', '512170'),
    '创业板ETF': ('创业板ETF 159915', '159915'),
    '电力ETF': ('电力ETF 159611', '159611'),
    '现金流ETF': ('现金流ETF 159399', '159399'),
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


def batch_search(assets: list, date_str: str, from_time: int = None) -> dict:
    """批量搜索多个资产"""
    results = {}
    
    for name in assets:
        if name not in DEFAULT_ASSETS:
            print(f"Warning: Unknown asset '{name}', skipping...")
            continue
            
        keyword_template, code = DEFAULT_ASSETS[name]
        keyword = f"{keyword_template} {date_str}"
        
        print(f"\n{'='*60}")
        print(f'Searching: {name} ({code})')
        print(f'Keyword: {keyword}')
        print(f'{"="*60}')
        
        result = search(keyword, from_time)
        
        if result.get('success'):
            results[name] = {
                'code': code,
                'data': result
            }
            # 输出message字段
            print(result.get('message', '(无消息)'))
        else:
            results[name] = {
                'code': code,
                'error': result.get('error', result.get('message', 'Unknown error'))
            }
            print(f"ERROR: {results[name]['error']}")
    
    return results


def main():
    parser = argparse.ArgumentParser(description='批量搜索市场数据')
    parser.add_argument('--date', type=str, required=True, help='搜索日期，如 "2026年3月29日"')
    parser.add_argument('--from-time', type=int, help='起始时间戳（秒）')
    parser.add_argument('--assets', type=str, nargs='*', help='要搜索的资产列表')
    parser.add_argument('--output', type=str, help='输出文件路径（JSON）')
    
    args = parser.parse_args()
    
    # 默认搜索所有资产
    assets = args.assets if args.assets else list(DEFAULT_ASSETS.keys())
    
    # 计算from_time（默认过去3小时）
    from_time = args.from_time or (int(time.time()) - 10800)
    
    print(f"Search Date: {args.date}")
    print(f"From Time: {from_time}")
    print(f"Assets: {assets}")
    
    results = batch_search(assets, args.date, from_time)
    
    # 统计结果
    success_count = sum(1 for v in results.values() if 'data' in v)
    error_count = sum(1 for v in results.values() if 'error' in v)
    
    print(f'\n\n{"="*60}')
    print('SEARCH COMPLETE')
    print(f'Total: {len(assets)} | Success: {success_count} | Failed: {error_count}')
    
    # 可选：保存结果到文件
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f'Results saved to: {args.output}')


if __name__ == '__main__':
    main()