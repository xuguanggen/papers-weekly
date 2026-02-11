# 📚 AI 论文周刊系统

一个支持多日期存档的AI论文周刊展示系统。

## ✨ 功能特点

- 📅 **日期导航**: 左侧边栏显示所有历史周刊，点击切换查看
- 📊 **论文数量**: 当前版本包含 **105篇论文** (从原来的80篇升级)
- 🔍 **实时搜索**: 支持按标题、作者、摘要搜索
- 📱 **响应式设计**: 完美支持手机、平板、电脑
- 🎨 **精美UI**: 紫色渐变设计，流畅动画效果

## 📁 项目结构

```
papers-weekly-site/
├── index.html              # 主页面
├── archives/               # 存档目录
│   ├── index.json         # 存档索引
│   ├── 2026-W06.json      # 第6周论文数据
│   └── 2026-W07.json      # 第7周论文数据 (示例)
├── weekly_crawler.py       # 每周爬虫脚本
└── auto_update.sh          # 自动更新脚本
```

## 🚀 使用指南

### 1. 每周更新论文

手动更新：
```bash
# 确保 /data/workspace/all_papers.json 已更新
python3 weekly_crawler.py
```

自动更新(推荐)：
```bash
# 设置定时任务，每周一执行
./auto_update.sh
```

### 2. 部署到GitHub Pages

```bash
git add archives/
git commit -m "chore: Update weekly papers"
git push origin master
```

GitHub Pages会自动部署更新(约1-2分钟)。

### 3. 查看网站

访问: **https://xuguanggen.github.io/papers-weekly/**

## 📝 存档格式

每周存档文件 (`archives/YYYY-WWW.json`):

```json
{
  "date": "2026-02-11",
  "week": "2026-W06", 
  "count": 105,
  "papers": [
    {
      "title": "论文标题",
      "authors": "作者列表",
      "summary": "摘要内容",
      "url": "arXiv链接"
    }
  ]
}
```

存档索引 (`archives/index.json`):

```json
{
  "archives": [
    {
      "week": "2026-W06",
      "date": "2026-02-11",
      "count": 105
    }
  ]
}
```

## 🔧 定时任务设置

使用 `cron` 设置每周自动更新:

```bash
# 编辑 crontab
crontab -e

# 添加以下行(每周一凌晨2点执行)
0 2 * * 1 /data/workspace/papers-weekly-site/auto_update.sh >> /tmp/papers-weekly.log 2>&1
```

## 🎯 未来功能计划

- [ ] 添加论文分类筛选(NLP、CV、RL等)
- [ ] 支持论文收藏功能
- [ ] 添加论文统计图表
- [ ] 支持导出PDF周报
- [ ] 添加RSS订阅功能

## 📞 联系方式

如有问题或建议，请通过GitHub Issues反馈。

---

**最后更新**: 2026-02-11  
**当前版本**: v2.0 (105篇论文 + 日期导航)
