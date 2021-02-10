from django.shortcuts import render

# Create your views here.

def page_not_found(request,exception):
    return render(request, 'error404.html',status=404)

def page_permission_denied(request,exception):
    return render(request, 'error403.html',status=403)

def page_inter_error(request):
    return render(request, 'error500.html',status=500)

def get_index_page(request):
    return render(request, 'index.html',status=200)