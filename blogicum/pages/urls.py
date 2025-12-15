from django.urls import path
from .views import AboutView, RulesView, PageCreateView, PageUpdateView

app_name = 'pages'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('rules/', RulesView.as_view(), name='rules'),
    # Admin-only page management (CBV)
    path('create/', PageCreateView.as_view(), name='page_create'),
    path('<slug:slug>/edit/', PageUpdateView.as_view(), name='page_edit'),
    # Optional detail view for pages created in DB (keeps existing addresses unchanged)
    path('<slug:slug>/', AboutView.as_view(), name='page_detail'),
]
