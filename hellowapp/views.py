from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("姓名：刘振兴  学号：20231201047  班级：23医信")