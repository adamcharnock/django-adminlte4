from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name='adminlte/index.html'), name='home'),
    path('login/', TemplateView.as_view(template_name='adminlte/login.html'), name='login'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]