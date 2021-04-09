from django.urls import path

from . import views

urlpatterns = [
    path('article/', views.ListArticle.as_view()),
    path('article/<int:pk>/', views.DetailArticle.as_view()),
    path('cards/', views.ListCards.as_view()),
    path('cards/<int:pk>/', views.DetailCards.as_view()),
    path('MarketSegments/', views.ListMarketSegments.as_view()),
    path('MarketSegments/<int:pk>/', views.DetailMarketSegments.as_view()),
    path('project/', views.ListProject.as_view()),
    path('project/<int:pk>/', views.DetailProject.as_view()),

]