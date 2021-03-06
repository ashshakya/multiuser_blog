from django.views.generic import TemplateView
from django.urls import path, include
from django.conf.urls import url
from .views import *


urlpatterns = [
    path('api/', include('blog.apis.urls')),
    path(
        'login',
        CustomLoginView.as_view(),
        name='login'
    ),
    path(
        'post',
        IndexView.as_view(),
        name='post'
    ),
    path(
        'post_list',
        PostListView.as_view(),
        name='post_list'
    ),
    path(
        'post/<int:pk>',
        PostDetailView.as_view(),
        name='post_detail'
    ),
    path(
        'post/<int:pk>/update',
        PostUpdateView.as_view(),
        name='post_update'
    ),
    path(
        '',
        HomeView.as_view(),
        name="home"
    ),
    path(
        'post-approve/<int:pk>',
        PostApprovalView.as_view(),
        name='post_approve'
    ),
    path(
        'post/approve-list',
        PostApprovalListView.as_view(),
        name="post_approve_list"
    ),
    path(
        'post/<int:pk>/delete',
        PostDeleteView.as_view(),
        name="post_delete"
    ),
    url(
        r'post/comment/(?P<pk>[0-9]+)$',
        CommentReplyView.as_view(),
        name="comment_reply"
    ),
    path(
        'post/approved-list/',
        PostApprovedView.as_view(),
        name="user_approved"
    ),
    # path(
    #     'user-info/',
    #     UserInfoView.as_view(),
    #     name="user_info"
    # ),
    # url(
    #     r'user-detail/(?P<slug>[\w.@+-]+)/$',
    #     UserDetailView.as_view(),
    #     name="user_detail"
    # ),
    # path(
    #     'greeting/',
    #     TemplateView.as_view(template_name="blog/greeting.html"),
    #     name='greeting'
    # ),
]
