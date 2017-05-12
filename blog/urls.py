
from django.conf.urls import url
# from django.views.generic import DetailView

from blog.models import Post
from .views import details, posts, add_post, edit_post

urlpatterns = [
    # url(r'^details/(?P<date>.+?)/(?P<slug>.+?)$', DetailView.as_view(
    #     model=Post,
    #     template_name='post_detail.html'
    # ), name='post_detail'),
    url(r'^details/(?P<date>.+?)/(?P<slug>.+?)$', details, name='post_detail'),
    url(r'^edit_post/(?P<date>.+?)/(?P<slug>.+?)$', edit_post, name='edit_post'),
    url(r'^posts/$', posts, name='posts'),
    url(r'^add_post/$', add_post, name='add_post'),
]
