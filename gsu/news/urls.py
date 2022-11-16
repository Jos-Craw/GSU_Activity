from django.urls import path
from django.contrib.auth.views import LoginView
from .views import index,zap_consult, zapis,zapisg,otpis,otpisg,cult,consult,otz, mass,sport,trud, POSTLoginView, profile, POSTLogoutView, ChangeUserInfoView, POSTChangeView, RegisterUserView, RegisterDoneView, user_activate, DeleteUserView, detail

app_name = 'news'

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', detail, name='detail'),
    path('cult/', cult, name='cult'),
    path('mass/', mass, name='mass'),
    path('sport/', sport, name='sport'),
    path('trud/', trud, name='trud'),
    path('consult/', consult, name='consult'),
    path('otz/', otz, name='otz'),
    path('zapis_consult/<int:pk>/', zap_consult, name='zap_consult'),
    path('zapis/<int:pk>/', zapis, name='zapis'),
    path('zapisg/<int:pk>/', zapisg, name='zapisg'),
    path('otpis/<int:pk>/', otpis, name='otpis'),
    path('otpisg/<int:pk>/', otpisg, name='otpisg'),
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/login/', POSTLoginView.as_view(), name='login'),
    path('accounts/logout/', POSTLogoutView.as_view(), name='logout'),
    path('accounts/profile/delete', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/change', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/password/change', POSTChangeView.as_view(), name='password_change'),   
]
