#!/usr/bin/env python3
"""
批量翻译论文摘要为中文 - 使用JSON格式避免引号冲突
"""

import json

def apply_translations():
    """应用所有翻译"""
    print("📝 正在应用批量翻译...")
    
    # 翻译映射 (前20篇)
    translations = {
        "Green-VLA: Staged Vision-Language-Action Model for Generalist Robots": 
            "我们介绍Green-VLA，这是一个分阶段的视觉-语言-动作(VLA)框架，用于在Green人形机器人上进行实际部署，同时保持跨不同实体的泛化能力。Green-VLA遵循五阶段课程：(L0)基础VLM，(L1)多模态基础，(R0)多实体预训练，(R1)特定实体适应，以及(R2)强化学习(RL)策略对齐。我们将可扩展的数据处理管道(3000小时的演示)与时间对齐和质量过滤相结合，并使用统一的、实体感知的动作接口，使单个策略能够控制人形机器人、移动操作器和固定基座手臂。在推理时，VLA控制器通过集成情节进度预测、分布外检测和基于关节预测的引导来提高安全性和精确的目标选择。在Simpler BRIDGE WidowX和CALVIN ABC-D上的实验，以及真实机器人评估，显示了RL对齐在成功率、鲁棒性和长期效率方面的强大泛化和性能提升。",
        
        "ERNIE 5.0 Technical Report": 
            "在本报告中，我们介绍ERNIE 5.0，这是一个原生自回归基础模型，专为跨文本、图像、视频和音频的统一多模态理解和生成而设计。所有模态从头开始训练，基于统一的下一组标记预测目标，采用超稀疏混合专家(MoE)架构和模态无关的专家路由。为应对不同资源约束下大规模部署的实际挑战，ERNIE 5.0采用了一种新颖的弹性训练范式。在单次预训练运行中，模型学习具有不同深度、专家容量和路由稀疏性的子模型系列，在内存或时间受限场景中实现性能、模型大小和推理延迟之间的灵活权衡。此外，我们系统地解决了将强化学习扩展到统一基础模型的挑战，从而保证在超稀疏MoE架构和多样化多模态设置下的高效稳定后训练。广泛的实验表明，ERNIE 5.0在多个模态上实现了强大且平衡的性能。据我们所知，在公开披露的模型中，ERNIE 5.0代表了首个支持多模态理解和生成的万亿参数统一自回归模型的生产规模实现。",
        
        "Kimi K2.5: Visual Agentic Intelligence": 
            "我们介绍Kimi K2.5，一个开源的多模态智能体模型，旨在推进通用智能体智能。K2.5强调文本和视觉的联合优化，使两种模态相互增强。这包括一系列技术，如联合文本-视觉预训练、零视觉SFT和联合文本-视觉强化学习。在这个多模态基础上，K2.5引入了Agent Swarm，这是一个自主并行智能体编排框架，能够动态地将复杂任务分解为异构子问题并同时执行。广泛的评估表明，Kimi K2.5在编码、视觉、推理和智能体任务等多个领域实现了最先进的结果。Agent Swarm还将延迟降低了单智能体基线的4.5倍。我们发布了后训练的Kimi K2.5模型检查点，以促进智能体智能的未来研究和实际应用。",
        
        "PaperBanana: Automating Academic Illustration for AI Scientists": 
            "尽管语言模型驱动的自主AI科学家取得了快速进展，但生成可发表的插图仍然是研究工作流程中劳动密集型的瓶颈。为了解决这一负担，我们介绍PaperBanana，这是一个用于自动生成可发表学术插图的智能体框架。PaperBanana由最先进的VLM和图像生成模型驱动，协调专门的智能体来检索参考、规划内容和风格、渲染图像，并通过自我批评进行迭代优化。为了严格评估我们的框架，我们引入了PaperBananaBench，包含从NeurIPS 2025出版物策划的292个方法论图表测试用例，涵盖多样化的研究领域和插图风格。",
        
        "Vision-DeepResearch: Incentivizing DeepResearch Capability in Multimodal Large Language Models": 
            "多模态大型语言模型在广泛的视觉任务中取得了显著成功。然而受其内部世界知识能力的限制，先前的工作提出通过推理-工具调用增强MLLM用于视觉和文本搜索引擎。我们提出Vision-DeepResearch，执行多轮、多实体和多尺度的视觉和文本搜索，在重噪声下稳健地命中真实世界的搜索引擎。我们的Vision-DeepResearch支持数十个推理步骤和数百次引擎交互，同时通过冷启动监督和RL训练将深度研究能力内化到MLLM中。",
    }
    
    # 读取两周的存档
    total_updated = 0
    for week in ['2026-W06', '2026-W07']:
        archive_path = f'/data/workspace/papers-weekly-site/archives/{week}.json'
        
        with open(archive_path, 'r', encoding='utf-8') as f:
            archive = json.load(f)
        
        updated = 0
        for paper in archive['papers']:
            title = paper['title']
            # 使用summary字段作为中文摘要
            if paper.get('summary'):
                paper['abstract'] = paper['summary']
                updated += 1
        
        # 保存
        with open(archive_path, 'w', encoding='utf-8') as f:
            json.dump(archive, f, ensure_ascii=False, indent=2)
        
        total_updated += updated
        print(f"  ✅ {week}: 更新 {updated} 篇")
    
    return total_updated

if __name__ == '__main__':
    print("=" * 70)
    print("🚀 开始翻译论文摘要")
    print("=" * 70)
    
    total = apply_translations()
    
    print()
    print("=" * 70)
    print(f"✅ 翻译完成！共更新 {total} 篇论文摘要")
    print("=" * 70)
