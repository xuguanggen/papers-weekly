#!/usr/bin/env python3
"""
爬取HuggingFace Papers的多周数据，自动翻译摘要为中文
"""

import json
import urllib.request
import urllib.parse
import time
import re
from datetime import datetime

def fetch_huggingface_papers(week):
    """
    从HuggingFace API获取指定周的论文
    week格式: YYYY-WWW (例如: 2026-W06)
    """
    api_url = f'https://huggingface.co/api/daily_papers?week={week}'
    
    print(f"\n🔍 正在爬取 {week} 的论文...")
    
    try:
        with urllib.request.urlopen(api_url, timeout=30) as response:
            data = json.loads(response.read().decode('utf-8'))
        
        papers = []
        for item in data:
            paper = item.get('paper', {})
            
            # 提取论文ID (去除v版本号)
            arxiv_id = paper.get('id', '')
            clean_id = re.sub(r'v\d+$', '', arxiv_id)
            
            # 构建论文数据
            paper_data = {
                'title': paper.get('title', ''),
                'authors': ', '.join([author.get('name', '') for author in paper.get('authors', [])]),
                'summary': paper.get('summary', ''),  # 原始英文摘要
                'abstract': '',  # 将用于中文翻译
                'arxiv_id': arxiv_id,
                'url': f'https://arxiv.org/abs/{clean_id}',
                'published': paper.get('publishedAt', ''),
                'upvotes': item.get('upvotes', 0)
            }
            
            papers.append(paper_data)
        
        print(f"✅ 成功获取 {len(papers)} 篇论文")
        return papers
        
    except Exception as e:
        print(f"❌ 爬取失败: {e}")
        return []

def translate_abstract_to_chinese(english_text, title):
    """
    将英文摘要翻译成中文
    这里使用简单的标记，实际翻译需要在后续步骤完成
    """
    # 标记为待翻译
    return {
        'original': english_text,
        'title': title,
        'status': 'pending'
    }

def create_archive(week, papers):
    """创建周存档文件"""
    # 解析周次信息
    year, week_num = week.split('-W')
    
    # 获取该周的日期（周一）
    from datetime import datetime, timedelta
    jan_4 = datetime(int(year), 1, 4)
    week_start = jan_4 + timedelta(weeks=int(week_num)-1, days=-jan_4.weekday())
    date_str = week_start.strftime('%Y-%m-%d')
    
    archive = {
        'week': week,
        'date': date_str,
        'count': len(papers),
        'papers': papers
    }
    
    return archive

def main():
    print("=" * 70)
    print("🚀 HuggingFace Papers 多周爬虫")
    print("=" * 70)
    
    # 要爬取的周次
    weeks = ['2026-W06', '2026-W07']
    
    all_archives = []
    total_papers = 0
    
    for week in weeks:
        # 获取论文
        papers = fetch_huggingface_papers(week)
        
        if papers:
            # 创建存档
            archive = create_archive(week, papers)
            all_archives.append(archive)
            total_papers += len(papers)
            
            # 保存单周存档
            archive_path = f'/data/workspace/papers-weekly-site/archives/{week}.json'
            with open(archive_path, 'w', encoding='utf-8') as f:
                json.dump(archive, f, ensure_ascii=False, indent=2)
            
            print(f"💾 已保存: {archive_path}")
        
        # 避免请求过快
        time.sleep(2)
    
    # 创建存档索引
    index = {
        'archives': [
            {
                'week': arch['week'],
                'date': arch['date'],
                'count': arch['count']
            }
            for arch in sorted(all_archives, key=lambda x: x['week'], reverse=True)
        ]
    }
    
    index_path = '/data/workspace/papers-weekly-site/archives/index.json'
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    
    print("\n" + "=" * 70)
    print("✅ 爬取完成！")
    print("=" * 70)
    print(f"📊 统计:")
    print(f"  爬取周数: {len(weeks)}")
    print(f"  论文总数: {total_papers}")
    print(f"  存档文件: {len(all_archives)}")
    print()
    
    # 保存待翻译列表
    pending_translations = []
    for archive in all_archives:
        for paper in archive['papers']:
            if paper.get('summary'):
                pending_translations.append({
                    'week': archive['week'],
                    'title': paper['title'],
                    'english': paper['summary']
                })
    
    translation_file = '/data/workspace/papers-weekly-site/pending_translations.json'
    with open(translation_file, 'w', encoding='utf-8') as f:
        json.dump(pending_translations, f, ensure_ascii=False, indent=2)
    
    print(f"📝 待翻译摘要: {len(pending_translations)} 篇")
    print(f"💾 翻译列表已保存: {translation_file}")
    print()
    print("⏭️  下一步: 运行翻译脚本将所有摘要翻译成中文")

if __name__ == '__main__':
    main()
