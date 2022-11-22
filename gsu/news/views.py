from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, AdvUser, Comment, Consult,Section, Tvor ,Trud, Volant
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ChangeUserInfoForm, RegisterUserForm, CommentForm, Subscribe ,Index,NewConsult,zapis_consult, PostForm,Subscribeg,TvorForm,VistForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.signing import BadSignature
from .utilities import signer
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime, timedelta, date

def index(request):
	weekd=datetime.today().isocalendar()[1] 
	posts = Post.objects.filter(eventdate__week=weekd)
	if request.method == 'POST':
		form = Index(request.POST)
		if form.is_valid():
			nach = form.cleaned_data['Начало']
			con = form.cleaned_data['Конец']
			posts = Post.objects.filter(eventdate__range=(nach,con))
	else:
		form = Index()
	return render(request, 'news/index.html', {'form': form,'posts': posts})

@login_required
def profile(request):
    posts = Post.objects.filter(zapisi=request.user.id)
    your_posts = Post.objects.filter(author=request.user.pk)
    a = date.today()
    b = a + timedelta(days=1)
    return render(request, 'news/profile.html', {'posts': posts,'your_posts':your_posts,'a':a,'b':b})

@login_required
def create(request):
    if request.method == 'POST' or request.FILES:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('news:index')
    else:
        form = PostForm(initial={'author': request.user.pk})
    context = {'form': form}
    return render(request, 'news/create.html', context)

@login_required
def create_v(request):
    if request.method == 'POST' or request.FILES:
        form = VistForm(request.POST, request.FILES)
        if form.is_valid():
        	vist = form.save()
        	return redirect('news:index')
    else:
        form = VistForm(initial={'author': request.user.pk})
    context = {'form': form}
    return render(request, 'news/create.html', context)

@login_required
def deletepost(request, pk):
	useremail=[]
	users = AdvUser.objects.all()
	messageSent = False
	post = get_object_or_404(Post, pk=pk)
	if request.method == 'POST':
		for d in post.zapisi.all():
  			print(d.email)
  			useremail.append(d.email)
		subject = 'ОТМЕНЯ МЕРОПРИЯТИЯ' 
		message = 'Отменя ' + post.content + ' ' + str(post.eventdate)+ ' ' +str(post.eventtime)
		send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, useremail)
		messageSent = True
		post.delete()
		return redirect('news:index')
	else:
		context = {'post': post,'messageSent': messageSent}
	return render(request, 'news/deletepost.html', context)

@login_required
def detail(request, pk):
	your_zapisi = Post.objects.filter(zapisi=request.user.id)
	messageSent = False
	post = get_object_or_404(Post, pk=pk)
	comments = Comment.objects.filter(post=pk,moderation=True)
	initial = {'post': post.pk}
	initial['author'] = request.user.first_name + ' ' + request.user.last_name
	a = date.today()
	b = a + timedelta(days=1)
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
			send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['novogencev.pavel@gmail.com']) #hodanovich@gsu.by, osnach@gsu.by
			messageSent = True
	return render(request, 'news/detail.html', {'post': post, 'comments': comments, 'form': form,'messageSent': messageSent,'your_zapisi':your_zapisi,'a':a,'b':b})


def cult(request):
    posts = Post.objects.all()
    your_zapisi = Post.objects.filter(zapisi=request.user.id)
    tvors = Tvor.objects.filter(otobr=True) 
    return render(request, 'news/cult.html', {'posts': posts,'your_zapisi':your_zapisi,'tvors':tvors})


def tvor(request,pk):
	naprav = get_object_or_404(Tvor, pk=pk)
	messageSent = False
	if request.method == 'POST':
		form = TvorForm(request.POST)
		if form.is_valid(): 
			cd = form.cleaned_data
			initial = {'naprav': naprav.pk} 
			subject = 'ЗАПИСЬ на творческое направление ' + cd['Роль']
			message = 'ЗАПИСЬ на '+ naprav.name +' '+cd['Роль'] +' ' + request.user.first_name + ' ' +request.user.last_name + ' ' +request.user.phone_num+ ' ' + request.user.email+' ' +request.user.group 
			send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['novogencev.pavel@gmail.com']) #VELIKY@gsu.by
			messageSent = True
	else:
		form = TvorForm
	return render(request, 'news/tvor.html',{'form':form,'messageSent': messageSent})


def sport(request):
	sections = Section.objects.filter(otobr=True)
	posts = Post.objects.all()
	your_zapisi = Post.objects.filter(zapisi=request.user.id) 
	return render(request, 'news/sport.html', {'posts': posts,'your_zapisi':your_zapisi,'sections':sections})


def mass(request):
	a = date.today()
	posts = Post.objects.all()
	your_zapisi = Post.objects.filter(zapisi=request.user.id) 
	return render(request, 'news/mass.html', {'posts': posts,'your_zapisi':your_zapisi,'a':a})

