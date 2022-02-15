from django.urls import path,include

from blog import views

urlpatterns = [
    path('',views.home,name='home'),
    path('blog-list/', views.blog_add, name='blog_list'),  # video_category
    path('list-blog/', views.list_blog.as_view(), name="list_blog"),
    path('blog-list-add/', views.show_now_add, name='blog_list_add'),
]
