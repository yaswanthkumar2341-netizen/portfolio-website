from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),  # the portfolio itself
    path('admin/', admin.site.urls),          # view submitted messages at /admin/
    path('api/', include('contact.urls')),    # the contact form API lives under /api/
]
