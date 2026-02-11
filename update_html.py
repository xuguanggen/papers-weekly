#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将JSON中的中文翻译应用回HTML文件
"""

import json
import re

def apply_translations_to_html(abstracts_json, input_html, output_html):
    """将翻译后的摘要应用到HTML"""
    
    # 读取翻译数据
    with open(abstracts_json, 'r', encoding='utf-8') as f:
        translations = json.load(f)
    
    # 读取HTML
    with open(input_html, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 提取所有摘要文本
    pattern = r'<div class="summary-text">(.*?)</div>'
    matches = list(re.finditer(pattern, html_content, re.DOTALL))
    
    print(f"HTML中找到 {len(matches)} 个摘要")
    print(f"JSON中有 {len(translations)} 条翻译")
    
    # 替换摘要
    new_html = html_content
    replaced_count = 0
    
    for i, match in enumerate(matches):
        trans_item = translations[i]
        original_text = match.group(1).strip()
        
        if trans_item['chinese']:
            # 有中文翻译,替换
            old_div = match.group(0)
            new_div = f'<div class="summary-text">{trans_item["chinese"]}</div>'
            new_html = new_html.replace(old_div, new_div, 1)
            replaced_count += 1
            print(f"✅ 第 {i+1} 篇: 已替换为中文")
        else:
            print(f"⏭️  第 {i+1} 篇: 暂无中文翻译,保留英文")
    
    # 保存
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    print(f"\n✅ 完成! 已替换 {replaced_count}/{len(matches)} 个摘要为中文")
    return replaced_count

if __name__ == "__main__":
    abstracts_json = "/data/workspace/papers-weekly-site/abstracts.json"
    input_html = "/data/workspace/papers-weekly-site/index.html"
    output_html = "/data/workspace/papers-weekly-site/index_updated.html"
    
    count = apply_translations_to_html(abstracts_json, input_html, output_html)
    
    if count > 0:
        # 备份原文件
        import shutil
        shutil.copy(input_html, input_html.replace('.html', '_backup.html'))
        print(f"📦 原文件已备份为 index_backup.html")
        
        # 使用新文件
        shutil.copy(output_html, input_html)
        print(f"🎉 index.html 已更新!")
