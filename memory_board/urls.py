from django.urls import path

from .views import MemoriesListView, MemoryDetailView, MemorySearchList, MemoryCreateView, MemoryDeleteView


urlpatterns = [

    path('', MemoriesListView.as_view(), name="memory_list"),
    path('detail/<slug:slug>/', MemoryDetailView.as_view(), name="memory_detail"),
    path('search/', MemorySearchList.as_view(), name="memory_search"),
    path('create/', MemoryCreateView.as_view(), name="memory_create"),
    path('<int:pk>/delete/', MemoryDeleteView.as_view(), name="memory_delete"),

]
