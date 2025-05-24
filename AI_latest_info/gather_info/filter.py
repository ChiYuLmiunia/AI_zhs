import re

def get_local_file_text(filename="gather.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print(f"读取到的内容: {content}")
            return content
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return None

def remove_html_css(text):
    # 删除HTML标签
    text = re.sub(r'<[^>]+>', '', text)
    # 删除内联CSS样式
    text = re.sub(r'\s*style\s*=\s*"[^"]*"', '', text)
    # 删除类名和ID
    text = re.sub(r'\s*(class|id)\s*=\s*"[^"]*"', '', text)
    # 删除多余的空格和换行符
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def storage_to_file(content, filename="after_filter_gather.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"内容已成功保存到 {filename}")
        print(content)
    except Exception as e:
        print(f"保存文件时出错: {e}")

def main():
    user_input = get_local_file_text(filename="gather.txt")
    if user_input is not None:
        result = remove_html_css(user_input)
        print("处理后的文本:", result)
        storage_to_file(result, "after_filter_gather.txt")
    else:
        print("未读取到有效的user_input")

if __name__ == "__main__":
    main()