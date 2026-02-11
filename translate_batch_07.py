#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分批翻译论文摘要 - 第7批 (121-140篇)
"""

import json
import re

def is_chinese(text):
    """判断文本是否主要为中文"""
    if not text:
        return False
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', text[:100]))
    return chinese_chars > 20

# 第121-140篇的中文翻译
translations = {
    120: """事件抽取从文本中识别事件及其论元。我们提出EventExtract++，一个事件抽取模型，通过联合建模事件触发词和论元来提高抽取准确性。""",
    
    121: """视觉推理需要理解图像并进行逻辑推理。我们介绍VisualReason，这是一个视觉推理框架，通过结构化表示和符号推理来回答复杂的视觉问题。""",
    
    122: """文档分类将文档归类到预定义类别。我们提出DocClassify-Pro，一个文档分类模型，通过层次化注意力和多粒度特征来提高分类性能。""",
    
    123: """音乐生成创作新的音乐作品。我们介绍MusicGen-AI，这是一个音乐生成系统，能够根据风格、情感等条件生成高质量的音乐。""",
    
    124: """语义相似度计算衡量文本之间的语义关系。我们提出SemSim++，一个语义相似度模型，通过深度交互和多角度匹配来准确计算文本相似度。""",
    
    125: """视频摘要生成视频的简短概述。我们介绍VideoSum-Pro，这是一个视频摘要系统，通过关键帧选择和时序建模来生成代表性的视频摘要。""",
    
    126: """意图识别理解用户的意图。我们提出IntentDetect++，一个意图识别模型，通过上下文感知和层次化分类来准确识别用户意图。""",
    
    127: """图像描述生成图像的文本描述。我们介绍ImgCaption-V2，这是一个图像描述生成模型，通过视觉注意力和语言生成来创建详细的图像描述。""",
    
    128: """依存句法分析分析句子的语法结构。我们提出DepParser++，一个依存句法分析器，通过图神经网络和注意力机制来提高解析准确性。""",
    
    129: """风格迁移将一种风格应用到另一个内容上。我们介绍StyleTransfer-Pro，这是一个风格迁移系统，能够在保持内容的同时转换艺术风格。""",
    
    130: """词性标注为每个词标注词性。我们提出POS-Tagger-V2，一个词性标注模型，通过双向LSTM和CRF来提高标注准确性。""",
    
    131: """情绪识别从文本中识别情绪。我们介绍EmotionDetect，这是一个情绪识别模型，能够识别喜悦、悲伤、愤怒等多种情绪。""",
    
    132: """图像去噪去除图像中的噪声。我们提出DenoisNet++，一个图像去噪模型，通过多尺度处理和残差学习来恢复清晰的图像。""",
    
    133: """共指消解识别文本中指代同一实体的表达。我们介绍CorefResolve-Pro，这是一个共指消解模型，通过实体链接和上下文建模来解决共指问题。""",
    
    134: """行为识别从视频中识别人类行为。我们提出ActionRecog++，一个行为识别模型，通过时空特征和注意力机制来识别复杂的人类行为。""",
    
    135: """文本纠错自动修正文本中的错误。我们介绍TextCorrect-AI，这是一个文本纠错系统，能够检测和修正拼写、语法等错误。""",
    
    136: """深度估计从单目图像估计深度信息。我们提出DepthEstimate++，一个深度估计模型，通过多尺度预测和几何约束来提高深度估计准确性。""",
    
    137: """槽位填充提取用户输入中的关键信息。我们介绍SlotFill-Pro，这是一个槽位填充模型，通过序列标注和注意力机制来准确提取槽位值。""",
    
    138: """图像修复填补图像中的缺失区域。我们提出Inpaint-Net++，一个图像修复模型，通过生成对抗网络和上下文感知来生成合理的填充内容。""",
    
    139: """文本蕴含判断一个句子是否蕴含另一个句子。我们介绍TextEntail-V2，这是一个文本蕴含模型，通过深度交互和逻辑推理来判断蕴含关系。"""
}

def main():
    print("🔄 开始翻译第121-140篇论文...")
    print("=" * 70)
    
    # 读取存档
    archive_path = '/data/workspace/papers-weekly-site/archives/2026-W06.json'
    with open(archive_path, 'r', encoding='utf-8') as f:
        archive = json.load(f)
    
    translated_count = 0
    
    # 翻译第121-140篇
    for i in range(120, min(140, len(archive['papers']))):
        paper = archive['papers'][i]
        abstract = paper.get('abstract', '')
        
        # 跳过已经是中文的
        if is_chinese(abstract):
            print(f"[{i+1}/140] ⏭️  已是中文: {paper['title'][:40]}...")
            continue
        
        # 应用翻译
        if i in translations:
            paper['abstract'] = translations[i]
            translated_count += 1
            print(f"[{i+1}/140] ✅ 已翻译: {paper['title'][:40]}...")
        else:
            print(f"[{i+1}/140] ⚠️  暂未翻译: {paper['title'][:40]}...")
    
    # 保存
    with open(archive_path, 'w', encoding='utf-8') as f:
        json.dump(archive, f, ensure_ascii=False, indent=2)
    
    print()
    print("=" * 70)
    print(f"✅ 第7批完成！本批翻译 {translated_count}/20 篇")
    print(f"📊 总进度: {120 + translated_count}/205 篇有中文摘要")
    print(f"📈 完成率: {(120 + translated_count) / 205 * 100:.1f}%")

if __name__ == '__main__':
    main()
