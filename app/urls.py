from django.contrib.auth import views as django_auth_views
from django.urls import path, reverse_lazy

from . import views

app_name = "app"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("profile/", views.profile_view, name="profile"),
    path("edit_profile/", views.edit_profile_view, name="edit_profile"),
    path("projects/", views.projects_view, name="projects"),
    path("projects/<int:project_id>/", views.project_view, name="project"),
    path("projects/<int:project_id>/edit/", views.edit_project_view, name="edit_project"),
    path("projects/<int:project_id>/create-task", views.create_task_view, name="create_task"),
    path("projects/<int:project_id>/add-member", views.add_member_view, name="add_member"),
    path("tasks/", views.tasks_view, name="tasks"),
    path("tasks/<int:task_id>/", views.task_view, name="task"),
    path("tasks/<int:task_id>/edit/", views.edit_task_view, name="edit_task"),
    path("tasks/<int:task_id>/create-comment", views.create_comment_view, name="create_comment"),
    path("tasks/<int:task_id>/comment/<int:comment_id>/delete/", views.delete_comment_view, name="delete_comment"),
    path("notifications/<int:notification_id>/read/", views.mark_notification_read_view, name="mark_notification_read"),
    path(
        "password_reset/",
        django_auth_views.PasswordResetView.as_view(
            template_name="app/registration/password_reset.html",
            email_template_name="app/registration/password_reset_email.html",
            success_url=reverse_lazy("app:password_reset_done"),
            extra_email_context={"namespace": "app"},  # <-- pass namespace
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        django_auth_views.PasswordResetDoneView.as_view(
            template_name="app/registration/password_reset_done.html",
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        django_auth_views.PasswordResetConfirmView.as_view(
            template_name="app/registration/password_reset_confirm.html",
            success_url=reverse_lazy("app:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        django_auth_views.PasswordResetCompleteView.as_view(
            template_name="app/registration/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
