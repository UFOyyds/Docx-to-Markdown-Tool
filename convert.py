"""
Copyright (c) 2024 Docx to Markdown Tool
Copyright (c) 2024 [新开发者的名字/组织名]

This file is part of the Docx to Markdown Tool project, 
and is released under the MIT License.
"""

# 导入所需的Python标准库和第三方库
import os  # 导入操作系统模块，用于文件和路径操作
from flask import Flask, request, send_file, render_template  # 导入Flask Web框架相关组件
from docx import Document  # 导入python-docx库，用于处理Word文档
import markdown  # 导入markdown库，用于处理Markdown格式

# 创建Flask应用实例
app = Flask(__name__)

# 添加主页路由
@app.route('/')
def index():
    return render_template('index.html')

def docx_to_markdown(docx_file):
    """
    将Word文档转换为Markdown格式
    
    参数:
        docx_file: 上传的Word文档文件对象
    返回:
        str: 转换后的Markdown文本内容
    """
    # 使用python-docx打开Word文档
    doc = Document(docx_file)
    # 创建列表用于存储转换后的Markdown内容
    markdown_content = []

    # 遍历文档中的每个段落
    for para in doc.paragraphs:
        if para.style.name.startswith('Heading'):  # 检查段落是否是标题样式
            # 获取标题级别（例如：Heading 1 -> 1级标题）
            level = int(para.style.name.split(' ')[-1])
            # 将Word标题转换为Markdown标题格式（例如：# 一级标题）
            markdown_content.append('#' * level + ' ' + para.text)
        elif para.text.strip() == '':  # 处理空行
            markdown_content.append('')
        else:  # 处理普通段落
            markdown_content.append(para.text)

    # 使用换行符连接所有内容，返回完整的Markdown文本
    return "\n".join(markdown_content)

# 定义Web API路由，处理文件上传和转换请求
@app.route('/convert', methods=['POST'])
def convert():
    # 检查请求中是否包含文件
    if 'file' not in request.files:
        return 'No file part', 400  # 返回错误信息和400状态码

    # 获取上传的文件
    file = request.files['file']
    # 检查是否选择了文件
    if file.filename == '':
        return 'No selected file', 400

    # 检查文件是否是Word文档（.docx格式）
    if file and file.filename.endswith('.docx'):
        try:
            # 调用转换函数，将Word文档转换为Markdown
            markdown_content = docx_to_markdown(file)

            # 将转换结果保存到临时文件
            output_file = 'output.md'
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)

            # 将转换后的文件发送给用户下载
            return send_file(output_file, 
                            as_attachment=True,  # 作为附件下载
                            download_name='converted.md')  # 设置下载文件名
        except Exception as e:
            return str(e), 500  # 返回错误信息和500状态码

    # 如果文件格式不正确，返回错误信息
    return 'Invalid file format', 400

# 程序入口点
if __name__ == '__main__':
    # 确保templates目录存在
    os.makedirs('templates', exist_ok=True)
    # 启动Flask应用，开启调试模式
    app.run(debug=True)