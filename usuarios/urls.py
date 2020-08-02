from django.urls import path
from usuarios.views import register
from django.views.generic.base import TemplateView

urlpatterns = [

    #path('register/', registrar, name='register'),
    #path('register/', MyFormView, name='register'),
    path('register/', register, name='register'),
    path('', TemplateView.as_view(template_name='index.html'), name='index')

]
