from django.urls import path

from main import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='posts-list'),
    path('posts/<int:pk>/', views.PostDetailsView.as_view(), name='post-details'),
    path('posts/create/', views.CreatePostView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.UpdatePostView.as_view(), name='update-post'),
    path('post/<int:pk>/delete/', views.DeletePostView.as_view(), name='delete-post'),
]