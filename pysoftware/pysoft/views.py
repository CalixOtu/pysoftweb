from django.shortcuts import render
from django.shortcuts import render, redirect
import pdfplumber
import re
from datetime import date
from django.db import transaction
from .models import *

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import PDFUpload, Question
from .forms import PDFUploadForm, QuestionForm

def home(request):
    return render(request, 'index.html', {})

def dashboard(request):
    pdfs = PDFUpload.objects.all()
    return render(request, 'dashboard.html', {'pdfs': pdfs})

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PDFUploadForm()
    return render(request, 'upload_pdf.html', {'form': form})

def extract_text(request, pdf_id):
    def extract_text_from_pdf(pdf_path):
        """Extracts raw text from each page of the PDF."""
        text_content = []
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text_content.append(page.extract_text())
        return "\n".join(text_content)

    def parse_questions_from_text(text):
        """Parses questions and options from the extracted text."""
        question_blocks = re.split(r"\n\d+\.\s", text)[1:]  # Split by numbered questions

        parsed_questions = []
        for block in question_blocks:
            # Extract the main question
            main_question_match = re.search(r"^(.*?)(?:\n|$)", block)
            main_question = main_question_match.group(1).strip() if main_question_match else None

            # Extract options A through D (and possibly E)
            options = {}
            for option_label in ['A', 'B', 'C', 'D', 'E']:
                option_match = re.search(rf"{option_label}\.\s+(.*?)(?:\n[A-E]\.|$)", block)
                if option_match:
                    options[option_label.lower()] = option_match.group(1).strip()

            parsed_questions.append({
                "question_main": main_question,
                "options": options
            })

        return parsed_questions

    # Run the process
    pdf_path = f'static/img/{get_object_or_404(PDFUpload, id=pdf_id).pdf_file}'
    text = extract_text_from_pdf(pdf_path)
    questions = parse_questions_from_text(text)
    for i in questions:
        Question.objects.create(
            pdf = get_object_or_404(PDFUpload, id=pdf_id),
            question_main=i.get('question_main', 'No name'),
            a= i['options'].get('a', 'No A'),
            b=i['options'].get('b', 'No B'),
            c=i['options'].get('c', 'No C'),
            d=i['options'].get('d', 'No D'),
            e=i['options'].get('e', 'No E'),

        )

    context = {'questions': questions}
    return render(request, 'extracted_questions.html', context)


def extracted_text_list(request):
    texts = Question.objects.all()
    return render(request, 'all_extracted.html', {'texts': texts})

def edit_extracted_text(request, text_id):
    text_obj = get_object_or_404(Question, id=text_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=text_obj)
        if form.is_valid():
            form.save()
            return redirect('extracted_text_list')
    else:
        form = QuestionForm(instance=text_obj)
    return render(request, 'edit_extracted.html', {'form': form})

def delete_extracted_text(request, text_id):
    text_obj = get_object_or_404(Question, id=text_id)
    if request.method == 'POST':
        text_obj.delete()
        return redirect('extracted_text_list')
    return render(request, 'delete_questions.html', {'text_obj': text_obj})


