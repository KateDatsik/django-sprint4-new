from django.urls import include, path

from blog import views

app_name = 'blog'

profile_urlpatterns = [
    path(
        'edit/',
        views.ProfileUpdateView.as_view(),
        name='edit_profile',
    ),
    path(
        '<username>/',
        views.ProfileListView.as_view(),
        name='profile',
    ),
]

post_urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='create_post'),
    path(
        '<post_id>/',
        views.PostDetailView.as_view(),
        name='post_detail',
    ),
    path(
        '<post_id>/edit/',
        views.PostUpdateView.as_view(),
        name='edit_post',
    ),
    path(
        '<post_id>/delete/',
        views.PostDeleteView.as_view(),
        name='delete_post',
    ),
    path(
        '<post_id>/comment/',
        views.CommentCreateView.as_view(),
        name='add_comment',
    ),
    path(
        '<post_id>/edit_comment/<comment_id>/',
        views.CommentUpdateView.as_view(),
        name='edit_comment',
    ),
    path(
        '<post_id>/delete_comment/<comment_id>/',
        views.CommentDeleteView.as_view(),
        name='delete_comment',
    ),
]

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('profile/', include(profile_urlpatterns)),
    path('posts/', include(post_urlpatterns)),
    path(
        'category/<slug:category_slug>/',
        views.CategoryPostsListView.as_view(),
        name='category_posts',
    ),
]
