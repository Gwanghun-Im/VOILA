from django.urls import path
from . import views


urlpatterns = [
    path('', views.getMovie),
    path('<int:pk>/', views.movie),
    path('likemovie/<int:pk>/',views.like_movie),
    path('<int:pk>/<int:review_pk>/', views.review),
    path('like/<int:review_pk>/',views.like_review),
    path('<int:pk>/<int:review_pk>/<int:comment_pk>/', views.comment),
    path('search/<str:title>',views.search),
    path('detail/<int:movie_id>', views.detail),
    path('word/<int:user_pk>',views.word),
    path('game/',views.game)
]