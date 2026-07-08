from django.contrib import admin

# Register your models here.



# from django.contrib import admin
# from .models import mainuser

# @admin.register(mainuser)
# class MainUserAdmin(admin.ModelAdmin):
#     list_display = ("user_id", "full_name", "email", "phonenumber", "is_active", "created_at")
#     search_fields = ("full_name", "email", "phonenumber")
#     list_filter = ("is_active", "created_at")
#     ordering = ("-created_at",)

#     # Simple form layout
#     fields = ("full_name", "email", "phonenumber", "password", "address", "is_active")




# @admin.register(mainuser)
# class MainUserAdmin(admin.ModelAdmin):
#     # Fields shown in the list view
#     list_display = ("user_id", "full_name", "email", "phonenumber", "is_active", "created_at")
    
#     # Add search bar
#     search_fields = ("full_name", "email", "phonenumber")
    
#     # Filters in the right sidebar
#     list_filter = ("is_active", "created_at")
    
#     # Default ordering
#     ordering = ("-created_at",)

#     # Fields editable in the form
#     fields = ("full_name", "email", "phonenumber", "password", "address", "is_active")
    
#     # Group fields into sections (optional)
#     fieldsets = (
#         ("Personal Info", {
#             "fields": ("full_name", "email", "phonenumber", "address")
#         }),
#         ("Account Settings", {
#             "fields": ("password", "is_active")
#         }),
#     )



from django.contrib import admin
from .models import mainuser

@admin.register(mainuser)
class MainUserAdmin(admin.ModelAdmin):
    # Show these fields in the list view
    list_display = ("user_id", "full_name", "email", "phonenumber", "is_active", "created_at")

    # Add search bar and filters
    search_fields = ("full_name", "email", "phonenumber")
    list_filter = ("is_active", "created_at")
    ordering = ("-created_at",)

    # ✅ Fields editable in the admin form
    # Include everything you want admins to change
    fields = ("full_name", "email", "phonenumber", "password", "address", "is_active")

    # ✅ Make timestamps read-only (so they show but can’t be edited)
    readonly_fields = ("created_at", "updated_at")

    # Optional: bulk actions
    actions = ["activate_users", "deactivate_users"]

    def activate_users(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, "Selected users have been activated.")

    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, "Selected users have been deactivated.")

    activate_users.short_description = "Activate selected users"
    deactivate_users.short_description = "Deactivate selected users"




# from django.contrib import admin
# from .models import Company

# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     # Show these fields in the list view
#     list_display = (
#         "company_id",
#         "name",
#         "category",
#         "location",
#         "is_active",
#         "joined_at",
#         "updated_at",
#     )

#     # Add search bar
#     search_fields = ("name", "category", "key_services", "location", "website")

#     # Filters in the right sidebar
#     list_filter = ("category", "is_active", "joined_at")

#     # Default ordering
#     ordering = ("-joined_at",)

#     # Fields editable in the admin form
#     fields = (
#         "name",
#         "description",
#         "category",
#         "key_services",
#         "location",
#         "website",
#         "logo",
#         "is_active",
#     )

#     # Read-only fields (timestamps should not be editable)
#     readonly_fields = ("joined_at", "updated_at")



# from django.contrib import admin
# from .models import Company


# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):

#     list_display = (
#         "company_id",
#         "name",
#         "description",
#         "category",
#         "key_services",
#         "location",
#         "website",
#         "logo",
#         "updated_at",
#         "is_active",
#         "joined_at",
#     )

#     search_fields = (
#         "name",
#         "category",
#         "key_services",
#         "location",
#     )

#     list_filter = (
#         "category",
#         "is_active",
#         "joined_at",
#     )

#     ordering = ("-joined_at",)

#     list_editable = (
        
#         "name",
#         "description",
#         "category",
#         "key_services",
#         "location",
#         "website",
#         "logo",
      
#         "is_active",
       
        
#     )

#     readonly_fields = (
#         "joined_at",
#         "updated_at",
#     )

#     actions = [
#         "activate_companies",
#         "deactivate_companies",
#     ]

#     def activate_companies(self, request, queryset):
#         queryset.update(is_active=True)

#     activate_companies.short_description = "Activate selected companies"

#     def deactivate_companies(self, request, queryset):
#         queryset.update(is_active=False)

#     deactivate_companies.short_description = "Deactivate selected companies"



# from django.contrib import admin
# from django.utils.html import format_html
# from .models import Company


# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):

#     list_display = (
#         "company_id",
#         "logo_tag",       # ✅ custom method to show logo
#         "name",
#         "description",
#         "category",
#         "key_services",
#         "location",
#         "website",
#         "updated_at",
#         "is_active",
#         "joined_at",
#     )

#     search_fields = (
#         "name",
#         "category",
#         "key_services",
#         "location",
#     )

#     list_filter = (
#         "category",
#         "is_active",
#         "joined_at",
#     )

#     ordering = ("-joined_at",)

#     list_editable = (
#         "name",
#         "description",
#         "category",
#         "key_services",
#         "location",
#         "website",
#         "is_active",
#     )

#     readonly_fields = (
#         "joined_at",
#         "updated_at",
#     )

#     actions = [
#         "activate_companies",
#         "deactivate_companies",
#     ]

#     def activate_companies(self, request, queryset):
#         queryset.update(is_active=True)

#     activate_companies.short_description = "Activate selected companies"

#     def deactivate_companies(self, request, queryset):
#         queryset.update(is_active=False)

#     deactivate_companies.short_description = "Deactivate selected companies"

