import re
def get_local_file_text(filename="gather.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(f"读取到{file.read()}")
            return file.read()
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return None

def remove_characters(text, chars_list):
    # 将列表转化为正则表达式的字符串形式
    chars_to_remove = ''.join(re.escape(char) for char in chars_list)
    # 创建一个正则表达式模式，用于匹配需要删除的字符
    pattern = f"[{chars_to_remove}]"
    # 使用re.sub来替换匹配到的字符
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text

def main():
    predefined_chars_to_remove = [".", ",", "!", "?", ";", ":", "-", "'", '"']  # 预定义需要删除的字符列表
    user_input = input()
    result = remove_characters(user_input, predefined_chars_to_remove)
    print("处理后的文本:", result)

if __name__ == "__main__":
    main()