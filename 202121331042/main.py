import sys
from file_process import read_file
from similarity_calculator import calculate_similarity
from split_data import get_tokens


def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <original_file> <copied_file> <output_file>")
        sys.exit(1)

    original_file_path = sys.argv[1]
    copied_file_path = sys.argv[2]
    output_file_path = sys.argv[3]
    try:
        orig_text = read_file(original_file_path)
        copied_text = read_file(copied_file_path)

        similarity = calculate_similarity(orig_text, copied_text)

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(f"{similarity:.2f}")
            print(f"重复率为: {similarity:.2f}")

    except FileNotFoundError:
        print("文件不存在或路径错误")
        sys.exit(1)
    except Exception as e:
        print(f"发生错误: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
