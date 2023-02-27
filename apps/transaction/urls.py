from django.urls import path
from apps.transaction import views

urlpatterns = [
    path("report/", views.ReportView.as_view(), name="report")
]
