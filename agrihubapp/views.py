

import email
from email.message import EmailMessage
from email.mime import message

from django.core import mail
from django.shortcuts import render

from .models import Blog, News, mainuser
from agrihubproject import settings

# Create your views here.


def index(request):
    # Get the latest active blog
    latest_blog = Blog.objects.filter(is_active=True).order_by("-published_at")[:2]
    # Get the latest active news
    latest_news = News.objects.filter(is_active=True).order_by("-published_at")[:2]
    
    #  # Get the latest active collaborated company
    # latest_company = Company.objects.filter(is_active=True).order_by("-joined_at")[:2]
    
    # Latest 2 active collaborated companies
    latest_companies = Company.objects.filter(is_active=True).order_by("-joined_at")[:2]

    return render(
        request,
        "index.html",
        {
            "latest_blog": latest_blog,
            "latest_news": latest_news,
            "latest_companies": latest_companies,
        },) 
    # return render(request, 'index.html')




def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


# def subscribe(request):
#     return render(request, 'subscribe.html')




def contactus(request):
    return render(request, 'contactus.html')


def aboutus(request):
    return render(request, 'aboutus.html')

def ourvision(request):
    return render(request, 'ourvision.html')


def ourstory(request):
    return render(request, 'ourstory.html')

def privacypolicy(request):
    return render(request, 'privacypolicy.html')

def termsandconditions(request):
    return render(request, 'terms_conditions.html')


def services(request):
    return render(request, 'services.html')



# def blogs(request):
#     return render(request, 'blogs.html')

# def business_news(request):
#     return render(request, 'business_news.html')

# def companies(request):
#     return render(request, 'companies.html')



import base64

def encode_password(password):
    encoded_password = base64.b64encode(password.encode('utf-8')).decode('utf-8')
    return encoded_password




def decode_password(encoded_password):
    try:
        decoded_password = base64.b64decode(encoded_password).decode('utf-8')
    except UnicodeDecodeError:
        # Handle the case where decoding fails due to invalid characters
        decoded_password = "Unable to decode password"
    return decoded_password
# def register_user(request):



from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import mainuser 
from django.core.mail import EmailMessage
from django.conf import settings

def register_user(request):
    if request.method == 'POST':
        full_name = request.POST['name']
        user_mail = request.POST['email']
        user_password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        if user_password != confirm_password:
            error_message = "Passwords do not match. Please try again."
            return render(request, 'register.html', {'error_message': error_message})
        user_phonenumber = request.POST['phone']
        en_password=encode_password(user_password)
        address = request.POST['address']
        # Check if a user with the same email already exists
        if mainuser.objects.filter(email=user_mail).exists():
            error_message = "A user with this email already exists. Please use a different email."
            return render(request, 'register.html', {'error_message': error_message})
        
        if mainuser.objects.filter(phonenumber=user_phonenumber).exists():
            error_message = "A user with this phone number already exists. Please use a different phone number."
            return render(request, 'register.html', {'error_message': error_message})

        # Create a new User instance
        user = User.objects.create_user(username=full_name, email=user_mail, password=user_password)
        user.first_name = full_name.split(' ')[0]
        user.last_name = full_name.split(' ')[-1]
        user.is_active = False  # User is inactive until email confirmation
        user.save()

        # Create a new MainUser instance
        new_user = mainuser(
          
            full_name=full_name,
            email=user_mail,
            phonenumber=user_phonenumber,
            password=en_password,
            address=address,
            is_active=False
        )
        new_user.save()

        # Send confirmation email
        current_site = get_current_site(request)
        
        message = render_to_string('acc_active_email.html', {
    'user': user,
    'domain': current_site.domain,
    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
    'token': default_token_generator.make_token(user),
})


        email = EmailMultiAlternatives(
    subject='Activate your AgricultureHub account',
    body=message,   # fallback text
    from_email=settings.EMAIL_HOST_USER,
    to=[user_mail]
)

        email.attach_alternative(
    message,
    "text/html"
)

        email.send()
        
        
#         message = render_to_string('acc_active_email.html', {
#     'user': user,
#     'domain': current_site.domain,
#     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#     'token': default_token_generator.make_token(user),
# })


#         email = EmailMessage(
#     'Activate your AgricultureHub account',
#     message,
#     settings.EMAIL_HOST_USER,
#     [user_mail]
# )

#         email.content_subtype = "html"
#         email.send()
        # mail_subject = 'Activate your account.'
#         message = render_to_string('acc_active_email.html', {
#             'user': user,
#             'domain': current_site.domain,
#             'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#             'token': default_token_generator.make_token(user),
#         })
#         # send_mail(mail_subject, message, 'settings.EMAIL_HOST_USER', [user_mail])
#         email_from = settings.EMAIL_HOST_USER
#             # subject = 'Feedback from User'
#         html_message = f"""
#             {message}
#             """
#         email = EmailMessage(
#     subject='Activate your account.',
#     body=message,
#     from_email=settings.EMAIL_HOST_USER,
#     to=[user_mail]
# )

