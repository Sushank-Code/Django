from django.shortcuts import render

# Create your views here.
def setcookie(request):
    response = render(request,'cooki_app/set_cookie.html')
    response.set_cookie('auth_id','iiiiii')
    response.set_cookie('pay_id','eeeeee')
    response.set_cookie('hi_id','eeeeee',max_age=120)
    return response

def getcookie(request):
    # id = request.COOKIES['auth_id']      # key of cookie
    # id = request.COOKIES.get('auth_id')  # This will display none if thereis no key

    all_cookie = request.COOKIES 
    context = {
        'all_cookie': all_cookie
    }
    return render(request,'cooki_app/get_cookie.html',context)

def delcookie(request):
    cookie_name = "auth_id"
    response = render(request,'cooki_app/del_cookie.html',{'deleted_cookie':cookie_name})
    response.delete_cookie(cookie_name)
    return response