#     # ✅ Custom method to render logo in list view
#     def logo_tag(self, obj):
#         if obj.logo:
#             return format_html('<img src="static/{}" style="height:50px;width:auto;" />', obj.logo.url)
#         return "No Logo"

#     logo_tag.short_description = "Logo"







from django.templatetags.static import static





from django.contrib import admin
from django.utils.html import format_html
from django.templatetags.static import static
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):

    list_display = (
        "company_id",
        "logo",       # ✅ custom method to show logo
        "name",
        "description",
        "category",
        "key_services",
        "location",
        "website",
        "updated_at",
        "is_active",
        "joined_at",
    )

    search_fields = ("name", "category", "key_services", "location")
    list_filter = ("category", "is_active", "joined_at")
    ordering = ("-joined_at",)

    list_editable = (
        "name",
        "description",
        "category",
        "key_services",
        "location",
        "website",
        "logo",
        "is_active",
    )

    readonly_fields = ("joined_at", "updated_at")

    actions = ["activate_companies", "deactivate_companies"]

    def activate_companies(self, request, queryset):
        queryset.update(is_active=True)
    activate_companies.short_description = "Activate selected companies"

    def deactivate_companies(self, request, queryset):
        queryset.update(is_active=False)
    deactivate_companies.short_description = "Deactivate selected companies"

    # ✅ Custom method to render logo from static folder
    def logo_tag(self, obj):
        if obj.logo:  # if using ImageField upload
            return format_html('<img src="{}" style="height:50px;width:auto;" />', obj.logo.url)
        else:  # fallback to static folder
            logo_url = static(f"company_logs/default.png")  # put a default logo in static/company_logs/
            return format_html('<img src="{}" style="height:50px;width:auto;" />', logo_url)

    logo_tag.short_description = "Logo"













from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    # List View
    list_display = (
        "news_id",
        "title",
        "summary",
        "content",
        "image",
        "category",
        "author",
        "source",
        "source_url",
        "views_count",
        "is_active",
        "published_at",
        "updated_at",
    )

    # Search
    search_fields = (
        "title",
        "summary",
        "content",
        "author",
        "source",
    )

    # Filters
    list_filter = (
        "category",
        "is_active",
        "published_at",
    )

    # Ordering
    ordering = (
        "-published_at",
    )

    # Editable directly from list page
    list_editable = (
        
        "title",
        "summary",
        "content",
        "image",
        "category",
        "author",
        "source",
        "source_url",
        "views_count",
        "is_active",
        
    )

    # Read-only fields
    readonly_fields = (
        "views_count",
        "published_at",
        "updated_at",
    )

    # Admin form fields
    fields = (
        "title",
        "summary",
        "content",
        "image",
        "author",
        "category",
        "source",
        "source_url",
        "is_active",
        "views_count",
        "published_at",
        "updated_at",
    )

    # Custom Actions
    actions = [
        "activate_news",
        "deactivate_news",
    ]

    def activate_news(self, request, queryset):
        queryset.update(is_active=True)

    activate_news.short_description = "Activate selected news"

    def deactivate_news(self, request, queryset):
        queryset.update(is_active=False)

    deactivate_news.short_description = "Deactivate selected news"
    
    
    
    
    
    
    
    
    
    
    
    
    
    from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    # Columns shown in admin list page
    list_display = (
        "blog_id",
        "title",
        "summary",
        "content",
        "image",
        "category",
        "author",
        "tags",
        "source_url",
        "views_count",
        "is_active",
        "published_at",
        "updated_at",
    )

    # Search functionality
    search_fields = (
        "title",
        "summary",
        "content",
        "author",
        "tags",
    )

    # Filters
    list_filter = (
        "category",
        "is_active",
        "published_at",
    )

    # Default ordering
    ordering = (
        "-published_at",
    )

    # Editable directly from list page
    list_editable = (
        "is_active",
        "title",
        "summary",
        "content",
        "image",
        "category",
        "author",
        "tags",
        "source_url",
        "views_count",
    )

    # Read-only fields
    readonly_fields = (
        "published_at",
        "updated_at",
    )

    # Blog form fields
    fields = (
        "title",
        "summary",
        "content",
        "image",
        "author",
        "category",
        "tags",
        "source_url",
        "is_active",
        "views_count",
        "published_at",
        "updated_at",
    )

    # Custom Actions
    actions = [
        "activate_blogs",
        "deactivate_blogs",
    ]

    def activate_blogs(self, request, queryset):
        queryset.update(is_active=True)

    activate_blogs.short_description = "Activate selected blogs"

    def deactivate_blogs(self, request, queryset):
        queryset.update(is_active=False)

    deactivate_blogs.short_description = "Deactivate selected blogs"
    
    
    



# admin.py
from django.contrib import admin
from .models import SiteStats

admin.site.register(SiteStats)






from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("company", "designation", "location", "job_type", "package", "is_urgent", "deadline", "posted_at", "is_active")
    list_filter = ("job_type", "is_urgent", "deadline")
    search_fields = ("company", "designation", "location")

    actions = ["activate_jobs", "deactivate_jobs"]

    def activate_jobs(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, "Selected jobs have been activated.")
    activate_jobs.short_description = "Activate selected jobs"

    def deactivate_jobs(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, "Selected jobs have been deactivated.")
    deactivate_jobs.short_description = "Deactivate selected jobs"





# admin.py
from django.contrib import admin
from .models import Subscriber

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "subscribed_at")   # columns shown in admin list
    search_fields = ("email",)                  # search by email
    ordering = ("-subscribed_at",)              # newest first




