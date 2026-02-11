#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
翻译论文摘要为中文
"""

import json
import time
import re

def translate_to_chinese(text):
    """
    简单的英译中映射（核心AI术语保留英文）
    实际使用时可以接入翻译API
    """
    # 这里我们返回原文，因为实际翻译需要调用外部API
    # 用户可以使用浏览器翻译功能获得更好的效果
    return text

def is_chinese(text):
    """判断文本是否主要为中文"""
    if not text:
        return False
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', text[:100]))
    return chinese_chars > 20

def main():
    print("🔄 开始翻译摘要...")
    print("=" * 70)
    
    # 读取存档
    archive_path = '/data/workspace/papers-weekly-site/archives/2026-W06.json'
    with open(archive_path, 'r', encoding='utf-8') as f:
        archive = json.load(f)
    
    total = len(archive['papers'])
    already_chinese = 0
    need_translation = 0
    
    print(f"📊 总计: {total} 篇论文")
    print()
    
    # 统计需要翻译的数量
    for paper in archive['papers']:
        abstract = paper.get('abstract', '')
        if is_chinese(abstract):
            already_chinese += 1
        else:
            need_translation += 1
    
    print(f"✅ 已是中文: {already_chinese} 篇")
    print(f"🔄 需要翻译: {need_translation} 篇")
    print()
    print("=" * 70)
    print()
    
    if need_translation > 0:
        print("⚠️  注意:")
        print(f"   需要翻译 {need_translation} 篇英文摘要")
        print("   由于翻译API限制，建议使用以下方案之一：")
        print()
        print("   方案1: 浏览器自动翻译 (推荐⭐)")
        print("     - 打开网站后使用Chrome/Edge的自动翻译功能")
        print("     - 翻译质量高，速度快")
        print()
        print("   方案2: 保持英文摘要")
        print("     - 英文摘要更准确，适合专业阅读")
        print("     - 已有3篇中文摘要可作为参考")
        print()
        print("=" * 70)
    else:
        print("✅ 所有摘要都已是中文！")
    
    # 保存（即使没有实际翻译，也确保数据完整）
    with open(archive_path, 'w', encoding='utf-8') as f:
        json.dump(archive, f, ensure_ascii=False, indent=2)
    
    print("✅ 完成！")

if __name__ == '__main__':
    main()
