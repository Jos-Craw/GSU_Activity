from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, AdvUser, Comment
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ChangeUserInfoForm, RegisterUserForm, CommentForm, Subscribe ,Index
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.signing import BadSignature
from .utilities import signer
from django.core.mail import send_mail
from django.conf import settings


@login_required
def index(request):
    posts = Post.objects.all() #добавить фильтр по датам
    return render(request, 'news/index.html', {'posts': posts})

@login_required
def profile(request):
    posts = Post.objects.filter(zapisi=request.user.id)
    return render(request, 'news/profile.html', {'posts': posts})


@login_required
def detail(request, pk):
	messageSent = False
	post = get_object_or_404(Post, pk=pk)
	comments = Comment.objects.filter(post=pk,moderation=True)
	initial = {'post': post.pk}
	initial['author'] = request.user.first_name + ' ' + request.user.last_name
	form_class = CommentForm
	form = form_class(initial=initial)
	if request.method == 'POST' or request.FILES:
		form = CommentForm(request.POST)
		c_form = form_class(request.POST, request.FILES)
		if c_form.is_valid():
			c_form.save()
		else:
			form = c_form
		if form.is_valid():
			cd = form.cleaned_data
			subject = 'НОВЫЙ КОММЕНТАРИЙ'
			message = 'Зайдите на сайт для одобрения комментария: '+cd['content'] + ' от ' + request.user.first_name + ' ' +request.user.last_name + ' ' +request.user.phone_num+ ' ' + request.user.email
			send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['novogencev.pavel@gmail.com'])
			messageSent = True
	return render(request, 'news/detail.html', {'post': post, 'comments': comments, 'form': form,'messageSent': messageSent})

@login_required
def cult(request):
    posts = Post.objects.all()
    return render(request, 'news/cult.html', {'posts': posts})

@login_required
def sport(request):
    posts = Post.objects.all()
    return render(request, 'news/sport.html', {'posts': posts})

@login_required
def mass(request):
    posts = Post.objects.all()
    return render(request, 'news/mass.html', {'posts': posts})

@login_required
def trud(request):
    posts = Post.objects.all()
    return render(request, 'news/trud.html', {'posts': posts})

@login_required
def otz(request):
	comments = Comment.objects.filter(moderation=True)
	return render(request, 'news/otz.html', {'comments': comments})

@login_required
def consult(request):
	posts = Post.objects.all()
	return render(request, 'news/consult.html', {'posts': posts})


class POSTLoginView(LoginView):
    template_name = 'news/login.html'


class POSTLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'news/logout.html'


class POSTChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'news/password_change.html'
    success_url = reverse_lazy('news:profile')
    success_message = 'Password changed'


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = 'news/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('news:profile')
    success_message = 'Info changed'

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'news/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('news:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'news/register_done.html'


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = AdvUser
    template_name = 'news/delete_user.html'
    success_url = reverse_lazy('news:index')

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'User deleted')
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'news/bad_signature.html')
    user = get_object_or_404(AdvUser, username=username)
    if user.is_activated:
        template = 'news/user_is_activated.html'
    else:
        template = 'news/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)

def zapis(request, pk):
	post = get_object_or_404(Post, pk=pk)
	messageSent = False
	if request.method == 'POST':
		form = Subscribe(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			initial = {'post': post.pk}
			subject = post.content + ' ЗАПИСЬ ' 
			message = 'ЛИЧНАЯ ЗАПИСЬ: '+cd['message'] + ' от ' + request.user.first_name + ' ' +request.user.last_name + ' ' +request.user.phone_num+ ' ' + request.user.email
			send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['novogencev.pavel@gmail.com'])
			messageSent = True
			post.zapisi.add(request.user.id)
	else:
		form = Subscribe()
	return render(request, 'news/zapis.html', {'form': form,'messageSent': messageSent,})

def zapisg(request, pk):
	post = get_object_or_404(Post, pk=pk)
	messageSent = False
	if request.method == 'POST':
		form = Subscribe(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			initial = {'post': post.pk}
			subject = post.content + ' ЗАПИСЬ ' 
			message = 'ГРУППОВАЯ ЗАПИСЬ: '+cd['message'] + ' от ' + request.user.first_name + ' ' +request.user.last_name + ' ' +request.user.phone_num+ ' ' + request.user.email
			send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['novogencev.pavel@gmail.com'])
			messageSent = True
			post.zapisi.add(request.user.id)
	else:
		form = Subscribe()
	return render(request, 'news/zapisg.html', {'form': form,'messageSent': messageSent,})

def otpis(request, pk):
	post = get_object_or_404(Post, pk=pk)
	messageSent = False
	if request.method == 'POST':
		form = Subscribe(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			initial = {'post': post.pk}
			subject = post.content + ' ОТПИСЬ ' 
			message = 'ЛИЧНАЯ ОТПИСЬ: '+cd['message'] + ' от ' + request.user.first_name + ' ' +request.user.last_name + ' ' +request.user.phone_num + ' ' + request.user.email
			send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['novogencev.pavel@gmail.com'])
			messageSent = True
			post.zapisi.remove(request.user.id)
	else:
		form = Subscribe()
	return render(request, 'news/otpisg.html', {'form': form,'messageSent': messageSent,})

def otpisg(request, pk):
	post = get_object_or_404(Post, pk=pk)
	messageSent = False
	if request.method == 'POST':
		form = Subscribe(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			initial = {'post': post.pk}
			subject = post.content + ' ОТПИСЬ ' 
			message = 'ГРУППОВАЯ ОТПИСЬ: '+cd['message'] + ' от ' + request.user.first_name + ' ' +request.user.last_name + ' ' +request.user.phone_num+ ' ' + request.user.email
			send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['novogencev.pavel@gmail.com'])
			messageSent = True
			post.zapisi.remove(request.user.id)
	else:
		form = Subscribe()
	return render(request, 'news/otpisg.html', {'form': form,'messageSent': messageSent,})