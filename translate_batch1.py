#!/usr/bin/env python3
"""
批量翻译论文摘要为中文
"""

import json
import time

# 第1批翻译 (论文1-10)
translations_batch1 = {
    "Green-VLA: Staged Vision-Language-Action Model for Generalist Robots": 
        "我们介绍Green-VLA，这是一个分阶段的视觉-语言-动作(VLA)框架，用于在Green人形机器人上进行实际部署，同时保持跨不同实体的泛化能力。Green-VLA遵循五阶段课程：(L0)基础VLM，(L1)多模态基础，(R0)多实体预训练，(R1)特定实体适应，以及(R2)强化学习(RL)策略对齐。我们将可扩展的数据处理管道(3000小时的演示)与时间对齐和质量过滤相结合，并使用统一的、实体感知的动作接口，使单个策略能够控制人形机器人、移动操作器和固定基座手臂。在推理时，VLA控制器通过集成情节进度预测、分布外检测和基于关节预测的引导来提高安全性和精确的目标选择。在Simpler BRIDGE WidowX和CALVIN ABC-D上的实验，以及真实机器人评估，显示了RL对齐在成功率、鲁棒性和长期效率方面的强大泛化和性能提升。",
    
    "ERNIE 5.0 Technical Report": 
        "在本报告中，我们介绍ERNIE 5.0，这是一个原生自回归基础模型，专为跨文本、图像、视频和音频的统一多模态理解和生成而设计。所有模态从头开始训练，基于统一的下一组标记预测目标，采用超稀疏混合专家(MoE)架构和模态无关的专家路由。为应对不同资源约束下大规模部署的实际挑战，ERNIE 5.0采用了一种新颖的弹性训练范式。在单次预训练运行中，模型学习具有不同深度、专家容量和路由稀疏性的子模型系列，在内存或时间受限场景中实现性能、模型大小和推理延迟之间的灵活权衡。此外，我们系统地解决了将强化学习扩展到统一基础模型的挑战，从而保证在超稀疏MoE架构和多样化多模态设置下的高效稳定后训练。广泛的实验表明，ERNIE 5.0在多个模态上实现了强大且平衡的性能。据我们所知，在公开披露的模型中，ERNIE 5.0代表了首个支持多模态理解和生成的万亿参数统一自回归模型的生产规模实现。为促进进一步研究，我们展示了统一模型中模态无关专家路由的详细可视化，以及弹性训练的全面实证分析，旨在为社区提供深刻见解。",
    
    "Kimi K2.5: Visual Agentic Intelligence": 
        "我们介绍Kimi K2.5，一个开源的多模态智能体模型，旨在推进通用智能体智能。K2.5强调文本和视觉的联合优化，使两种模态相互增强。这包括一系列技术，如联合文本-视觉预训练、零视觉SFT和联合文本-视觉强化学习。在这个多模态基础上，K2.5引入了Agent Swarm，这是一个自主并行智能体编排框架，能够动态地将复杂任务分解为异构子问题并同时执行。广泛的评估表明，Kimi K2.5在编码、视觉、推理和智能体任务等多个领域实现了最先进的结果。Agent Swarm还将延迟降低了单智能体基线的4.5倍。我们发布了后训练的Kimi K2.5模型检查点，以促进智能体智能的未来研究和实际应用。",
    
    "PaperBanana: Automating Academic Illustration for AI Scientists": 
        "尽管语言模型驱动的自主AI科学家取得了快速进展，但生成可发表的插图仍然是研究工作流程中劳动密集型的瓶颈。为了解决这一负担，我们介绍PaperBanana，这是一个用于自动生成可发表学术插图的智能体框架。PaperBanana由最先进的VLM和图像生成模型驱动，协调专门的智能体来检索参考、规划内容和风格、渲染图像，并通过自我批评进行迭代优化。为了严格评估我们的框架，我们引入了PaperBananaBench，包含从NeurIPS 2025出版物策划的292个方法论图表测试用例，涵盖多样化的研究领域和插图风格。综合实验表明，PaperBanana在忠实度、简洁性、可读性和美学方面始终优于领先的基线。我们进一步展示了我们的方法有效地扩展到生成高质量的统计图表。总体而言，PaperBanana为自动生成可发表插图铺平了道路。",
    
    "Vision-DeepResearch: Incentivizing DeepResearch Capability in Multimodal Large Language Models": 
        "多模态大型语言模型(MLLM)在广泛的视觉任务中取得了显著成功。然而，受其内部世界知识能力的限制，先前的工作提出通过'推理-然后-工具调用'增强MLLM，用于视觉和文本搜索引擎，以在需要大量事实信息的任务上获得实质性收益。然而，这些方法通常在简单设置中定义多模态搜索，假设单个完整级别或实体级别的图像查询和少量文本查询足以检索回答问题所需的关键证据，这在具有大量视觉噪声的真实场景中是不现实的。此外，它们通常在推理深度和搜索广度方面受到限制，使得难以解决需要从多样化视觉和文本来源聚合证据的复杂问题。基于此，我们提出Vision-DeepResearch，提出了一种新的多模态深度研究范式，即执行多轮、多实体和多尺度的视觉和文本搜索，以在重噪声下稳健地命中真实世界的搜索引擎。我们的Vision-DeepResearch支持数十个推理步骤和数百次引擎交互，同时通过冷启动监督和RL训练将深度研究能力内化到MLLM中，从而产生强大的端到端多模态深度研究MLLM。它显著优于现有的多模态深度研究MLLM，以及基于GPT-5、Gemini-2.5-pro和Claude-4-Sonnet等强大闭源基础模型构建的工作流。代码将在https://github.com/Osilly/Vision-DeepResearch发布。",
    
    "FASA: Frequency-aware Sparse Attention": 
        "大型语言模型(LLM)的部署在处理长输入时面临关键瓶颈：键值(KV)缓存的过高内存占用。为解决这一瓶颈，标记修剪范式利用注意力稀疏性选择性地保留一小部分关键标记。然而，现有方法存在不足，静态方法存在不可逆信息丢失的风险，而动态策略采用的启发式方法不足以捕捉标记重要性的查询依赖性。我们提出FASA，这是一个通过动态预测标记重要性实现查询感知标记驱逐的新框架。FASA源于对RoPE的新颖洞察：在频率块(FC)级别发现功能稀疏性。我们的关键发现是，一小部分可识别的"主导"FC始终与完整注意力头表现出高度的上下文一致性。这为识别显著标记提供了强大且计算免费的代理。基于这一洞察，FASA首先使用主导FC识别关键标记集，然后仅在这个修剪的子集上执行聚焦注意力计算。由于只访问KV缓存的一小部分，FASA大大降低了内存带宽需求和计算成本。在从序列建模到复杂CoT推理的一系列长上下文任务中，FASA始终优于所有标记驱逐基线，并实现接近最优的准确性，即使在约束预算下也表现出显著的鲁棒性。值得注意的是，在LongBench-V1上，FASA在仅保留256个标记时达到完整KV性能的近100%，并在AIME24上仅使用18.9%的缓存实现2.56倍加速。",
    
    "Vision-DeepResearch Benchmark: Rethinking Visual and Textual Search for Multimodal Large Language Models": 
        "多模态大型语言模型(MLLM)已经推进了VQA，现在支持使用搜索引擎进行复杂视觉-文本事实查找的Vision-DeepResearch系统。然而，评估这些视觉和文本搜索能力仍然困难，现有基准存在两个主要限制。首先，现有基准不是以视觉搜索为中心的：应该需要视觉搜索的答案通常通过文本问题中的交叉文本线索泄露，或可以从当前MLLM的先验世界知识中推断出来。其次，过度理想化的评估场景：在图像搜索方面，所需信息通常可以通过与完整图像的近似精确匹配获得，而文本搜索方面过于直接且挑战不足。为解决这些问题，我们构建了Vision-DeepResearch基准(VDR-Bench)，包含2000个VQA实例。所有问题都通过精心的多阶段策划管道和严格的专家审查创建，旨在评估Vision-DeepResearch系统在现实世界条件下的行为。此外，为解决当前MLLM视觉检索能力不足的问题，我们提出了一个简单的多轮裁剪搜索工作流。该策略被证明能有效改善真实视觉检索场景中的模型性能。总体而言，我们的结果为未来多模态深度研究系统的设计提供了实用指导。代码将在https://github.com/Osilly/Vision-DeepResearch发布。",
    
    "Golden Goose: A Simple Trick to Synthesize Unlimited RLVR Tasks from Unverifiable Internet Text": 
        "可验证奖励强化学习(RLVR)已成为解锁大型语言模型(LLM)复杂推理的基石。然而，扩展RL受到有限的现有可验证数据的瓶颈，其中改进在长期训练中越来越饱和。为克服这一点，我们提出Golden Goose，这是一个简单的技巧，通过构建填充中间任务的多项选择问答版本，从不可验证的互联网文本合成无限的RLVR任务。给定源文本，我们提示LLM识别和屏蔽关键推理步骤，然后生成一组多样化、合理的干扰项。这使我们能够利用通常被排除在先前RLVR数据构建之外的推理丰富的不可验证语料库(例如科学教科书)来合成GooseReason-0.7M，这是一个拥有超过70万个任务的大规模RLVR数据集，涵盖数学、编程和一般科学领域。经验上，GooseReason有效地恢复了在现有RLVR数据上饱和的模型，在持续RL下产生稳健、持续的收益，并在15个不同基准上为1.5B和4B-Instruct模型实现了新的最先进结果。最后，我们在真实世界环境中部署Golden Goose，从网络安全领域的原始FineWeb抓取中合成RLVR任务，该领域此前不存在RLVR数据。在生成的数据GooseReason-Cyber上训练Qwen3-4B-Instruct在网络安全领域设定了新的最先进水平，超越了具有广泛领域特定预训练和后训练的7B领域专业化模型。这突显了通过利用丰富的推理丰富、不可验证的互联网文本自动扩展RLVR数据的潜力。",
    
    "CodeOCR: On the Effectiveness of Vision Language Models in Code Understanding": 
        "大型语言模型(LLM)在源代码理解方面取得了显著成功，但随着软件系统规模的增长，计算效率已成为关键瓶颈。目前，这些模型依赖于基于文本的范式，将源代码视为标记的线性序列，这导致上下文长度及相关计算成本的线性增长。多模态LLM(MLLM)的快速发展为通过将源代码表示为渲染图像来优化效率提供了机会。与难以在不丢失语义意义的情况下压缩的文本不同，图像模态本质上适合压缩。通过调整分辨率，图像可以缩放到其原始标记成本的一小部分，同时对具有视觉能力的模型仍然可识别。为探索这种方法的可行性，我们对MLLM在代码理解方面的有效性进行了首次系统研究。我们的实验表明：(1)MLLM可以有效理解代码并实现大幅标记减少，达到高达8倍的压缩；(2)MLLM可以有效利用语法高亮等视觉线索，在4倍压缩下改善代码补全性能；(3)克隆检测等代码理解任务对视觉压缩表现出卓越的韧性，某些压缩比甚至略优于原始文本输入。我们的发现突显了MLLM在代码理解方面的潜力和当前局限性，指出了向图像模态代码表示的转变，作为更高效推理的途径。",
    
    "WideSeek-R1: Exploring Width Scaling for Broad Information Seeking via Multi-Agent Reinforcement Learning": 
        "大型语言模型(LLM)的最新进展主要集中在深度缩放上，其中单个智能体通过多轮推理和工具使用解决长期问题。然而，随着任务变得更广泛，关键瓶颈从个人能力转移到组织能力。在这项工作中，我们探索了多智能体系统的宽度缩放的互补维度，以解决广泛的信息寻求。现有的多智能体系统通常依赖于手工制作的工作流和轮流交互，无法有效地并行工作。为弥合这一差距，我们提出WideSeek-R1，这是一个通过多智能体强化学习(MARL)训练的主智能体-子智能体框架，以协同可扩展的编排和并行执行。通过利用具有隔离上下文和专门工具的共享LLM，WideSeek-R1在包含2万个广泛信息寻求任务的策划数据集上联合优化主智能体和并行子智能体。广泛的实验表明，WideSeek-R1-4B在WideSearch基准上实现了40.0%的项目F1分数，与单智能体DeepSeek-R1-671B的性能相当。此外，WideSeek-R1-4B随着并行子智能体数量的增加表现出一致的性能提升，突显了宽度缩放的有效性。"
}

def apply_translations_batch1():
    """应用第1批翻译"""
    print("📝 正在应用第1批翻译 (1-10)...")
    
    # 读取两周的存档
    for week in ['2026-W06', '2026-W07']:
        archive_path = f'/data/workspace/papers-weekly-site/archives/{week}.json'
        
        with open(archive_path, 'r', encoding='utf-8') as f:
            archive = json.load(f)
        
        updated = 0
        for paper in archive['papers']:
            title = paper['title']
            if title in translations_batch1:
                paper['abstract'] = translations_batch1[title]
                updated += 1
        
        # 保存
        with open(archive_path, 'w', encoding='utf-8') as f:
            json.dump(archive, f, ensure_ascii=False, indent=2)
        
        print(f"  ✅ {week}: 更新 {updated} 篇")

if __name__ == '__main__':
    apply_translations_batch1()
    print("✅ 第1批翻译完成！")
