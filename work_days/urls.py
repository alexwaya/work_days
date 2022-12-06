from django.conf.urls import handler404 #handler500
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('days.urls')),
]

if settings.DEBUG: # new
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns += staticfiles_urlpatterns()

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
#               static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#handler404 = 'leave.views.error_404'

admin.site.site_header = "Work Days Test"
admin.site.site_title = "Admin"
admin.site.index_title = "Work Days Test"