def trud(request):
    posts = Post.objects.all()
    truds = Trud.objects.filter(otobr=True)
    volonts = Volant.objects.filter(otobr=True)
    your_zapisi = Post.objects.filter(zapisi=request.user.id) 
    return render(request, 'news/trud.html', {'posts': posts,'your_zapisi':your_zapisi,'truds':truds,'volonts': volonts})

def trud_naprav(request,pk):
	trud = get_object_or_404(Trud, pk=pk)
	messageSent = False
	if request.method == 'POST':
		form = zapis_consult(request.POST)
		if form.is_valid(): 
			initial = {'trud': trud.pk}
			subject = 'ЗАПИСЬ на трудовое направление '  
			message = 'ЗАПИСЬ на '+ trud.name +' ' + request.user.first_name + ' ' +request.user.last_name + ' ' +request.user.phone_num+ ' ' + request.user.email+' ' +request.user.group 
			send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['novogencev.pavel@gmail.com']) #FEDORENKO@gsu.by
			messageSent = True
	else:
		form = zapis_consult
	return render(request, 'news/tvor.html',{'messageSent': messageSent})


def volon_naprav(request,pk):
	volont = get_object_or_404(Volant, pk=pk) 
	messageSent = False
	if request.method == 'POST':
		form = zapis_consult(request.POST)
		if form.is_valid():
			if volont.name == 'Профсоюз':
				email = 'novogencev.pavel@gmail.com' #AZYAVCHIKOV@gsu.by
			else:
				email = 'novogencev.pavel@gmail.com' #FEDORENKO@gsu.by
			initial = {'volont': volont.pk}
			subject = 'ЗАПИСЬ на волонтерское направление '  
			message = 'ЗАПИСЬ на '+ volont.name +' ' + request.user.first_name + ' ' +request.user.last_name + ' ' +request.user.phone_num+ ' ' + request.user.email+' ' +request.user.group 
			send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
			messageSent = True
	else:
		form = zapis_consult
	return render(request, 'news/tvor.html',{'messageSent': messageSent})	



def otz(request):
	comments = Comment.objects.filter(moderation=True)
	return render(request, 'news/otz.html', {'comments': comments})

def sec(request,pk):
	section = get_object_or_404(Section, pk=pk)
	messageSent = False
	if request.method == 'POST':
		form = zapis_consult(request.POST)
		if form.is_valid(): 
			initial = {'section': section.pk}
			subject = 'ЗАПИСЬ на секцию '  
			message = 'ЗАПИСЬ на '+ section.name +' ' + request.user.first_name + ' ' +request.user.last_name + ' ' +request.user.phone_num+ ' ' + request.user.email+' ' +request.user.group 
			send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['novogencev.pavel@gmail.com']) #KULESHOV@gsu.by
			messageSent = True
	else:
		form = zapis_consult
	return render(request, 'news/sec.html',{'messageSent': messageSent})


def consult(request):
	consults = Consult.objects.filter(zan=False)
	form_class = NewConsult
	form = form_class
	if request.method == 'POST':
		c_form = form_class(request.POST, request.FILES)
		if c_form.is_valid():
			c_form.save()
		else:
			form = c_form
	return render(request, 'news/consult.html', {'consults': consults, 'form': form})

def zap_consult(request, pk):
	consult = get_object_or_404(Consult, pk=pk)
	messageSent = False
	if request.method == 'POST':
		form = zapis_consult(request.POST)
		if form.is_valid(): 
			initial = {'consult': consult.pk}
			subject = 'ЗАПИСЬ на консультацию '  
			message = 'ЗАПИСЬ на '+ str(consult.eventdate) +' '+ consult.eventtime + ' : ' + request.user.first_name + ' ' +request.user.last_name + ' ' +request.user.phone_num+ ' ' + request.user.email+ ' ' +request.user.group
			send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['novogencev.pavel@gmail.com']) #TROSHEVA@gsu.by
			messageSent = True
			consult.zan = True
			consult.save()
	else:
		form = zapis_consult
	return render(request,'news/zapis_consult.html',{'consult':consult,'form': form,'messageSent': messageSent})



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
			if post.vist == True:
				email = 'novogencev.pavel@gmail.com' #LVDUBROVSKAYA@gsu.by
			elif post.tags == 'cult':
				email = 'novogencev.pavel@gmail.com' #VELIKY@gsu.by
			elif post.tags == 'sport':
				email = 'novogencev.pavel@gmail.com' #KULESHOV@gsu.by
			elif post.tags == 'mass':
				email = 'novogencev.pavel@gmail.com' #osnach@gsu.by,bardashevich@gsu.by
			elif post.tags == 'trud':
				email = 'novogencev.pavel@gmail.com' #FEDORENKO@gsu.by
			cd = form.cleaned_data
			initial = {'post': post.pk}
			subject = post.name + ' ЗАПИСЬ ' 
			message = 'ЛИЧНАЯ ЗАПИСЬ: от ' + request.user.first_name + ' ' +request.user.last_name + ' ' +request.user.phone_num+ ' ' + request.user.email+' ' +request.user.group
			send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
			messageSent = True
			post.zapisi.add(request.user.id)
			post.mesta = post.mesta -1
			post.save()
	else:
		form = Subscribe()
	return render(request, 'news/zapis.html', {'form': form,'messageSent': messageSent})

