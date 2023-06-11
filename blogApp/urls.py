from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from . import views

urlpatterns = [
    path('',PostListView.as_view(extra_context={'title':'Home'}),name='blog-home'),
    path('user/<username>',UserPostListView.as_view(extra_context={'title':"<username>'s posts"}),name='user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(extra_context={'title':'Post Details'}),name='post-details'), 
    path('post/new/',PostCreateView.as_view(extra_context={'title':'Post Create'}),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(extra_context={'title':'Post Update'}),name='post-update'), 
    path('post/<int:pk>/delete/',PostDeleteView.as_view(extra_context={'title':'Post delete'}),name='post-delete'),
    path('about/',views.about,name='blog-about')
]
