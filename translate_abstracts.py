#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
论文摘要翻译脚本
从HTML文件中提取英文摘要，翻译成中文后更新HTML
"""

import re
import os
import time
from openai import OpenAI

def extract_abstracts(html_content):
    """从HTML中提取所有摘要"""
    pattern = r'<div class="summary-text">(.*?)</div>'
    abstracts = re.findall(pattern, html_content, re.DOTALL)
    return abstracts

def translate_abstract(text, client):
    """使用OpenAI API翻译摘要"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "你是一个专业的学术论文翻译专家。请将以下英文摘要翻译成中文，保持学术性和专业性，翻译要准确流畅。只输出翻译后的中文，不要有任何额外说明。"},
                {"role": "user", "content": text}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"翻译出错: {e}")
        return text  # 出错时返回原文

def translate_html(input_file, output_file):
    """翻译HTML文件中的所有摘要"""
    print("开始翻译论文摘要...")
    
    # 读取HTML文件
    with open(input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 提取所有摘要
    abstracts = extract_abstracts(html_content)
    print(f"找到 {len(abstracts)} 篇论文摘要")
    
    # 初始化OpenAI客户端（使用环境变量中的API Key）
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("错误: 未找到 OPENAI_API_KEY 环境变量")
        return False
    
    client = OpenAI(api_key=api_key)
    
    # 翻译每个摘要并替换
    new_html = html_content
    for i, abstract in enumerate(abstracts, 1):
        print(f"\n正在翻译第 {i}/{len(abstracts)} 篇...")
        print(f"原文预览: {abstract[:100]}...")
        
        # 翻译
        translated = translate_abstract(abstract, client)
        print(f"译文预览: {translated[:100]}...")
        
        # 替换HTML中的内容
        new_html = new_html.replace(
            f'<div class="summary-text">{abstract}</div>',
            f'<div class="summary-text">{translated}</div>',
            1  # 只替换第一次出现
        )
        
        # 避免API限流，稍作延迟
        time.sleep(0.5)
    
    # 保存新文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    print(f"\n✅ 翻译完成！已保存到: {output_file}")
    return True

if __name__ == "__main__":
    input_file = "/data/workspace/papers-weekly-site/index.html"
    output_file = "/data/workspace/papers-weekly-site/index_zh.html"
    
    success = translate_html(input_file, output_file)
    
    if success:
        # 备份原文件
        os.rename(input_file, input_file.replace('.html', '_en.html'))
        # 使用翻译后的文件作为新的index.html
        os.rename(output_file, input_file)
        print("✅ 已更新 index.html 为中文版本")
        print("📝 原英文版本已保存为 index_en.html")
