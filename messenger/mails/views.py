from django.shortcuts import render, get_object_or_404, redirect
from .models import Mail
from .forms import Mail_Form
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
# Create your views here.

@login_required(login_url='/login/')
def mail_create_view(request):
    initial_data={
        'from_user': str(request.user)
    }
    form=Mail_Form(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        form=Mail_Form()
        messages.success(request, "Message Sent!")
        return redirect('/mails/')
    context={'form': form}
    return render(request, 'mails/mail_create.html', context=context)

@login_required(login_url='/login/')
def mail_detail_view(request, id):
    obj=Mail.objects.get(id=id)
    context={
        'mail': obj
    }
    return render(request, 'mails/mail_detail.html', context=context)

@login_required(login_url='/login/')
def mail_list_view(request):
    user=str(request.user)
    print(user)
    if request.user.is_authenticated==False:
        messages.info(request, "You Must Be Logged In")
        return redirect('/login/')
    queryset=Mail.objects.all()
    valid_set=[] #valid object set for corresponding user 
    for query in queryset:
        print(query.to_user)
        if str(query.to_user)==user:
            valid_set.append(query)
    if len(valid_set)==0: #if no email to show
        messages.info(request, "No Messages to Show")
    context={
        'mails_list': valid_set
    }
    return render(request, 'mails/mail_list.html', context=context)