from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'users_example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^signup/$', 'users_example.views.signup_view'),
    url(r'^users/(?P<user_id>\d+)/edit/$', 'users_example.views.edit_user_view'),

    url(r'^admin/', include(admin.site.urls)),
)
