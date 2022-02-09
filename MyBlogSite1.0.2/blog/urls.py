from django.urls import path
from .views import Article_View, article_detail, Article_Create_View, Article_Update_View, Delet_Article

urlpatterns=[
    path('',Article_View.as_view(),name='articles'),
    path('article/<int:id>/', article_detail,name='article_detail'),
    path('article/new/', Article_Create_View.as_view(), name='new_article'),
    path('article/<int:pk>/edit', Article_Update_View.as_view(), name='edit_article'),
    path('article/<int:pk>/delete', Delet_Article.as_view(), name='delete'),
]