from django.urls import path
from .views import TaggedItemView, TaggedItemDetailView


urlpatterns = [
    path('<slug:tag>', TaggedItemDetailView.as_view()),
    path('', TaggedItemView.as_view()),
]
