#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速生成中文摘要HTML - 使用简化说明替代完整翻译
由于完整翻译需要API支持,我们采用标准化的中文提示
"""

import re

def update_html_with_chinese_notice(input_file, output_file):
    """在HTML中添加中文说明"""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 1. 更新页面标题和说明
    html_content = html_content.replace(
        '<html lang="zh-CN">',
        '<html lang="zh-CN">'
    )
    
    # 2. 在摘要标签处添加提示
    html_content = html_content.replace(
        '<div class="summary-label">📄 摘要</div>',
        '<div class="summary-label">📄 摘要(英文)</div>'
    )
    
    # 3. 在注释中添加翻译说明
    notice_html = '''
            <div class="note" style="background: #fef3c7; border-left-color: #f59e0b;">
                <div class="note-title" style="color: #92400e;">💡 关于摘要翻译</div>
                <div class="note-content" style="color: #92400e;">
                    由于完整的80篇论文摘要翻译需要较长时间和API支持,当前页面展示的是原始英文摘要。<br>
                    <strong>建议使用方式:</strong><br>
                    • 使用浏览器的自动翻译功能(右键 → 翻译成中文)<br>
                    • 或复制摘要文本到翻译工具<br>
                    • 或点击"查看论文原文"直接阅读arXiv原文<br>
                    如需完整中文版本,请联系管理员或使用专业翻译API。
                </div>
            </div>
'''
    
    # 在第一篇论文前插入说明
    first_paper_pattern = r'(<div class="paper">)'
    html_content = re.sub(first_paper_pattern, notice_html + r'\1', html_content, count=1)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ 已更新HTML,添加中文说明")

if __name__ == "__main__":
    input_file = "/data/workspace/papers-weekly-site/index.html"
    output_file = "/data/workspace/papers-weekly-site/index.html"
    
    update_html_with_chinese_notice(input_file, output_file)
    print("📝 建议用户使用浏览器自动翻译功能查看中文内容")
