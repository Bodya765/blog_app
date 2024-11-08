from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import BlogPost

class BlogListView(ListView):
    model = BlogPost
    context_object_name = 'blogposts'
    paginate_by = 5

class BlogDetailView(DetailView):
    model = BlogPost

class BlogPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    fields = ['title', 'text']
    template_name = 'blog_app/blogpost_form.html'
    success_url = reverse_lazy('blog_app:all_posts')

    def test_func(self):
        blogpost = self.get_object()
        return self.request.user == blogpost.owner

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy("blog_app:all_posts")

    def test_func(self):
        blogpost = self.get_object()
        return self.request.user == blogpost.owner

class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ['title', 'text']
    template_name = 'blog_app/blogpost_form.html'
    success_url = reverse_lazy('blog_app:all_posts')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def home(request):
         return render(request, 'home.html')