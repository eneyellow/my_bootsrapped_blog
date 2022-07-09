from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from . models import BlogPost



class HomePageView(TemplateView):
    template_name = 'home.html'


class BlogListView(ListView):
    model = BlogPost
    ordering = ('-date_added',)
    template_name = 'post_list.html'
    
    
    
class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'post_detail.html'
    
    
    
class BlogCreateView(CreateView):
    model = BlogPost
    fields = '__all__'
    template_name = 'post_new.html'
    
    
    
class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'text']
    template_name = 'post_edit.html'
    
    
class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    