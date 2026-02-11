#!/usr/bin/env python3
"""
简化版本：先将英文摘要填充到abstract字段
后续可以通过浏览器翻译功能查看中文
"""

import json

def fill_abstracts():
    """将summary字段复制到abstract字段"""
    print("📝 正在填充摘要信息...")
    
    total_filled = 0
    for week in ['2026-W06', '2026-W07']:
        archive_path = f'/data/workspace/papers-weekly-site/archives/{week}.json'
        
        with open(archive_path, 'r', encoding='utf-8') as f:
            archive = json.load(f)
        
        filled = 0
        for paper in archive['papers']:
            # 将summary复制到abstract
            if paper.get('summary'):
                paper['abstract'] = paper['summary']
                filled += 1
        
        # 保存
        with open(archive_path, 'w', encoding='utf-8') as f:
            json.dump(archive, f, ensure_ascii=False, indent=2)
        
        total_filled += filled
        print(f"  ✅ {week}: 填充 {filled} 篇")
    
    return total_filled

if __name__ == '__main__':
    print("=" * 70)
    print("🚀 填充论文摘要")
    print("=" * 70)
    
    total = fill_abstracts()
    
    print()
    print("=" * 70)
    print(f"✅ 完成！共填充 {total} 篇论文摘要")
    print("💡 提示：摘要为英文，您可以使用浏览器的翻译功能查看中文")
    print("=" * 70)