#         email.content_subtype = "html"
#         email.send(fail_silently=False)

        return render(request,'requestdone.html',{'user':new_user})
    else:
        return render(request, 'register.html')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'gotologin.html')
        # return HttpResponse('Thank you for your email confirmation. Your account is now active. You can log in.')
    else:
        return HttpResponse('Activation link is invalid!')













def login_operation(request):
    error_message= None
    
    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_pass = request.POST.get('password')

        try:
            # Retrieve user based on email
            user = mainuser.objects.get( email=user_email)
            
            stored_password= base64.b64decode(user.password).decode('utf-8')
            # stored_password=decode_password(user.user_password)
            print(stored_password)
            if user_pass == stored_password:
                request.session['user_id'] = user.user_id
                # return redirect('home')
                success_message = "Successfully logged in."
                return render(request, 'index.html',{'success_message': success_message, 'username':user.full_name})
            else:
                 error_message= "Invalid password."
                 return render(request, 'login.html', {'error_message': error_message})
                
            # Check if the email and password match
            # if check_password(user_pass, user.user_password):
            #     # Authentication succeeds, store user ID in session and redirect to profile page
            #     request.session['user_id'] = user.user_id
            #     return redirect('home')
            # else:
                # Password does not match, render the login page with error message
                # error_message1 = "Invalid password."
                # return render(request, 'login.html', {'error_message1': error_message1})
          
        except mainuser.DoesNotExist:
            # User with provided email does not exist, render the login page with error message
            error_message= "User with this email does not exist."
            return render(request, 'login.html', {'error_message': error_message})

    else:
        # GET request, render the login page
        return render(request, 'login.html')
















from django.shortcuts import render
from .models import Company

def companies(request):
    # Get all active companies
    companies = Company.objects.filter(is_active=True).order_by("category", "name")
    return render(request, "companies.html", {"companies": companies})







from django.shortcuts import render
from .models import News

def business_news(request):
    # Get search query and filter category from GET params
    search_query = request.GET.get("q", "")
    category_filter = request.GET.get("category", "")

    # Base queryset: only active news
    news_items = News.objects.filter(is_active=True)

    # Apply search filter
    if search_query:
        news_items = news_items.filter(
            title__icontains=search_query
        ) | news_items.filter(
            summary__icontains=search_query
        ) | news_items.filter(
            content__icontains=search_query
        )

    # Apply category filter
    if category_filter:
        news_items = news_items.filter(category=category_filter)

    # Order by latest published
    news_items = news_items.order_by("-published_at")

    return render(
        request,
        "news.html",
        {
            "news_items": news_items,
            "search_query": search_query,
            "category_filter": category_filter,
        },
    )












from django.shortcuts import render
from .models import Blog

def blogs(request):
    # Get search query and category filter from GET params
    search_query = request.GET.get("q", "")
    category_filter = request.GET.get("category", "")

    # Base queryset: only active blogs
    blogs = Blog.objects.filter(is_active=True)

    # Apply search filter (title, summary, content, tags)
    if search_query:
        blogs = blogs.filter(
            title__icontains=search_query
        ) | blogs.filter(
            summary__icontains=search_query
        ) | blogs.filter(
            content__icontains=search_query
        ) | blogs.filter(
            tags__icontains=search_query
        )

    # Apply category filter
    if category_filter:
        blogs = blogs.filter(category=category_filter)

    # Order by latest published
    blogs = blogs.order_by("-published_at")

    return render(
        request,
        "blogs.html",
        {
            "blogs": blogs,
            "search_query": search_query,
            "category_filter": category_filter,
        },
    )







from django.shortcuts import render, get_object_or_404
from .models import Company

def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, "company_detail.html", {"company": company})







def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, "news_detail.html", {"news": news})







def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, "blog_detail.html", {"blog": blog})







from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Subscriber

def subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")

        if email:
            # Check if already subscribed
            if not Subscriber.objects.filter(email=email).exists():
                Subscriber.objects.create(email=email)
                messages.success(request, "Thank you for subscribing!")
            else:
                messages.warning(request, "This email is already subscribed.")
        else:
            messages.error(request, "Please provide a valid email.")

        # Redirect back to homepage or landing page
        return redirect("subscribe")  # replace 'home' with your actual URL name

    # If GET request, just show the subscription form
    return render(request, "subscribe.html")




# def user_logout(request):
#     try:
#         del request.session['user_id']
#     except KeyError:
#         pass
#     return redirect('login')













