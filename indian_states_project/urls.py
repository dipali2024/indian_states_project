"""
URL configuration for indian_states_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from indian_states.views import StateListView, StateDetailView, StateCreateView, StateUpdateView, StateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StateListView.as_view(), name='state_list'),
    path('<int:pk>/', StateDetailView.as_view(), name='state_detail'),
    path('add/', StateCreateView.as_view(), name='state_create'),
    path('<int:pk>/update/', StateUpdateView.as_view(), name='state_update'),
    path('<int:pk>/delete/', StateDeleteView.as_view(), name='state_delete'),
]
