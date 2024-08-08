# ed/urls.py
from django.urls import path

import ed.views as v


urlpatterns = [
    path('', v.home, name="home"),
    path('video/', v.videos, name="video"),
    # Forum
    path('forum/', v.forum_view, name='forum'),
    path('forum/comment/', v.comment_view, name='comment'),
    path('forum/create', v.forum_create, name='create'),
    path('forum/search/', v.search_post, name='message_search'),
    path('forum/filter', v.advfilter, name='advfilter'),
    path('forum/searchworker/', v.searchworker_view, name='searchworker'),
    path('posts/', v.posts, name='posts'),
    path('contact/', v.contacts, name='contact'),
    # Account
    path('login/', v.login_view, name='login_view'),
    path('register/', v.register, name='register'),
    path('logout/', v.logout_view, name='logout'),

]