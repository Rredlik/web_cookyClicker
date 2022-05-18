from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from users.forms import UserForm


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


def UserLoginView(request):
    form = UserForm()

    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse('Аккаунт отлючен!')
        else:
            return HttpResponse('Не верный логин')
        return render(request, 'login.html', {'form': form, 'invalid': True})

    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)
