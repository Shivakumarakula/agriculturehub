

from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

from .utils import notify_all_users    


class mainuser(models.Model):
    user_id = models.AutoField(primary_key=True)

    full_name = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        max_length=150,
        unique=True
    )

    phonenumber = models.CharField(
        max_length=15,
        unique=True
    )

    password = models.CharField(
        max_length=255
    )

    address = models.TextField()

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return self.full_name
    
    
    
    


from django.db import models

class Subscriber(models.Model):
    subscriber_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=150, unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email





from django.db import models

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=100)  # e.g. "Agri-Tech", "Education", "Finance"
    key_services = models.TextField()  # e.g. "Soil testing, crop analytics, training"
    location = models.CharField(max_length=150)  # e.g. "Hyderabad, Telangana"
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to="company_logos/", blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        new = self.pk is None
        super().save(*args, **kwargs)
        if new and self.is_active:
            recipients = list(mainuser.objects.values_list("email", flat=True)) + \
                         list(Subscriber.objects.values_list("email", flat=True))
            link = reverse("company_detail", args=[self.pk])
            notify_all_users(
                subject=f"New Company Collaboration: {self.name}",
                message=self.description[:150],
                link=f"https://http://127.0.0.1:8000/{link}",
                recipients=recipients
            )









from django.db import models

class News(models.Model):
    CATEGORY_CHOICES = [
        ('government', 'Government Schemes'),
        ('market', 'Market Prices'),
        ('technology', 'Agricultural Technology'),
        ('weather', 'Weather Updates'),
        ('crop', 'Crop Management'),
        ('livestock', 'Livestock'),
        ('export', 'Export & Import'),
        ('research', 'Research & Innovation'),
        ('general', 'General Agriculture'),
          ('Business', 'Agriculture Business'),
    ]

    news_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    summary = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to="news_images/", blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='general')
    source = models.CharField(max_length=150, blank=True, null=True)
    source_url = models.URLField(blank=True, null=True)
    views_count = models.PositiveIntegerField(default=0)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
   
    def save(self, *args, **kwargs):
        new = self.pk is None
        super().save(*args, **kwargs)
        if new and self.is_active:
            recipients = list(mainuser.objects.values_list("email", flat=True)) + \
                         list(Subscriber.objects.values_list("email", flat=True))
            link = reverse("news_detail", args=[self.pk])
            notify_all_users(
                subject=f"Latest News: {self.title}",
                message=self.summary[:150],
                link=f"https://http://127.0.0.1:8000/{link}",
                recipients=recipients
            )






from django.db import models

class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('agriculture', 'Agriculture'),
        ('technology', 'Technology'),
        ('education', 'Education'),
        ('market', 'Market'),
        ('research', 'Research'),
        ('general', 'General'),
        ('webinar', 'Webinar'),
        ('success_story', 'Success Story'),
        ('innovation', 'Innovation'),
        ('business', 'Business'),
        ('other', 'Other'),

    ]

    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)                     # Blog headline
    summary = models.TextField()                                 # Short intro/teaser
    content = models.TextField()                                 # Full blog content
    image = models.ImageField(upload_to="blog_images/", blank=True, null=True)  # Optional cover image
    author = models.CharField(max_length=100, blank=True, null=True)            # Admin or contributor
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='general')
    tags = models.CharField(max_length=200, blank=True, null=True)              # Comma-separated tags
    source_url = models.URLField(blank=True, null=True)                         # External reference if any
    views_count = models.PositiveIntegerField(default=0)                        # Track popularity
    published_at = models.DateTimeField(auto_now_add=True)                      # When added
    updated_at = models.DateTimeField(auto_now=True)                            # Last updated
    is_active = models.BooleanField(default=True)                               # Show/hide on site

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        new = self.pk is None
        super().save(*args, **kwargs)
        if new and self.is_active:
            # collect recipients here
            recipients = list(mainuser.objects.values_list("email", flat=True)) + \
                         list(Subscriber.objects.values_list("email", flat=True))
            link = reverse("blog_detail", args=[self.pk])
            notify_all_users(
                subject=f"New Blog: {self.title}",
                message=self.summary[:150],
                link=f"https://http://127.0.0.1:8000/{link}",
                recipients=recipients
            )





# models.py
from django.db import models

class SiteStats(models.Model):
    members = models.PositiveIntegerField(default=0)
    students = models.PositiveIntegerField(default=0)
    partners = models.PositiveIntegerField(default=0)
    linkedin_followers = models.PositiveIntegerField(default=0)
    instagram_followers = models.PositiveIntegerField(default=0)
    youtube_followers = models.PositiveIntegerField(default=0)
    whatsapp_followers = models.PositiveIntegerField(default=0)
    webinars = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Stats (updated {self.updated_at})"





class Job(models.Model):
    company = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    location = models.TextField()
    qualifications = models.TextField(blank=True, null=True)
    experience = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    job_type = models.CharField(
        max_length=50,
        choices=[("FT","Full-time"),("PT","Part-time"),("IN","Internship"),("CT","Contract")],
        default="FT"
    )
    is_urgent = models.BooleanField(default=False)
    eligibility_notes = models.TextField(blank=True, null=True)
    
    package = models.CharField(max_length=100, blank=True, null=True)  # 💰 Salary / CTC
    
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    
    apply_link = models.URLField(blank=True, null=True)
    apply_instructions = models.TextField(blank=True, null=True)
    
    deadline = models.DateField(blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.company} - {self.designation}"
    
    def save(self, *args, **kwargs):
        new = self.pk is None
        super().save(*args, **kwargs)
        if new and self.is_active:
            # collect recipients here
            recipients = list(mainuser.objects.values_list("email", flat=True)) + \
                         list(Subscriber.objects.values_list("email", flat=True))
            link = reverse("jobs_list")
            notify_all_users(
                subject=f"New Job: {self.designation}",
                message=self.description[:150],
                link=f"https://http://127.0.0.1:8000/{link}",
                recipients=recipients
            )



