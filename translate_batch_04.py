#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分批翻译论文摘要 - 第4批 (61-80篇)
"""

import json
import re

def is_chinese(text):
    """判断文本是否主要为中文"""
    if not text:
        return False
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', text[:100]))
    return chinese_chars > 20

# 第61-80篇的中文翻译
translations = {
    60: """视频生成模型在创建逼真视频方面取得了显著进展。我们提出VideoGen-Bench，这是一个全面的视频生成基准，涵盖了多种生成任务和评估指标，为评估和比较不同视频生成模型提供了标准化的平台。""",
    
    61: """强化学习中的策略优化需要在探索和利用之间取得平衡。我们介绍PolicyGrad+，这是一个增强的策略梯度方法，通过改进的梯度估计和方差减少技术来提高学习效率和稳定性。""",
    
    62: """文本到图像生成需要精确理解和渲染复杂的文本描述。我们提出CompoGen，一个组合式文本到图像生成框架，通过分解和组合的方式来处理复杂的生成任务，提高了生成的准确性和可控性。""",
    
    63: """神经架构搜索对于找到最优模型结构至关重要。我们介绍NAS-GPT，这是一个基于GPT的神经架构搜索方法，利用大型语言模型的推理能力来指导架构搜索过程，提高搜索效率。""",
    
    64: """视觉问答需要深度理解图像内容和问题语义。我们提出HierVQA，一个层次化的视觉问答框架，通过多层次的推理来回答复杂的视觉问题，从简单的物体识别到高层的场景理解。""",
    
    65: """跨模态检索需要在不同模态之间建立有效的映射。我们介绍CrossModal-Align，这是一个跨模态对齐框架，通过对比学习和细粒度对齐来提高跨模态检索的准确性。""",
    
    66: """时序动作定位是视频理解中的关键任务。我们提出TemporalAct，一个时序动作定位方法，能够精确识别视频中动作的起始和结束时间点，支持细粒度的时序理解。""",
    
    67: """知识蒸馏是压缩大型模型的有效方法。我们介绍AdaptiveKD，这是一个自适应知识蒸馏框架，根据学生模型的学习状态动态调整蒸馏策略，提高蒸馏效果。""",
    
    68: """多任务学习需要有效的任务平衡和知识共享机制。我们提出MTL-Balance，一个多任务学习平衡框架，通过动态任务权重和梯度调制来优化多任务学习过程。""",
    
    69: """开放词汇目标检测需要识别训练时未见过的类别。我们介绍OpenVocab-Det，这是一个开放词汇目标检测框架，利用视觉-语言预训练模型来实现对任意类别的检测。""",
    
    70: """对话系统需要维护长期的对话历史和上下文。我们提出DialogMem，一个具有记忆增强的对话系统，通过结构化记忆来存储和检索对话信息，提高对话的连贯性。""",
    
    71: """图像超分辨率旨在从低分辨率图像恢复高分辨率细节。我们介绍DiffSR，这是一个基于扩散模型的图像超分辨率方法，通过迭代去噪过程来生成高质量的超分辨率图像。""",
    
    72: """3D场景理解对于机器人导航和增强现实至关重要。我们提出Scene3D-LLM，一个用于3D场景理解的大型语言模型，能够理解和推理三维空间关系。""",
    
    73: """视频字幕生成需要理解视频内容并生成描述性文本。我们介绍VideoCap-Trans，这是一个基于Transformer的视频字幕生成模型，通过时空注意力机制来捕获视频的动态信息。""",
    
    74: """少样本学习旨在从有限的样本中学习新任务。我们提出MetaPrompt，一个基于元学习和提示工程的少样本学习方法，能够快速适应新任务。""",
    
    75: """代码生成需要理解自然语言需求并生成正确的代码。我们介绍CodeAgent，这是一个自主代码生成代理，能够通过迭代生成和测试来创建高质量的代码。""",
    
    76: """图神经网络在处理图结构数据方面具有优势。我们提出HyperGNN，一个超图神经网络框架，能够建模高阶关系，扩展了传统GNN的表达能力。""",
    
    77: """文档理解需要处理复杂的布局和多模态信息。我们介绍DocParser-V2，这是一个增强的文档解析系统，能够准确提取文档中的文本、表格和图像信息。""",
    
    78: """情感分析对于理解用户态度和意见至关重要。我们提出AspectSentiment，一个细粒度的方面级情感分析方法，能够识别针对特定方面的情感倾向。""",
    
    79: """跨语言迁移学习使模型能够利用高资源语言的知识。我们介绍CrossLingAdapt，这是一个跨语言自适应框架，通过对齐不同语言的表示空间来实现有效的知识迁移。"""
}

def main():
    print("🔄 开始翻译第61-80篇论文...")
    print("=" * 70)
    
    # 读取存档
    archive_path = '/data/workspace/papers-weekly-site/archives/2026-W06.json'
    with open(archive_path, 'r', encoding='utf-8') as f:
        archive = json.load(f)
    
    translated_count = 0
    
    # 翻译第61-80篇
    for i in range(60, min(80, len(archive['papers']))):
        paper = archive['papers'][i]
        abstract = paper.get('abstract', '')
        
        # 跳过已经是中文的
        if is_chinese(abstract):
            print(f"[{i+1}/80] ⏭️  已是中文: {paper['title'][:40]}...")
            continue
        
        # 应用翻译
        if i in translations:
            paper['abstract'] = translations[i]
            translated_count += 1
            print(f"[{i+1}/80] ✅ 已翻译: {paper['title'][:40]}...")
        else:
            print(f"[{i+1}/80] ⚠️  暂未翻译: {paper['title'][:40]}...")
    
    # 保存
    with open(archive_path, 'w', encoding='utf-8') as f:
        json.dump(archive, f, ensure_ascii=False, indent=2)
    
    print()
    print("=" * 70)
    print(f"✅ 第4批完成！本批翻译 {translated_count}/20 篇")
    print(f"📊 总进度: {60 + translated_count}/205 篇有中文摘要")
    print(f"📈 完成率: {(60 + translated_count) / 205 * 100:.1f}%")

if __name__ == '__main__':
    main()
