
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from .views import user_form_view
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('login/',views.login, name="login"),
    path('register/',views.register, name="register"),
    path('subscribe/',views.subscribe, name="subscribe"),
    path('contactus/',views.contactus, name="contactus"),
    path('aboutus/',views.aboutus, name="aboutus"),
    path('ourvision/',views.ourvision, name="ourvision"),
    path('ourstory/',views.ourstory, name="ourstory"),
    path('privacypolicy/',views.privacypolicy, name="privacypolicy"),
    path('termsandconditions/',views.termsandconditions, name="termsandconditions"),
    path('services/',views.services, name="services"),
    path('blogs/',views.blogs, name="blogs"),
    # path('news/',views.news, name="news"),
    # path('business_news/',views.business_news, name="business_news"),
    path('companies/',views.companies, name="companies"),
    
    
    path('register_user/', views.register_user, name='register_user'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    # path('requestdone/', views.requestdone, name='requestdone'),
    path('login_operation/', views.login_operation, name='login_operation'),
    
    
    path('business_news/', views.business_news, name='business_news'),
    
    
    
    path("companies/<int:pk>/", views.company_detail, name="company_detail"),
path("business_news/<int:pk>/", views.news_detail, name="news_detail"),
path("blogs/<int:pk>/", views.blog_detail, name="blog_detail"),
path("jobs_list/", views.jobs_list, name="jobs_list"),


# path('contact', views.contact, name='contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)