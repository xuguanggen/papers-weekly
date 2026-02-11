#!/bin/bash
# 每周论文更新脚本
# 建议每周一凌晨自动执行

set -e

echo "🚀 开始更新论文周刊..."
echo "📅 当前时间: $(date '+%Y-%m-%d %H:%M:%S')"

cd /data/workspace/papers-weekly-site

# 1. 运行爬虫(假设你有爬虫脚本)
echo "📡 正在爬取最新论文..."
# python3 /path/to/your/crawler.py

# 2. 创建新的周存档
echo "📦 创建本周存档..."
python3 weekly_crawler.py

# 3. 提交到Git
echo "📝 提交更新..."
git add archives/
git commit -m "chore: Update weekly papers archive - $(date '+%Y-W%W')" || true

# 4. 推送到GitHub  
echo "🌐 推送到GitHub..."
git push origin master

echo "✅ 更新完成！"
echo "📊 本周论文已添加到存档"
