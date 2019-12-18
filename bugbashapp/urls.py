"""bugbashapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from bugreport import views as Report
from accounts import views as user_view
from leaderboard import views as lb

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_view.login_view, name='landing'),
    path('register/', user_view.register, name="register"),
    path('login/', user_view.login_view, name="login_view"),
    path('home/', Report.create_bashing_session, name="home"),
    path('leaderboard/', lb.leaderboard_list, name="leaderboard_view"),
    path('bugreport/', Report.create_user_bug_view, name="bug_report"),
    path('bugreport/create_report/', Report.create_report, name='ajax_bugreport_create'),
    path('bugreport/update/',  Report.update_bug, name='ajax_bugreport_update'),
    path('bugreport/delete/',  Report.delete_user_bug, name='ajax_bugreport_delete'),
    path('logout/', user_view.logout_view, name="logout_view")
]
