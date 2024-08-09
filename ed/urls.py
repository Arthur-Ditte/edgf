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
    # Posts
    path('posts/', v.posts, name='posts'),
    path('contact/', v.contacts, name='contact'),
    # Account
    path('login/', v.login_view, name='login_view'),
    path('register/', v.register, name='register'),
    path('logout/', v.logout_view, name='logout'),
    path('sale/', v.sale, name='sale'),
    # Profile
    path('profile/', v.profile_view, name='profile'),
    path('profile/fa/', v.fa, name='fa'),
    path('profileadd', v.profile_add, name='profile_add'),
    path('notification', v.notification_view, name='notification'),
    path('settings', v.settings_view, name='settings'),
    # For Supporter
    path('supporter/', v.supporter, name='supporter'),
    # Help
    path('problems', v.problems, name='problem'),
    # Rickroll
    path('tests', v.rickroll, name='rickroll'),


]