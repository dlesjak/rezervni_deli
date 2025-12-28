from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'spareparts', views.SparePartViewSet)

# app_name = 'polls'
# urlpatterns = [
#     path("", views.IndexView.as_view(), name="index"),
# ]
app_name = 'rd'
urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.PartsView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.PartUpdateView.as_view(), name="part_edit"),
    path("<int:pk>/delete/", views.PartDeleteView.as_view(), name="part_delete"),
    path("create/", views.create_view, name="part_create"),
    path("api/", include(router.urls)),
]
