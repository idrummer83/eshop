from django.conf.urls import url
from django.views.generic.list import ListView
from .views import show_all, detail
from .models import Product

urlpatterns = [
    url(r'^all/$', show_all, name='show_all'),
    url(r'^detail/(?P<product_id>\d+)$', detail, name='detail'),
    url(r'^all1/$', ListView.as_view(model=Product, paginate_by=2, template_name='show_all1.html'))
    # url(r'^all1/$', ListView.as_view(
    #     queryset=Product.objects.filter(id=1), paginate_by=2, template_name='show_all1.html'))
]
