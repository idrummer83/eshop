from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from .forms import LoginForm
# Create your views here.


def log_in(request):
    if request.user.is_authenticated:
        # return redirect('/products/all')
        return redirect(reverse('show_all'))
    form = LoginForm()
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['name'],
            password=request.POST['passwd']
        )
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '/products/all')
            return redirect(next_url)
    return render(request, 'login.html', {
        'form': form
    })


def log_out(request):
    logout(request)
    # return redirect('/')
    return redirect(reverse('login'))
