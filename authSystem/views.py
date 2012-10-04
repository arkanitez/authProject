from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from authSystem.RegForms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from authSystem.models import UserAccount

def UserRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                    username     = form.cleaned_data['username'],
                    email        = form.cleaned_data['email'],
                    password     = form.cleaned_data['password'])
            user.save()
            useraccount = UserAccount(user=user, name=form.cleaned_data['name'], birthday=form.cleaned_data['birthday'])
            useraccount.save()
            return HttpResponseRedirect('/profile')
        else:
            return render_to_response('authSystem/register.html',{'form':form}, context_instance=RequestContext(request))
    else:
        form = RegistrationForm
        context = {'form': form }
        return render_to_response('authSystem/register.html', context, context_instance=RequestContext(request))

def LoginRequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile')
    if request.method == 'POST':
        pass
    else:
        form = LoginForm()
        context = {'form':form}
        return render_to_response('authSystem/login.html', context, context_instance=RequestContext(request))
