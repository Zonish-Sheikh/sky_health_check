from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_team, name='select_team'),   # First page: Select team and name
    path('choose/', views.choose_team_cards, name='choose_team_cards'),  # Second page: Choose team and cards
    path('view-selected-cards/', views.view_selected_cards, name='view_selected_cards'),  # Third page: View selected cards
]
