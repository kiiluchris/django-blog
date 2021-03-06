from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

import blog.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'jester.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    # url(r'^$', blog.views.index, name = "index"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include("blog.urls", namespace="blog")),
    url(r'^', include("personalsite.urls", namespace="personalsite")),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	