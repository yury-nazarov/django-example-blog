from django.urls import path
from . import views

# Пространство имен позволяет обращатся к url по схеме: {app_name:name}
app_name = 'blog'

# Django просматривает все url и останавливается на том,
# который первый подходит под шаблон
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>',
         views.post_detail,
         name='post_detail'),
]



# Docs
# path & re_path (https://docs.djangoproject.com/en/5.1/ref/urls/#django.urls.re_path) для определяния шаблонов url-адресов
# regexp: https://docs.python.org/3/howto/regex.html
# Все возможные конверторы путей можно посмотреть тут https://docs.djangoproject.com/en/5.1/topics/http/urls/#path-converters