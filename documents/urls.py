from django.urls import path


from . import views

app_name ="documents"

urlpatterns = [
    path("pending_documents", views.pending_documents, name="pending_documents"),
    path("documents_single/<str:pk>/", views.documents_single, name="documents_single"),
    path("accept_documents/<str:pk>/", views.accept_documents, name="accept_documents"),
    path("reject_documents/<str:pk>/", views.reject_documents, name="reject_documents"),
    path("accepted/documents", views.accepted_documents, name="accepted_documents"),
    path("rejected/documents", views.rejected_documents, name="rejected_documents"),
    
]
