from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("add-student/", views.add_student, name="add_student"),
    path("view-student/", views.view_student, name="view_student"),
    path("edit-student/<int:student_id>/", views.edit_student, name="edit_student"),
    path("delete-student/<int:student_id>/", views.delete_student, name="delete_student"),
]