def zapisg(request, pk):
	post = get_object_or_404(Post, pk=pk)
	messageSent = False
	if request.method == 'POST':
		form = Subscribeg(request.POST)
		if form.is_valid():
			if post.vist == True:
				email = 'novogencev.pavel@gmail.com' #LVDUBROVSKAYA@gsu.by
			elif post.tags == 'cult':
				email = 'novogencev.pavel@gmail.com' #VELIKY@gsu.by
			elif post.tags == 'sport':
				email = 'novogencev.pavel@gmail.com' #KULESHOV@gsu.by
			elif post.tags == 'mass':
				email = 'novogencev.pavel@gmail.com' #osnach@gsu.by,bardashevich@gsu.by
			elif post.tags == 'trud':
				email = 'novogencev.pavel@gmail.com' #FEDORENKO@gsu.by
			cd = form.cleaned_data
			initial = {'post': post.pk}
			subject = post.name + ' ЗАПИСЬ ' 
			message = 'ГРУППОВАЯ ЗАПИСЬ: '+cd['message'] + ' от ' + request.user.first_name + ' ' +request.user.last_name + ' ' +request.user.phone_num+ ' ' + request.user.email
			send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
			messageSent = True
			post.zapisi.add(request.user.id)
			post.mesta = post.mesta - cd['colvo']
			post.save()
	else:
		form = Subscribeg()
	return render(request, 'news/zapis.html', {'form': form,'messageSent': messageSent,})

def otpis(request, pk):
	post = get_object_or_404(Post, pk=pk)
	messageSent = False
	if request.method == 'POST':
		form = Subscribe(request.POST)
		if form.is_valid():
			if post.vist == True:
				email = 'novogencev.pavel@gmail.com' #LVDUBROVSKAYA@gsu.by
			elif post.tags == 'cult':
				email = 'novogencev.pavel@gmail.com' #VELIKY@gsu.by
			elif post.tags == 'sport':
				email = 'novogencev.pavel@gmail.com' #KULESHOV@gsu.by
			elif post.tags == 'mass':
				email = 'novogencev.pavel@gmail.com' #osnach@gsu.by,bardashevich@gsu.by
			elif post.tags == 'trud':
				email = 'novogencev.pavel@gmail.com' #FEDORENKO@gsu.by
			cd = form.cleaned_data
			initial = {'post': post.pk}
			subject = post.name + ' ОТПИСЬ ' 
			message = 'ЛИЧНАЯ ОТПИСЬ: от ' + request.user.first_name + ' ' +request.user.last_name + ' ' +request.user.phone_num + ' ' + request.user.email+ ' ' +request.user.group
			send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
			messageSent = True
			post.zapisi.remove(request.user.id)
			post.mesta = post.mesta +1
			post.save()
	else:
		form = Subscribe()
	return render(request, 'news/otpis.html', {'form': form,'messageSent': messageSent,})

def otpisg(request, pk):
	post = get_object_or_404(Post, pk=pk)
	messageSent = False
	if request.method == 'POST':
		form = Subscribeg(request.POST)
		if form.is_valid():
			if post.vist == True:
				email = 'novogencev.pavel@gmail.com' #LVDUBROVSKAYA@gsu.by
			elif post.tags == 'cult':
				email = 'novogencev.pavel@gmail.com' #VELIKY@gsu.by
			elif post.tags == 'sport':
				email = 'novogencev.pavel@gmail.com' #KULESHOV@gsu.by
			elif post.tags == 'mass':
				email = 'novogencev.pavel@gmail.com' #osnach@gsu.by,bardashevich@gsu.by
			elif post.tags == 'trud':
				email = 'novogencev.pavel@gmail.com' #FEDORENKO@gsu.by
			cd = form.cleaned_data
			initial = {'post': post.pk}
			subject = post.name + ' ОТПИСЬ ' 
			message = 'ГРУППОВАЯ ОТПИСЬ: '+cd['message'] + ' от ' + request.user.first_name + ' ' +request.user.last_name + ' ' +request.user.phone_num+ ' ' + request.user.email
			send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
			messageSent = True
			post.zapisi.remove(request.user.id)
			post.mesta = post.mesta + cd['colvo']
			post.save()
	else:
		form = Subscribeg()
	return render(request, 'news/otpis.html', {'form': form,'messageSent': messageSent,})