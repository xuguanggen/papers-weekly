#!/usr/bin/env python3
"""
智能论文爬虫 - 带LLM分析和评分
"""
import requests
import json
import time
from datetime import datetime

def fetch_weekly_papers(week):
    """从HuggingFace爬取指定周的论文"""
    print(f"🔍 正在爬取 {week} 的论文...")
    url = f'https://huggingface.co/api/daily_papers?week={week}'
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        papers = response.json()
        print(f"✅ 成功获取 {len(papers)} 篇论文")
        return papers
    except Exception as e:
        print(f"❌ 爬取失败: {e}")
        return []

def analyze_paper_relevance(title, abstract):
    """
    分析论文与特定领域的相关度
    返回: {game, efficiency, llm, agent, total}
    """
    # 这里我们会用简单的关键词匹配来模拟LLM分析
    # 实际使用时可以调用真实的LLM API
    
    title_lower = title.lower()
    abstract_lower = abstract.lower()
    text = f"{title_lower} {abstract_lower}"
    
    # 游戏相关关键词
    game_keywords = [
        'game', 'gaming', 'player', 'gameplay', 'video game',
        'reinforcement learning', 'simulation', 'environment',
        'unity', 'unreal', '3d', 'virtual', 'interactive'
    ]
    
    # 工程提效关键词
    efficiency_keywords = [
        'efficiency', 'optimization', 'performance', 'speed',
        'acceleration', 'fast', 'efficient', 'scalable',
        'engineering', 'deployment', 'production', 'inference',
        'compilation', 'quantization', 'pruning', 'compression'
    ]
    
    # LLM相关关键词
    llm_keywords = [
        'language model', 'llm', 'gpt', 'transformer', 'bert',
        'pretrain', 'fine-tuning', 'prompt', 'instruction',
        'generation', 'nlp', 'natural language', 'chat',
        'reasoning', 'understanding', 'text'
    ]
    
    # Agent相关关键词
    agent_keywords = [
        'agent', 'autonomous', 'planning', 'reasoning',
        'decision making', 'tool use', 'action', 'policy',
        'multi-agent', 'collaboration', 'interaction',
        'embodied', 'robot', 'control'
    ]
    
    def calculate_score(keywords, max_score=10):
        """基于关键词匹配计算分数"""
        matches = sum(1 for kw in keywords if kw in text)
        # 归一化到0-10分
        score = min(max_score, matches * 2)
        return score
    
    game_score = calculate_score(game_keywords)
    efficiency_score = calculate_score(efficiency_keywords)
    llm_score = calculate_score(llm_keywords)
    agent_score = calculate_score(agent_keywords)
    
    # 计算总分（加权）
    total_score = (game_score * 1.0 + 
                   efficiency_score * 1.2 + 
                   llm_score * 1.5 + 
                   agent_score * 1.3)
    
    return {
        'game': round(game_score, 1),
        'efficiency': round(efficiency_score, 1),
        'llm': round(llm_score, 1),
        'agent': round(agent_score, 1),
        'total': round(total_score, 1)
    }

def process_papers(raw_papers):
    """处理和分析论文"""
    processed = []
    
    for i, paper in enumerate(raw_papers, 1):
        print(f"📊 分析论文 {i}/{len(raw_papers)}: {paper.get('title', 'Unknown')[:50]}...")
        
        title = paper.get('title', '')
        abstract = paper.get('summary', '')
        
        # 分析相关度
        scores = analyze_paper_relevance(title, abstract)
        
        # 正确提取作者信息 - 从 paper.authors 中获取
        paper_obj = paper.get('paper', {})
        authors_list = paper_obj.get('authors', [])
        if authors_list:
            # 提取作者姓名
            authors = ', '.join([a.get('name', '') for a in authors_list[:5] if a.get('name')])
        else:
            authors = '作者信息待获取'
        
        # 正确提取arXiv ID - 从 paper.id 中获取
        arxiv_id = paper_obj.get('id', '')
        if arxiv_id:
            url = f"https://arxiv.org/abs/{arxiv_id}"
        else:
            # 备用方案：尝试从其他字段获取
            url = paper.get('arxivId', '')
            if url and not url.startswith('http'):
                url = f"https://arxiv.org/abs/{url}"
        
        processed_paper = {
            'title': title,
            'authors': authors,
            'abstract': abstract,  # 英文摘要，稍后翻译
            'abstract_zh': '',  # 待翻译
            'url': url,
            'publishedAt': paper.get('publishedAt', ''),
            'scores': scores
        }
        
        processed.append(processed_paper)
        time.sleep(0.1)  # 避免过快
    
    return processed

def main():
    print("=" * 70)
    print("🚀 智能论文爬虫与分析系统")
    print("=" * 70)
    
    # 1. 爬取论文
    week = '2026-W07'
    raw_papers = fetch_weekly_papers(week)
    
    if not raw_papers:
        print("❌ 没有获取到论文数据")
        return
    
    # 2. 分析论文
    print(f"\n📊 开始分析 {len(raw_papers)} 篇论文...")
    processed_papers = process_papers(raw_papers)
    
    # 3. 按总分降序排序
    processed_papers.sort(key=lambda x: x['scores']['total'], reverse=True)
    
    # 4. 添加排序后的序号
    for i, paper in enumerate(processed_papers, 1):
        paper['rank'] = i
    
    # 5. 保存结果
    output = {
        'week': week,
        'total': len(processed_papers),
        'generated_at': datetime.now().isoformat(),
        'papers': processed_papers
    }
    
    output_file = f'/data/workspace/papers-weekly-site/archives/{week}.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 分析完成！结果已保存到: {output_file}")
    
    # 6. 显示Top 10
    print("\n" + "=" * 70)
    print("🏆 Top 10 最相关论文:")
    print("=" * 70)
    
    for paper in processed_papers[:10]:
        print(f"\n#{paper['rank']} {paper['title'][:60]}...")
        print(f"   🎮 游戏: {paper['scores']['game']} | "
              f"⚡ 提效: {paper['scores']['efficiency']} | "
              f"🤖 LLM: {paper['scores']['llm']} | "
              f"🎯 Agent: {paper['scores']['agent']} | "
              f"💯 总分: {paper['scores']['total']}")
    
    # 7. 更新索引
    index_data = {
        'archives': [
            {
                'week': week,
                'date': '2026-02-09',
                'count': len(processed_papers)
            }
        ]
    }
    
    with open('/data/workspace/papers-weekly-site/archives/index.json', 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n📝 待翻译摘要数量: {len(processed_papers)}")
    print("💡 下一步: 运行翻译脚本将摘要翻译成中文")

if __name__ == '__main__':
    main()
