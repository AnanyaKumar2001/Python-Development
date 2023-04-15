from django.urls.conf import path

from . import views


urlpatterns = [
    path('<int:book_id>', views.detail, name='detail')
]
