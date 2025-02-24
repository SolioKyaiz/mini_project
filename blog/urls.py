from django.urls import path
from blog.views import category, post, comment, like_dislike, bookmark
from blog.views.category import category_detail, category_list
from blog.views.post import post_list, post_edit,post_detail,post_create,post_delete

app_name = 'blog'

urlpatterns = [
    #Categories
    path('categories/',category.category_list, name = 'category-list'),
    path('categories/<int:pk>/',category.category_detail, name = 'category-detail'),

    #Posts
    path('posts/',post.post_list, name = 'post-list'),
    path('posts<int:pk>/',post.post_detail, name = 'post-detail'),
    path('posts/create/', post.post_create,name = 'post-create'),
    path('post/<int:pk>/edit/', post.post_edit, name = 'post-edit'),
    path('post/<int:pk>/delete/', post.post_delete, name = 'post-delete'),

    #Comments
    path('posts/<int:pk>/comment/add/', comment.add_comment, name = 'comment-add'),
    path('comments/<int:pk>/delete/delete/', comment.delete_comment, name = 'comment-delete'),

    #Likes and Dislikes and bookmarks
    path('posts/<int:pk>/like/', like_dislike.toggle_like, name = 'toggle-like'),
    path('posts/<int:pk>/dislike/', like_dislike.toggle_dislike, name = 'toggle-dislike'),
    path('posts/<int:pk>/bookmark/', bookmark.toggle_bookmark, name = 'toggle-bookmark'),
]