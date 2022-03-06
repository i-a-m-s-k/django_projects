
from django.http import HttpResponse

def owner(request):
    return HttpResponse("Hello, world. 3c2140d1 is the polls owner.")

def myview(request) :
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    resp = HttpResponse('view count='+str(num_visits))
    resp.set_cookie('dj4e_cookie', '3c2140d1', max_age=1000)
    return resp


