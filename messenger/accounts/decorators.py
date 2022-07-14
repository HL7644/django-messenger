from django.http import HttpResponse
from django.shortcuts import redirect

#decorator: takes ftn as input -> add another functionality to it before it is called(declared)
def unauthenticated_user(view_ftn): #to determine user authentication
    def wrapper_ftn(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/mails/')
        else:
            return view_ftn(request, *args, **kwargs)
    return wrapper_ftn

def allowed_users(allowed_roles=[]):
    def decorator(view_ftn):
        def wrapper_ftn(request, *args, **kwargs):
            print(request.user.groups.all()[0].name)
            return view_ftn(request, *args, **kwargs)
        return wrapper_ftn
    return decorator