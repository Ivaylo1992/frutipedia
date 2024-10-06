
from django.urls import path, include
from frutipedia.fruit import views

urlpatterns = [
    path('create/', views.CreateFruitView.as_view(), name='create_fruit'),
    path('<int:fruitId>/', include([
        path('details/', views.DetailsFruitView.as_view(), name='details_fruit'),
        path('edit/', views.EditFruitView.as_view(), name='edit_fruit'),
        path('delete/', views.DeleteFruitView.as_view(), name='delete_fruit'),
    ])),
]
