from django.http import HttpResponse
from datetime import datetime


def hello_world(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"姓名：刘振兴  学号：20231201047  班级：23医信<br>当前时间：{current_time}")