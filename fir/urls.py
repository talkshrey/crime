from django.urls import path

from . import views

urlpatterns = [
    path('numbers/', views.HelplineView.as_view(), name="Numbers"),
    path('reports/', views.ReportView.as_view(), name="Reports")
]