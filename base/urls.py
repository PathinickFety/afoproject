from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Participant URLs
    path('participants/', views.participant_list, name='participant_list'),
    path('participants/<int:pk>/', views.participant_detail, name='participant_detail'),
    path('participants/new/', views.participant_create, name='participant_create'),
    path('participants/<int:pk>/edit/', views.participant_update, name='participant_update'),
    path('participants/<int:pk>/delete/', views.participant_delete, name='participant_delete'),
    
    # Team URLs
    path('teams/', views.team_list, name='team_list'),
    path('teams/new/', views.team_create, name='team_create'),
    
    # Judge URLs
    path('judges/', views.judge_list, name='judge_list'),
    
    # Battle URLs
    path('', views.battle_list, name='battle_list'),
    path('battles/<int:pk>/', views.battle_detail, name='battle_detail'),
    path('battles/<int:battle_id>/vote/', views.judge_vote, name='judge_vote'),
    path('battle/create/', views.battle_create, name='battle_create'),
    path('battle/<int:pk>/update/', views.battle_update, name='battle_update'),
    path('battle/<int:pk>/delete/', views.battle_delete, name='battle_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)