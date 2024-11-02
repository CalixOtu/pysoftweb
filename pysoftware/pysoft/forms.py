from django import forms
from .models import PDFUpload, Question

class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PDFUpload
        fields = ['title', 'pdf_file']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_main', 'a', 'b', 'c', 'd', 'e']
