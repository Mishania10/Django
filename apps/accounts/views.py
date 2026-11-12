from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render

from .forms import LoginForm, RegistrationForm


def register(request):
    if request.user.is_authenticated:
        return redirect('my_requests')
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('create_request')
    return render(request, 'accounts/register.html', {'form': form})


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm


class AccountLogoutView(LogoutView):
    next_page = 'create_request'
