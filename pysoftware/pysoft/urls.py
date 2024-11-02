from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload-pdf/', views.upload_pdf, name='upload_pdf'),
    path('extract-text/<int:pdf_id>/', views.extract_text, name='extract_text'),
    path('extracted-texts/', views.extracted_text_list, name='extracted_text_list'),
    path('edit-extracted-text/<int:text_id>/', views.edit_extracted_text, name='edit_extracted_text'),
    path('delete-extracted-text/<int:text_id>/', views.delete_extracted_text, name='delete_extracted_text'),
]
