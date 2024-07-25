from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

import users.urls, chatrooms.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(users.urls)),
    path('chatrooms/', include('chatrooms.urls')),
] + debug_toolbar_urls()
