from django.shortcuts import render


def home_view(request):
    notifications = request.user.notifications.filter(is_read=False).order_by("-created_at")
    return render(request, "app/home.html", {"notifications": notifications})
