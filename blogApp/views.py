from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User

#home page views with render funcn
def home(request):
    return render(request, 'blogApp/home.html',{
        'posts' : Post.objects.all(),
        'title' : 'Home'
        })

#about page views with render funcn
def about(request):
    return render(request, 'blogApp/about.html',{
        'title': 'About'
        })

#Post views start(view,create,update,delete)
#<!--Post views page class-->
class PostListView(ListView):
    model = Post
    template_name = 'blogApp/home.html' #<app>/<model>_<viewtype>.html, <blogApp>/<Post>_<List>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] #to show the latest post first
    paginate_by = 2 #paginations 

#<!--Respective User's Posts view page-->
class UserPostListView(ListView):
    model = Post
    template_name = 'blogApp/user_posts.html' #<app>/<model>_<viewtype>.html, <blogApp>/<Post>_<List>.html
    context_object_name = 'posts'
    paginate_by = 2 #paginations 

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
    '''def get_context_data(self, **kwargs):
        context = super(UserPostListView,self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        context['title'] = user.username
        return context'''

#<!--Post Details page class-->
class PostDetailView(DetailView):
    model = Post

#<!--Post Create page class-->
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#<!--Post Update page class-->
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
        
#<!--Post Delete page class-->
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False  
#Post views end(view,create,update,delete)