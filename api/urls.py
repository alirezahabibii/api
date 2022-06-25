from django.urls import path, include
# from .views import ArticleList, ArticleDetail, UserList, UserDetail
from .views import ArticleViewSet, UserViewSet
from rest_framework import routers

app_name = 'api'

router = routers.SimpleRouter()
router.register('articles', ArticleViewSet)
router.register('users', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    # path('', ArticleList.as_view(), name='list'),
    # path('<int:pk>', ArticleDetail.as_view(), name='detail'),
    # path('users/', UserList.as_view(), name='user_list'),
    # path('users/<int:pk>', UserDetail.as_view(), name='user_detail'),
]
