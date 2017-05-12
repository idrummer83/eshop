from random import randint
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse_lazy

from .models import Product, Feedback
from .forms import FeedbackForm


def index(request):
    return render(request, 'index.html', {
        'rand': randint(1, 10)
    })

@login_required(login_url='/')
def show_all(request):
    p = Paginator(Product.objects.order_by('pk').all(), 2)
    page = int(request.GET.get('p', 1))
    return render(
        request,
        'show_all.html',
        {'products': p.page(page)}
    )

# @login_required(login_url='/')
@login_required(login_url=reverse_lazy('login'))
def detail(request, product_id):
    form = FeedbackForm()
    product = get_object_or_404(Product, pk=int(product_id))
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            Feedback.objects.create(
                nick=form.cleaned_data['nick'],
                feedback=form.cleaned_data['feedback'],
                product=product,
            )
            messages.success(request, 'Feedback is added successfully')
            return redirect('/products/detail/' + product_id)
    return render(
        request,
        'detail.html',
        {
            'product': product,
            'form': form,
            'feedbacks': Feedback.objects.filter(product=product),
        }
    )
