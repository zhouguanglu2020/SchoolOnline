import urllib.parse, requests,json
from django.shortcuts import render, redirect, HttpResponse


# Create your views here.

##主页
main_page = r"http://jingsijiaoyu.top/"       #更换公众号需要修改

#  微信授权url
#scope=snsapi_userinfo   弹出授权页面，可以通过`openid`获取到昵称，头像，用户信息，不需要关注就能获取用户信息
#scope=snsapi_base   不弹出页面，直接跳转，只能获取openid
url="https://open.weixin.qq.com/connect/oauth2/authorize?appid={0}&redirect_uri={1}&response_type=code&scope=snsapi_userinfo&state=openid_required#wechat_redirect"
app_id = 'wxe167e77a73dff8a7'      #更换公众号需要修改
AppSecret = '054b8df9ee37cfe2cce3d2a13c7f297f'   #更换公众号需要修改



def page_not_found(request,exception):
    # return redirect("/")
    return render(request, 'error404.html',status=404)

def page_permission_denied(request,exception):
    return render(request, 'error403.html',status=403)

def page_inter_error(request):
    return render(request, 'error500.html',status=500)

def get_index_page(request):
    return render(request, 'index.html',status=200)

def get_teacher(request):
    return render(request,'web/teacher.html')

def get_student(request):
    return HttpResponse("找学生页面")

def teacherRegister(request):
    return render(request,'web/teacherregister.html')

def studentRegister(request):
    return HttpResponse("学生注册页面")

def get_course(request):
    return HttpResponse("课程页面")

def r_oauth(request):
    # 授权

    url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid={0}&redirect_uri={1}&response_type=code&scope=snsapi_userifo&state=openid_required#wechat_redirect"
    redirect_uri = main_page

    redirect_uri = urllib.parse.quote(redirect_uri)

    print(url.format(app_id, redirect_uri))
    return redirect(url.format(app_id, redirect_uri)) # format拼接url


def get_user_info(request):
    # 获取用户信息
    code = request.GET.get("code")
    if not code:
        return HttpResponse("not find code")
    token_url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid={0}&secret={1}&code={2}&grant_type=authorization_code"
    # 通过code 可以获取到access_token ，但是code 只能获取道一次获取token 的时候可能要刷新，不然会获取不到token
    data = requests.get(token_url.format(app_id, AppSecret, code))
    # 转为json 格式的字符串
    data = json.loads(data.content.decode("utf-8"))
    # 获取access_token
    access_token = data['access_token']
    open_id = data['openid']
    refresh_token = data['refresh_token']
    if not access_token or not open_id:
        return None  # 判断是否有token 和open_id
    # 用户的url
    user_url = "https://api.weixin.qq.com/sns/userinfo?access_token={0}&openid={1}&lang=zh-CN"
    d = requests.get(user_url.format(access_token, open_id))
    d = d.content.decode("utf-8")
    if not d:
        return None
    d = json.loads(d)
    if d.has_key("errcode") and d["errcode"] == 40001:
        # token过期解决
        refresh_token_url = "https://api.weixin.qq.com/sns/oauth2/refresh_token?appi={0}&grant_type=refresh_type=refresh_token&refresh_token={1}"
    r_d = requests.get(refresh_token_url.format(app_id, refresh_token))
    r_d = json.loads(r_d.content.decode("utf-8"))
    access_token = r_d["access_token"]
    d = requests.get(user_url.format(access_token, open_id))
    d = d.content.decode("utf-8")
    response = HttpResponse(json.dumps(d))
    # 设置cookie 将用户信息保存到cookie里面
    response.set_cookie("userinfo", json.dumps(d), max_age=7 * 24 * 3600)  # 设置过期时间7 天
    return response
