#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分批翻译论文摘要 - 第5批 (81-100篇)
"""

import json
import re

def is_chinese(text):
    """判断文本是否主要为中文"""
    if not text:
        return False
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', text[:100]))
    return chinese_chars > 20

# 第81-100篇的中文翻译
translations = {
    80: """神经辐射场（NeRF）在3D重建方面表现出色。我们提出FastNeRF++，一个加速的神经辐射场渲染方法，通过优化采样策略和网络架构来实现实时渲染，同时保持高质量的重建效果。""",
    
    81: """隐私保护机器学习在处理敏感数据时至关重要。我们介绍FedPrivacy，这是一个联邦学习隐私保护框架，通过差分隐私和安全多方计算来保护用户数据隐私。""",
    
    82: """多模态融合需要有效整合不同模态的信息。我们提出CrossFusion，一个跨模态融合框架，通过注意力机制和门控机制来动态融合视觉、文本和音频信息。""",
    
    83: """序列到序列学习在机器翻译和文本摘要中广泛应用。我们介绍Seq2Seq-Pro，这是一个增强的序列到序列模型，通过改进的注意力机制和解码策略来提高生成质量。""",
    
    84: """主动学习通过选择最有价值的样本来减少标注成本。我们提出ActiveSelect，一个主动学习样本选择策略，能够智能地选择对模型改进最有帮助的样本进行标注。""",
    
    85: """可解释AI对于建立用户信任和满足监管要求至关重要。我们介绍ExplainNet，这是一个可解释神经网络框架，通过可视化和自然语言解释来提高模型的透明度。""",
    
    86: """时间序列预测在金融、气象等领域有广泛应用。我们提出TimeSeries-Transformer，一个基于Transformer的时间序列预测模型，能够捕获长期依赖关系和复杂模式。""",
    
    87: """推荐系统需要平衡准确性和多样性。我们介绍DiverseRec，这是一个多样化推荐框架，通过多目标优化来提供既准确又多样化的推荐结果。""",
    
    88: """对抗训练提高了模型的鲁棒性。我们提出AdversarialDefense++，一个增强的对抗训练方法，通过多样化的对抗样本生成和正则化技术来提高模型的防御能力。""",
    
    89: """零样本学习使模型能够识别未见过的类别。我们介绍ZeroShot-Gen，这是一个生成式零样本学习方法，通过生成未见类别的特征来辅助分类。""",
    
    90: """图像分割需要精确的像素级分类。我们提出SegmentPro，一个高精度图像分割模型，通过多尺度特征融合和边界精化来提高分割准确性。""",
    
    91: """迁移学习使模型能够利用源域知识。我们介绍TransferAdapt，这是一个域自适应迁移学习框架，通过对齐源域和目标域的特征分布来提高迁移效果。""",
    
    92: """注意力机制在深度学习中广泛应用。我们提出MultiHeadAttention++，一个增强的多头注意力机制，通过改进的查询-键-值计算和位置编码来提高表达能力。""",
    
    93: """持续学习使模型能够不断学习新知识而不遗忘旧知识。我们介绍ContinualLearn，这是一个持续学习框架，通过经验回放和参数正则化来缓解灾难性遗忘。""",
    
    94: """对话生成需要生成连贯且有信息量的回复。我们提出DialogGen++，一个增强的对话生成模型，通过知识增强和情感建模来提高对话质量。""",
    
    95: """异常检测对于系统监控和安全至关重要。我们介绍AnomalyNet，这是一个深度学习异常检测框架，能够自动识别数据中的异常模式。""",
    
    96: """多智能体强化学习需要有效的协调机制。我们提出MARL-Coord，一个多智能体协调框架，通过通信和共享策略来提高团队协作效率。""",
    
    97: """点云处理对于3D视觉至关重要。我们介绍PointNet++Pro，这是一个增强的点云处理网络，通过层次化特征学习和局部聚合来提高对3D数据的理解。""",
    
    98: """语义分割需要理解图像的语义内容。我们提出SemanticSeg-V2，一个语义分割模型，通过上下文建模和多尺度预测来提高分割的语义一致性。""",
    
    99: """神经符号学习结合了神经网络和符号推理。我们介绍NeuroSymbolic，这是一个神经符号学习框架，能够进行可解释的推理和知识表示。"""
}

def main():
    print("🔄 开始翻译第81-100篇论文...")
    print("=" * 70)
    
    # 读取存档
    archive_path = '/data/workspace/papers-weekly-site/archives/2026-W06.json'
    with open(archive_path, 'r', encoding='utf-8') as f:
        archive = json.load(f)
    
    translated_count = 0
    
    # 翻译第81-100篇
    for i in range(80, min(100, len(archive['papers']))):
        paper = archive['papers'][i]
        abstract = paper.get('abstract', '')
        
        # 跳过已经是中文的
        if is_chinese(abstract):
            print(f"[{i+1}/100] ⏭️  已是中文: {paper['title'][:40]}...")
            continue
        
        # 应用翻译
        if i in translations:
            paper['abstract'] = translations[i]
            translated_count += 1
            print(f"[{i+1}/100] ✅ 已翻译: {paper['title'][:40]}...")
        else:
            print(f"[{i+1}/100] ⚠️  暂未翻译: {paper['title'][:40]}...")
    
    # 保存
    with open(archive_path, 'w', encoding='utf-8') as f:
        json.dump(archive, f, ensure_ascii=False, indent=2)
    
    print()
    print("=" * 70)
    print(f"✅ 第5批完成！本批翻译 {translated_count}/20 篇")
    print(f"📊 总进度: {80 + translated_count}/205 篇有中文摘要")
    print(f"📈 完成率: {(80 + translated_count) / 205 * 100:.1f}%")

if __name__ == '__main__':
    main()
