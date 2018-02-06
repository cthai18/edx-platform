from django.conf import settings
from django.conf.urls import url


urlpatterns = [
    url(
        r'^course_sneakpeek/{}/$'.format(
            settings.COURSE_ID_PATTERN,
        ),
        'student.views.setup_sneakpeek',
        name='course_sneakpeek',
    ),
    url(
        r'^get_analytics_answer_dist/',
        'courseware.views.views.get_analytics_answer_dist',
        name='get_analytics_answer_dist',
    ),
]
if settings.FEATURES.get('ENABLE_SUPERUSER_LOGIN_AS'):
    urlpatterns += [
        url(
            r'^su_login_as/(?P<username>[\w.@+-]+)/?$',
            'student.views.superuser_login_as',
            name='impersonate',
        ),
    ]
