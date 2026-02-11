#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每周论文爬虫 - 支持多日期存档
"""

import json
import os
from datetime import datetime
import shutil

def create_weekly_archive():
    """创建本周的论文存档"""
    
    # 获取当前日期
    current_date = datetime.now().strftime('%Y-%m-%d')
    current_week = datetime.now().strftime('%Y-W%W')  # 例如: 2026-W07
    
    # 创建存档目录
    archive_dir = "/data/workspace/papers-weekly-site/archives"
    os.makedirs(archive_dir, exist_ok=True)
    
    # 读取所有论文数据 (使用修复后的数据源)
    data_file = '/data/workspace/papers_data_fixed.json'
    if not os.path.exists(data_file):
        data_file = '/data/workspace/papers_data.json'
    
    with open(data_file, 'r', encoding='utf-8') as f:
        all_papers = json.load(f)
    
    # 确保所有论文都有URL
    import re
    for paper in all_papers:
        if not paper.get('url') or paper['url'] == '待获取':
            arxiv_id = paper.get('arxiv_id', '')
            if arxiv_id:
                clean_id = re.sub(r'v\d+$', '', arxiv_id)
                paper['url'] = f'https://arxiv.org/abs/{clean_id}'
    
    print(f"📚 找到 {len(all_papers)} 篇论文")
    
    # 创建本周存档
    archive_data = {
        'date': current_date,
        'week': current_week,
        'count': len(all_papers),
        'papers': all_papers
    }
    
    # 保存到存档文件
    archive_file = f"{archive_dir}/{current_week}.json"
    with open(archive_file, 'w', encoding='utf-8') as f:
        json.dump(archive_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 已创建存档: {archive_file}")
    
    # 更新索引文件
    index_file = f"{archive_dir}/index.json"
    if os.path.exists(index_file):
        with open(index_file, 'r', encoding='utf-8') as f:
            index = json.load(f)
    else:
        index = {'archives': []}
    
    # 检查是否已存在该周的存档
    existing = [a for a in index['archives'] if a['week'] == current_week]
    if existing:
        # 更新现有存档
        for a in index['archives']:
            if a['week'] == current_week:
                a['date'] = current_date
                a['count'] = len(all_papers)
        print(f"🔄 更新存档: {current_week}")
    else:
        # 添加新存档
        index['archives'].insert(0, {
            'week': current_week,
            'date': current_date,
            'count': len(all_papers)
        })
        print(f"➕ 添加新存档: {current_week}")
    
    # 保存索引
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 索引已更新")
    return archive_data

if __name__ == "__main__":
    create_weekly_archive()
