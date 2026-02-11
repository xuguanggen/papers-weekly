#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HuggingFace Papers API 爬虫
使用官方API爬取每周精选论文
"""

import requests
import json
from datetime import datetime

def crawl_huggingface_papers_api(week='2026-W06'):
    """使用API爬取HuggingFace Papers"""
    
    api_url = f'https://huggingface.co/api/daily_papers?week={week}'
    print(f"🌐 正在访问API: {api_url}")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(api_url, headers=headers, timeout=30)
        response.raise_for_status()
        print(f"✅ API请求成功 (状态码: {response.status_code})")
        
        data = response.json()
        print(f"📦 获取到 {len(data)} 篇论文")
        
        papers = []
        
        for idx, item in enumerate(data, 1):
            try:
                paper_data = item.get('paper', {})
                
                # 提取论文ID
                paper_id = paper_data.get('id', '')
                
                # 提取标题
                title = paper_data.get('title', 'Untitled')
                
                # 提取作者
                authors_list = paper_data.get('authors', [])
                if authors_list:
                    # 提取作者名字
                    author_names = []
                    for author in authors_list:
                        name = author.get('name', '')
                        if name:
                            author_names.append(name)
                    authors = ', '.join(author_names) if author_names else 'Unknown Authors'
                else:
                    authors = 'Unknown Authors'
                
                # 提取摘要
                summary = paper_data.get('summary', '')
                if not summary:
                    summary = "No abstract available."
                
                # 构建arXiv URL
                url = f"https://arxiv.org/abs/{paper_id}"
                
                paper = {
                    'title': title.strip(),
                    'authors': authors.strip(),
                    'summary': summary.strip(),
                    'url': url
                }
                
                papers.append(paper)
                print(f"  [{idx}] {title[:60]}...")
                
            except Exception as e:
                print(f"  ⚠️  解析第{idx}条数据时出错: {e}")
                continue
        
        print(f"\n✅ 成功解析 {len(papers)} 篇论文")
        return papers
        
    except requests.RequestException as e:
        print(f"❌ API请求失败: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"❌ JSON解析失败: {e}")
        return []
    except Exception as e:
        print(f"❌ 爬取失败: {e}")
        return []

def save_papers(papers, week='2026-W06'):
    """保存论文到JSON文件"""
    
    output_file = f'/data/workspace/huggingface_papers_{week}.json'
    
    data = {
        'source': 'HuggingFace Papers',
        'week': week,
        'crawl_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'count': len(papers),
        'papers': papers
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"💾 已保存到: {output_file}")
    return output_file

if __name__ == "__main__":
    week = '2026-W06'
    print(f"🚀 开始爬取 HuggingFace Papers {week}")
    print("=" * 70)
    
    papers = crawl_huggingface_papers_api(week)
    
    if papers:
        output_file = save_papers(papers, week)
        print("\n" + "=" * 70)
        print(f"✅ 任务完成！")
        print(f"📊 共爬取 {len(papers)} 篇论文")
        print(f"📁 保存位置: {output_file}")
    else:
        print("\n❌ 未能爬取到论文数据")
