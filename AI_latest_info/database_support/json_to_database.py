import os
import json
import mysql.connector


def read_json(file_path):
    """读取JSON文件并返回字典结构"""
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
        return {}

    try:
        with open(file_path, 'r', encoding='utf-8') as f:  # 指定编码为 utf-8
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"JSON 解码错误: {e}")
        return {}
    except UnicodeDecodeError as e:
        print(f"文件编码错误: {e}")
        return {}
    except Exception as e:
        print(f"读取文件时发生未知错误: {e}")
        return {}


def mySQL_Support(transet_sql):
    """Connect to a local MySQL database and execute the provided SQL statement."""
    try:
        # Establish connection to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="io",  # Replace with your MySQL username
            password="123456789",  # Replace with your MySQL password
            database="aizhs"  # Replace with your database name
        )
        cursor = connection.cursor()
        cursor.execute(transet_sql)
        connection.commit()
        print(f"SQL executed successfully: {transet_sql}")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()


def sync_json(content):
    """解析JSON内容并为每个文章条目生成Transet_SQL插入语句"""
    if not content or "news_categories" not in content:
        print("无效的JSON内容或缺少'news_categories'字段")
        return

    sql_template = "INSERT INTO articles (category, title, content, published_date) VALUES ('{category}', '{title}', '{content}', '{published_date}');"

    for category_data in content["news_categories"]:
        category = category_data.get("category", "未知分类")
        for article in category_data.get("articles", []):
            title = article.get("title", "").replace("'", "''")  # Escape single quotes
            article_content = article.get("content", "").replace("'", "''")
            published_date = article.get("published_date", "1970-01-01")
            transet_sql = sql_template.format(
                category=category,
                title=title,
                content=article_content,
                published_date=published_date
            )
            mySQL_Support(transet_sql)


def main():
    local_content = read_json("./sample.json")
    print(local_content)
    sync_json(local_content)

if __name__ == '__main__':
    main()