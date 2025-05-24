USE aizhs

CREATE TABLE articles (
                          id INT AUTO_INCREMENT PRIMARY KEY,  -- 自增主键，用于唯一标识每条记录
                          category VARCHAR(255) NOT NULL,     -- 文章分类，如 "科技"、"体育" 等
                          title VARCHAR(255) NOT NULL,        -- 文章标题
                          content TEXT NOT NULL,              -- 文章内容，使用 TEXT 类型以支持较长文本
                          published_date DATE NOT NULL        -- 发布日期，格式为 YYYY-MM-DD
);