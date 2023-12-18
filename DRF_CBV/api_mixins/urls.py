from django.urls import path
from .views import StudentListView, GetStudentUpdateAndDelete
urlpatterns = [
    path('studentlistview/',StudentListView.as_view()),
    path('studentview/<int:pk>/',GetStudentUpdateAndDelete.as_view())
]
