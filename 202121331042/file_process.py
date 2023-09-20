def read_file(path):
    """

    :param path: 文件路径
    :return: 返回打开的文件类
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError('文件不存在， 请检查路径是否正确')

