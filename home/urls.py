from django.urls import path
from .views import StudentList, StudentDetail, SubjectList, SubjectDetail
urlpatterns = [
    path('students/', StudentList.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student_detail'),
    path('subjects/', SubjectList.as_view(), name='subject_list'),
    path('subjects/<int:pk>/', SubjectDetail.as_view(), name='subject_detail'),
]