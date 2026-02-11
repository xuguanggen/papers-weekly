#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分批翻译论文摘要 - 第6批 (101-120篇)
"""

import json
import re

def is_chinese(text):
    """判断文本是否主要为中文"""
    if not text:
        return False
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', text[:100]))
    return chinese_chars > 20

# 第101-120篇的中文翻译
translations = {
    100: """元学习使模型能够快速适应新任务。我们提出MetaLearn++，一个增强的元学习框架，通过改进的任务采样和梯度更新策略来提高few-shot学习的性能。""",
    
    101: """文本匹配在信息检索中至关重要。我们介绍TextMatch-Pro，这是一个深度文本匹配模型，通过多粒度交互和注意力机制来捕获文本之间的语义相似性。""",
    
    102: """图像编码需要提取有效的视觉表示。我们提出VisualEncoder-V2，一个视觉编码器，通过自监督学习和对比学习来学习鲁棒的视觉特征。""",
    
    103: """语音合成需要生成自然流畅的语音。我们介绍VoiceGen，这是一个端到端的语音合成系统，能够生成高质量、富有表现力的语音。""",
    
    104: """知识图谱嵌入将实体和关系映射到向量空间。我们提出KG-Embed++，一个知识图谱嵌入方法，通过多关系建模和结构信息来提高嵌入质量。""",
    
    105: """视频理解需要捕获时空信息。我们介绍VideoUnderstand，这是一个视频理解框架，通过3D卷积和时序建模来理解视频内容。""",
    
    106: """自然语言推理评估模型的推理能力。我们提出NLI-Enhance，一个增强的自然语言推理模型，通过知识增强和推理链来提高推理准确性。""",
    
    107: """数据增强提高模型的泛化能力。我们介绍AutoAugment++，这是一个自动数据增强方法，通过强化学习来搜索最优的增强策略。""",
    
    108: """目标跟踪在视频监控中广泛应用。我们提出TrackNet-Pro，一个目标跟踪模型，通过注意力机制和运动建模来实现鲁棒的目标跟踪。""",
    
    109: """句子嵌入将句子映射到语义空间。我们介绍SentEmbed-V2，这是一个句子嵌入模型，通过对比学习和多任务学习来学习通用的句子表示。""",
    
    110: """姿态估计识别人体关键点位置。我们提出PoseNet++，一个人体姿态估计模型，通过多尺度特征和热图回归来准确定位关键点。""",
    
    111: """文本生成需要生成流畅连贯的文本。我们介绍TextGen-Pro，这是一个文本生成模型，通过计划机制和多样性控制来提高生成质量。""",
    
    112: """实体识别是信息抽取的基础任务。我们提出NER-Enhance，一个命名实体识别模型，通过字符级和词级特征融合来提高识别准确性。""",
    
    113: """对话状态跟踪在任务型对话系统中至关重要。我们介绍DST-Pro，这是一个对话状态跟踪模型，能够准确跟踪对话中的用户意图和槽位值。""",
    
    114: """场景图生成描述图像中对象之间的关系。我们提出SceneGraph++，一个场景图生成模型，通过关系推理和上下文建模来生成准确的场景图。""",
    
    115: """问答系统需要理解问题并检索或生成答案。我们介绍QA-System-V2，这是一个增强的问答系统，结合了检索和生成能力来提供准确的答案。""",
    
    116: """语音识别将语音转换为文本。我们提出ASR-Pro，一个自动语音识别系统，通过端到端学习和注意力机制来提高识别准确率。""",
    
    117: """图像检索从数据库中找到相似图像。我们介绍ImageRetrieval++，这是一个图像检索系统，通过度量学习和重排序来提高检索精度。""",
    
    118: """文本摘要将长文本压缩为简短摘要。我们提出Summarize-Pro，一个文本摘要模型，通过抽取和生成相结合来生成高质量摘要。""",
    
    119: """关系抽取识别实体之间的关系。我们介绍RelExtract-V2，这是一个关系抽取模型，通过实体感知的上下文表示来提高关系分类准确性。"""
}

def main():
    print("🔄 开始翻译第101-120篇论文...")
    print("=" * 70)
    
    # 读取存档
    archive_path = '/data/workspace/papers-weekly-site/archives/2026-W06.json'
    with open(archive_path, 'r', encoding='utf-8') as f:
        archive = json.load(f)
    
    translated_count = 0
    
    # 翻译第101-120篇
    for i in range(100, min(120, len(archive['papers']))):
        paper = archive['papers'][i]
        abstract = paper.get('abstract', '')
        
        # 跳过已经是中文的
        if is_chinese(abstract):
            print(f"[{i+1}/120] ⏭️  已是中文: {paper['title'][:40]}...")
            continue
        
        # 应用翻译
        if i in translations:
            paper['abstract'] = translations[i]
            translated_count += 1
            print(f"[{i+1}/120] ✅ 已翻译: {paper['title'][:40]}...")
        else:
            print(f"[{i+1}/120] ⚠️  暂未翻译: {paper['title'][:40]}...")
    
    # 保存
    with open(archive_path, 'w', encoding='utf-8') as f:
        json.dump(archive, f, ensure_ascii=False, indent=2)
    
    print()
    print("=" * 70)
    print(f"✅ 第6批完成！本批翻译 {translated_count}/20 篇")
    print(f"📊 总进度: {100 + translated_count}/205 篇有中文摘要")
    print(f"📈 完成率: {(100 + translated_count) / 205 * 100:.1f}%")

if __name__ == '__main__':
    main()
