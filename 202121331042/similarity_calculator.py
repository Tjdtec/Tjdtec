import numpy as np
import pandas as pd

from collections import Counter
from split_data import get_tokens


def calculate_similarity(orig_text, ori_add_text):
    """
    使用余弦相似度计算两份文本文件的重复率
    :param orig_text: 原文文件
    :param ori_add_text: 抄袭文件
    :return: 余弦相似度
    """
    orig_tokens = get_tokens(orig_text)
    copied_tokens = get_tokens(ori_add_text)

    orig_word_freq = dict(Counter(orig_tokens))
    copied_word_freq = dict(Counter(copied_tokens))
    ori_df = pd.DataFrame(orig_word_freq, index=[0])
    cop_df = pd.DataFrame(copied_word_freq, index=[0])

    # 计算出两份文本文件的词向量
    df = pd.concat([ori_df, cop_df], axis=0)
    df.fillna(0, inplace=True)
    file_array = df.values
    ori_vector = file_array[0]
    cop_vector = file_array[1]

    # 计算余弦相似度
    cos_similarity = np.dot(ori_vector, cop_vector) / (np.linalg.norm(ori_vector) * np.linalg.norm(cop_vector))
    print(f'文章相似度: {cos_similarity}')

    return cos_similarity
