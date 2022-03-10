from django.urls import path,re_path
from . import views

app_name = "expenses"

urlpatterns = [
    path('claim-requests', views.pending_claim_requests, name='pending_claim_requests'),
    path('approved-expenses', views.approved_expense_list, name='approved_expense_list'),
    re_path(r'^approve-claim/(?P<pk>.*)/', views.approve_claim_request ,name='approve_claim_request'),
    re_path(r'^reject-claim/(?P<pk>.*)/', views.reject_claim_request ,name='reject_claim_request'),
    re_path(r'^single-expense-claim/(?P<pk>.*)/', views.expense_claim_single ,name='expense_claim_single'),
    
]
