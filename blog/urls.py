from django.urls import path # type: ignore
from django.conf.urls.static import static # type: ignore
from blog import views
from django_portafolio import settings # type: ignore


app_name='blog' # para referenciar a todas las urls del blog

urlpatterns = [
    path('', views.posts, name='posts'),
    path('<int:post_id>/',views.post_detail,name='post_detail'),#<int:post_id>
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
