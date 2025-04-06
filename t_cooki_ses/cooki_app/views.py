from django.shortcuts import render

# Create your views here.

# cookie

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

# session

def setsession(request):
    request.session['fname'] = 'Sushank'
    request.session['lname'] = 'Lamsal'
    request.session['roll']= 101
    return render(request,'cooki_app/set_session.html')

def getsession(request):
    all_session = request.session
    print(all_session)
    fid = request.session.get('fname')
    return render(request,'cooki_app/get_session.html',{'all_session':all_session,
                                                        'fid':fid})

def delsession(request):
    ses_name = 'lname'
    if ses_name in request.session:
        del request.session[ses_name]
    return render(request,'cooki_app/del_session.html',{'del_session':ses_name})

def flushsession(request):
    request.session.flush()
    return render(request,'cooki_app/flush_session.html')