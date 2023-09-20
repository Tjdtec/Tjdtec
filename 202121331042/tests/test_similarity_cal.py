import unittest
import pytest

from similarity_calculator import calculate_similarity


@pytest.mark.test
def test_calculate_similarity():
    # 定义一些测试用例
    case1 = ("今天是星期天，天气晴，今天晚上我要去看电影。",
             "今天是周天，天气晴朗，我晚上要去看电影。")

    # 针对每个测试用例进行测试
    similarity1 = calculate_similarity(case1[0], case1[1])
    assert 0.7 <= similarity1 <= 1
