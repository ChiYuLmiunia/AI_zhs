import json

def read_json(file_path):
    """读取JSON文件并返回字典结构"""
    if not os.path.exists(file_path):
        return {}

    with open(file_path, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def main():
    pass

if __name__ == '__main__':
    main()