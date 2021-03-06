from django.views.generic import TemplateView
from django.urls import path, include
from django.conf.urls import url
from .views import *


urlpatterns = [
    path('api/', include('accounts.apis.urls')),
    path(
        'user-info/',
        UserInfoView.as_view(),
        name="user_info"
    ),
    path(
        'user-detail/<int:pk>',
        UserDetailView.as_view(),
        name="user_detail"
    ),
    url(
        r'user-detail/(?P<slug>[\w.@+-]+)/$',
        UserDetailView.as_view(),
        name='user-detail'
    ),
    url(
        r'user-update/(?P<slug>[\w.@+-]+)/$',
        UserUpdateView.as_view(),
        name='user-update'
    ),
    path(
        'greeting/',
        TemplateView.as_view(template_name="blog/greeting.html"),
        name='greeting'
    ),
    url(
        r'skill/(?P<slug>[\w.@+-]+)/$',
        SkillView.as_view(),
        name='skill'
    ),
    path(
        'skill-update/<int:pk>',
        SkillUpdateView.as_view(),
        name='skill-update'
    ),
    url(
        r'qualification/(?P<slug>[\w.@+-]+)/$',
        QualificationView.as_view(),
        name='qualification'
    ),
    url(
        r'experience/(?P<slug>[\w.@+-]+)/$',
        ExperienceView.as_view(),
        name='experience'
    ),
    path(
        'skill/delete/<int:pk>',
        DeleteSkillView.as_view(),
        name="skill_delete"
    ),
    path(
        'qualification/edit/<int:pk>',
        QualificationUpdateView.as_view(),
        name="qualification_edit"
    ),
    path(
        'qualification/delete/<int:pk>',
        QualificationDeleteView.as_view(),
        name="qualification_delete"
    ),
    path(
        'experience/edit/<int:pk>',
        ExperienceUpdateView.as_view(),
        name="experience_edit"
    ),
    path(
        'experience/delete/<int:pk>',
        ExperienceDeleteView.as_view(),
        name="experience_delete"
    ),
]
