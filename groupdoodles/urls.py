"""
URL configuration for groupdoodles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from groupdoodles_api.views import check_user, UserView, DoodleView, PaletteView, DoodleCollabView, PaletteLikeView
from groupdoodles_api import consumers

router = DefaultRouter(trailing_slash=False)

router.register(r'users', UserView, 'user')
router.register(r'doodles', DoodleView, 'doodle')
router.register(r'palettes', PaletteView, 'palette')
router.register(r'doodle_collabs', DoodleCollabView, 'doodle_collab')
router.register(r'palette_likes', PaletteLikeView, 'palette_like')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('checkuser', check_user, name='check_user'),
]

websocket_urlpatterns = [
    re_path(r'ws/signalling', consumers.SignallingSocketConsumer.as_asgi())
]