from random import randint

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Product, Feedback
from .forms import FeedbackForm


def index(request):
    return render(request, 'index.html', {'rand': randint(1, 10)})


def show_all(request):
    return render(
        request,
        'show_all.html',
        {'products': Product.objects.all()}
    )


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