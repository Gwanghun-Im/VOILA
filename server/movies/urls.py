from django.urls import path
from . import views


urlpatterns = [
    path('', views.getMovie),
    path('<int:pk>/', views.movie),
    path('<int:pk>/<int:review_pk>/', views.review),
    path('<int:pk>/<int:review_pk>/<int:comment_pk>/', views.comment),
    path('search/<str:title>',views.search),
    path('detail/<int:movie_id>', views.detail),
    path('word/<int:user_pk>',views.word)
]