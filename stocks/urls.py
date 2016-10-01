from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from stocks import views

urlpatterns = [
    url(r'^stocks/$', views.StockList.as_view()),
    url(r'^stocks/([0-9]+)/$', views.StockDetail.as_view()),
    url(r'^stocks/([0-9]+)/latest/', views.StockLatest.as_view()),
    url(r'^stocks/samplepush/', views.StockRefresh.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

