from django.conf.urls import include, url

from django.contrib import admin
from ide import views 
urlpatterns = [
    # Examples:
    # url(r'^$', 'semiasm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.editor,name="editor"),
    url(r'^admin/', include(admin.site.urls)),
]
