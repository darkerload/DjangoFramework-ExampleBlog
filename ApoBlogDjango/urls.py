from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ApoBlogDjango.views.index'),
    #url(r'^blog/', include('blog.urls')),
    url(r'^index/', 'ApoBlogDjango.views.index'),
    url(r'^detailView/', 'ApoBlogDjango.views.detailView', name='detailView'),
    url(r'^comments/', 'ApoBlogDjango.views.comments'),
    url(r'^leaveComment/', 'ApoBlogDjango.views.leaveComment'),
    url(r'^admin/', include(admin.site.urls)),

)
