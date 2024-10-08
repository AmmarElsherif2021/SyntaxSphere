from django.urls import path
from .views import SignUpView, SignInView, SignOutView, HandlingPostsViewSet, LikesViewSet, CommentsViewSet
from rest_framework.routers import SimpleRouter

post_list = HandlingPostsViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = HandlingPostsViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='sign-up'),
    path('signin/', SignInView.as_view(), name='sign-in'),
    path('signout/', SignOutView.as_view(), name='sign-out'),
    path('posts/', post_list, name='post-list-create'),  # Combined list and create
    path('posts/<uuid:id>/', post_detail, name='post-detail-delete'),  # Combined detail and delete
    path('posts/<uuid:pk>/like/', LikesViewSet.as_view({'post': 'create'}), name='like-post'),
    path('posts/<uuid:pk>/comments/', CommentsViewSet.as_view({'post': 'create', 'get': 'list'}), name='comment-create-list'),  # Allow GET method for comments
    # Corrected to list
     # Corrected typo
]