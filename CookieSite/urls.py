from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^$', include('accounts.urls')),
    url(r'^main/', include('board.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^board/', include('board.urls', namespace='board')),
    url(r'^accounts/', include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
