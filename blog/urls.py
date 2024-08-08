from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="blog-index"),
    path('about/',views.about,name="blog-about"),
    path('createpost/',views.createpost,name="blog-post"),
    path('post_details/<int:pk>/',views.post_details,name="blog-post-details"),
    path('post_edit/<int:pk>/',views.post_edit,name="blog-post-edit"),
    path('post_delete/<int:pk>/',views.post_delete,name="blog-post-delete"),
]
