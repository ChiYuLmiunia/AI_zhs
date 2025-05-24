import requests


def fetch_url_content(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 确保响应状态码为200
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def storage_to_file(content, filename="gather.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"内容已成功保存到 {filename}")
        print(content)
    except Exception as e:
        print(f"保存文件时出错: {e}")


def scrape_and_combine(urls):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    combined_content = ""

    for url in urls:
        content = fetch_url_content(url, headers)
        if content:
            combined_content += content + "\n"  # 每个页面内容后加换行符

    return combined_content


# 发送请求，后续可以根据实际情况增加。——ChiYu 2025 05 22
if __name__ == "__main__":
    urls = [
        "https://ai-bot.cn/daily-ai-news/",
        "https://maomu.com/news"
    ]
    result = scrape_and_combine(urls)
    storage_to_file(result)