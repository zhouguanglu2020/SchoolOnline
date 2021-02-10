from django.shortcuts import render,HttpResponse

# Create your views here.

def get_index_page(request):
    """
    方法用于
    :param a:
    :param a:
    :retrun :
    """
    return HttpResponse("这里是个api主页")