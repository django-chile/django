from django.conf.urls import url
from ..adopcion.views import index_adopcion


urlpatterns = [
     url(r'^$', index_adopcion),
]
