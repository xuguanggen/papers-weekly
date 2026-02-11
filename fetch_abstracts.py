#!/usr/bin/env python3
"""
从arXiv API获取论文的完整摘要信息
"""

import json
import urllib.request
import urllib.parse
import time
import xml.etree.ElementTree as ET
import re

def fetch_arxiv_abstract(arxiv_id):
    """从arXiv API获取论文摘要"""
    # 清理arxiv_id (移除版本号)
    clean_id = re.sub(r'v\d+$', '', arxiv_id)
    
    # arXiv API URL
    base_url = 'http://export.arxiv.org/api/query?'
    query = f'id_list={clean_id}'
    
    try:
        with urllib.request.urlopen(base_url + query) as response:
            data = response.read().decode('utf-8')
        
        # 解析XML
        root = ET.fromstring(data)
        
        # 命名空间
        ns = {
            'atom': 'http://www.w3.org/2005/Atom',
            'arxiv': 'http://arxiv.org/schemas/atom'
        }
        
        # 查找entry
        entry = root.find('atom:entry', ns)
        if entry is not None:
            # 获取摘要
            summary = entry.find('atom:summary', ns)
            if summary is not None:
                abstract = summary.text.strip()
                # 清理换行和多余空格
                abstract = ' '.join(abstract.split())
                return abstract
        
        return None
        
    except Exception as e:
        print(f"  ⚠️  获取失败 {arxiv_id}: {e}")
        return None

def main():
    print("🔄 开始获取论文摘要...")
    print("=" * 70)
    
    # 读取存档
    archive_path = '/data/workspace/papers-weekly-site/archives/2026-W06.json'
    with open(archive_path, 'r', encoding='utf-8') as f:
        archive = json.load(f)
    
    total = len(archive['papers'])
    success = 0
    failed = 0
    mapped = 0
    api_fetched = 0
    
    print(f"📊 总计: {total} 篇论文")
    print()
    
    for i, paper in enumerate(archive['papers'], 1):
        arxiv_id = paper.get('arxiv_id', '')
        title = paper['title'][:50]
        current_abstract = paper.get('abstract', '').strip()
        
        # 检查是否已有有效摘要（不是占位符）
        placeholder_keywords = ['待获取', '暂时无法获取', '摘要信息待获取']
        is_placeholder = any(kw in current_abstract for kw in placeholder_keywords)
        
        if current_abstract and not is_placeholder:
            print(f"[{i}/{total}] ✅ 已有有效摘要: {title}...")
            success += 1
            continue
        
        # 优先使用summary字段（中文摘要），但要检查是否是占位符
        summary = paper.get('summary', '').strip()
        summary_is_placeholder = any(kw in summary for kw in placeholder_keywords)
        
        if summary and not summary_is_placeholder:
            paper['abstract'] = paper['summary']
            print(f"[{i}/{total}] 📝 映射summary→abstract: {title}...")
            mapped += 1
            success += 1
            continue
        
        # 如果没有summary，尝试从arXiv API获取
        if not arxiv_id:
            print(f"[{i}/{total}] ⚠️  缺少arxiv_id: {title}...")
            paper['abstract'] = "摘要信息暂时无法获取，请点击下方链接查看完整论文"
            failed += 1
            continue
        
        # 从arXiv API获取
        print(f"[{i}/{total}] 🔍 从API获取... {arxiv_id}: {title}...")
        abstract = fetch_arxiv_abstract(arxiv_id)
        
        if abstract:
            paper['abstract'] = abstract
            api_fetched += 1
            success += 1
            print(f"         ✅ 成功 ({len(abstract)} 字符)")
        else:
            paper['abstract'] = "摘要信息暂时无法获取，请点击下方链接查看完整论文"
            failed += 1
            print(f"         ❌ 失败")
        
        # 避免请求过快
        if i % 10 == 0:
            print(f"  ⏸️  休息3秒... (已处理 {i}/{total})")
            time.sleep(3)
        else:
            time.sleep(0.5)
    
    # 保存更新后的存档
    with open(archive_path, 'w', encoding='utf-8') as f:
        json.dump(archive, f, ensure_ascii=False, indent=2)
    
    print()
    print("=" * 70)
    print("✅ 完成！")
    print(f"📊 统计:")
    print(f"  成功: {success} 篇")
    print(f"    - 映射summary: {mapped} 篇")
    print(f"    - API获取: {api_fetched} 篇")
    print(f"  失败: {failed} 篇")
    print(f"  总计: {total} 篇")

if __name__ == '__main__':
    main()
