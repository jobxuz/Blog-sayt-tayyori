from django.urls import path
from .views import ArticleListView,\
    ArticleUpdateView,\
    ArticleDeleteView,\
    ArticleDetailView,\
    ArticleCreateView,\
    categoria_View,SportArticleDetailView,uzbekiston_categoria_View,UzbArticleDetailView

urlpatterns = [
    path('<int:pk>/edit/',ArticleUpdateView.as_view(),name='articles_edit_url'),
    path('<int:pk>/',ArticleDetailView.as_view(),name='article_detail_url'),
    path('<int:pk>/delete',ArticleDeleteView.as_view(),name='article_delete_url'),
    path('new/',ArticleCreateView.as_view(),name='article_new_url'),
    path('uzbekiston/',uzbekiston_categoria_View,name='uzbekiston_url'),
    path('sport/',categoria_View,name='categoria_url'),
    path('sport/<int:pk>/',SportArticleDetailView,name='sport_detail_url'),
    path('uzb/<int:pk>/',UzbArticleDetailView,name='uzb_detail_url'),
    path('',ArticleListView,name='articles_list'),
]