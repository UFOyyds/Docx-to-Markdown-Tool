# Word 文档转 Markdown 工具

这是一个基于 Web 界面的工具，用于将 Word 文档（.docx）转换为 Markdown 格式（.md）。

## 环境要求

- Python 3.x
- Flask
- python-docx
- markdown

## 项目结构

```
项目根目录/
├── convert.py          # Flask 应用主程序
├── requirements.txt    # Python 依赖包列表
├── templates/         # HTML 模板目录
│   └── index.html    # Web 界面模板
└── docs/             # 文档目录
    ├── input/        # 上传文件临时存储
    └── output/       # 转换结果临时存储
```

## 安装

1. 创建并激活虚拟环境（可选但推荐）：
```bash
python -m venv format_conversion_env
source format_conversion_env/bin/activate  # Linux/Mac
# 或
format_conversion_env\Scripts\activate  # Windows
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 使用方法

1. 启动 Web 服务：
```bash
python convert.py
```

2. 在浏览器中访问：
```
http://localhost:5000
```

3. 通过 Web 界面使用：
   - 点击"选择文件"按钮选择 Word 文档（.docx 格式）
   - 点击"Upload and Convert"按钮
   - 转换完成后文件会自动下载

## 功能特点

- 简洁的 Web 界面
- 支持文件拖放上传
- 自动文件格式验证
- 即时文件转换
- 自动文件下载
- 支持标题格式转换
- 自动清理临时文件

## 注意事项

- 仅支持 .docx 格式的 Word 文档
- 目前支持基本的文本和标题转换
- 转换后的文件会自动下载
- 所有上传和转换的文件都是临时的，会定期清理
- 更多功能正在开发中...

## 许可证

本项目采用 MIT 许可证。这意味着您可以：

- ✅ 自由使用
- ✅ 自由修改
- ✅ 自由分发
- ✅ 商业使用
- ✅ 私人使用

使用本项目代码时，需要：

1. 保留原始许可证：
   - 在您的项目中包含完整的 LICENSE 文件
   - 或在您的许可证中包含原始 MIT 许可证文本

2. 保留版权声明：
   - 在使用或修改的源代码文件中添加版权声明
   - 可以添加您自己的版权声明，但必须保留原始版权信息

示例版权声明：
```python
"""
Copyright (c) 2024 Docx to Markdown Tool
Copyright (c) 2024 [您的名字/组织名]

This file is part of the Docx to Markdown Tool project, 
and is released under the MIT License.
"""
```

详细信息请参见 [LICENSE](LICENSE) 文件。 