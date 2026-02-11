#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
论文摘要翻译脚本 - 离线版本
提取所有英文摘要，准备批量翻译
"""

import re
import json

def extract_abstracts_with_positions(html_content):
    """从HTML中提取所有摘要及其位置信息"""
    pattern = r'<div class="summary-text">(.*?)</div>'
    abstracts = []
    for match in re.finditer(pattern, html_content, re.DOTALL):
        abstracts.append({
            'text': match.group(1).strip(),
            'start': match.start(1),
            'end': match.end(1)
        })
    return abstracts

def main():
    input_file = "/data/workspace/papers-weekly-site/index.html"
    
    # 读取HTML文件
    with open(input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 提取所有摘要
    abstracts = extract_abstracts_with_positions(html_content)
    print(f"找到 {len(abstracts)} 篇论文摘要")
    
    # 导出为JSON格式，方便翻译
    output_data = []
    for i, abstract in enumerate(abstracts, 1):
        output_data.append({
            'id': i,
            'english': abstract['text'],
            'chinese': ''  # 待翻译
        })
    
    # 保存到JSON文件
    with open('/data/workspace/papers-weekly-site/abstracts.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 已导出摘要到 abstracts.json")
    print(f"📝 共 {len(abstracts)} 篇摘要待翻译")
    
    # 打印前3篇作为预览
    print("\n前3篇摘要预览:")
    for item in output_data[:3]:
        print(f"\n--- 第{item['id']}篇 ---")
        print(f"{item['english'][:200]}...")

if __name__ == "__main__":
    main()
