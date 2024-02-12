from django.urls import path
from .views import CategoryList, TagList, ItemList, UserRegistration, ItemCreateView, CategoryCreateView, TagCreateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register', UserRegistration.as_view(), name='user-registration'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('tags', TagList.as_view(), name='tag-list'),
    path('items', ItemList.as_view(), name='item-list'),
    path('items/create', ItemCreateView.as_view(), name='item-create'),
    path('categories/create', CategoryCreateView.as_view(), name='category-create'),
    path('tags/create', TagCreateView.as_view(), name='tag-create')
]