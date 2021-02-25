from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from .models import Post, Comment, Category, Contact
from .forms import Add_Comment, Add_Post, ContactForm
from django.views.generic import (
    DetailView,
    ListView,
    CreateView
)
from django.views.generic.edit import FormMixin
from django.utils import timezone


def home(request):
    context = {
        'posts': Post.objects.filter(category=2).first(),
        'recentposts': Post.objects.all()[:4],
        'DuasPosts': Post.objects.filter(category=4
                                         ).all(),
        'peotry': Post.objects.filter(category=5).all()
    }
    return render(request, 'index.html', context)


class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'post-detailview.html'
    form_class = Add_Comment

    def get_success_url(self):
        return reverse('duas-detail', kwargs={'pk': self.object.id})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = Comment.objects.filter(
            post=self.kwargs['pk']).count()
        context['categoy'] = getattr(super().get_object(), 'category')
        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.save()
        return super(PostDetailView, self).form_valid(form)

    def get_object(self):
        obj = super().get_object()
        obj.post_view += 1
        obj.save()
        return obj


class CreatePost(CreateView):
    model = Post
    form_class = Add_Post
    template_name = 'post-detailview.html'

    def form_valid(self, form):
        return super().form_valid(form)

    success_url = reverse_lazy('home')


class CatListView(ListView):

    template_name = 'category.html'
    context_object_name = 'catlis'

    def get_queryset(self):

        content = {
            'cat': self.kwargs['Category'],
            'posts': Post.objects.filter(category__name=self.kwargs['Category'])
        }
        return content


class TagIndexView(ListView):
    template_name = 'tagpostlsit.html'
    context_object_name = 'tag_list'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))


def category_list(request):
    category_list = Category.objects.exclude(name='Default')
    context = {
        "category_list": category_list,
    }
    return context


def about(request):
    return render(request, 'about.html')


def user_admin(request):
    return render(request, 'admin.html')


def disclaimer(request):
    return render(request, 'Disclaimer.html')


def PrivacyPolicy(request):
    return render(request, 'privacy.html')


class Contact(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contactus.html'

    success_url = reverse_lazy('home')


def search(request):
    querry = request.GET['querry']
    if len(querry) > 25:
        AllPost = Post.objects.none
    else:
        AllPosttitle = Post.objects.filter(title__icontains=querry)
        AllPostcontent = Post.objects.filter(content__icontains=querry)
        AllPost = AllPosttitle.union(AllPostcontent)

    context = {
        'AllPost': AllPost,
        'querry': querry
    }
    return render(request, 'searchresult.html',  context)
