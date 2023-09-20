import jieba
import re


def remove_punctuation(text):
    """
    使用正则表达式去除标点符号和非中文字符
    :param text: 处理文本
    :return: 返回去除标点符号的文本
    """
    cleaned_text = re.sub(r'[^\u4e00-\u9fa5]+', '', text)
    return cleaned_text


def get_tokens(text):
    """
    对文本语句进行分割
    :param text: 处理文本
    :return: 处理后的文本
    """
    seg_list = list(jieba.cut(text, cut_all=True))
    _seg_list = [remove_punctuation(seg) for seg in seg_list]
    clean_seg_list = [seg for seg in _seg_list if seg != '']
    return clean_seg_list
