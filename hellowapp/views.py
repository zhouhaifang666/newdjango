from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
import os


def hello_world(request):
    # 方法1：直接返回HTML内容
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 读取HTML文件内容
    html_file_path = os.path.join(os.path.dirname(__file__), 'index.html')
    
    try:
        with open(html_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # 不替换时间占位符，让JavaScript处理动态更新
        return HttpResponse(html_content)
    except FileNotFoundError:
        # 如果HTML文件不存在，返回默认信息
        return HttpResponse(f"姓名：刘振兴  学号：20231201047  班级：23医信<br>当前时间：{current_time}")