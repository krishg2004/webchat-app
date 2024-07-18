
# from django.contrib import admin
# from django.urls import path, include
# # from chat.views import index
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('chat/', include('chat.urls',namespace='chat')),
# ]

from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('chat/', include('chat.urls',namespace='chat')),
    path('admin/', admin.site.urls),

]
