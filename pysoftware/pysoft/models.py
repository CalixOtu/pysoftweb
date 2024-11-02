from django.db import models
questions_image_storage_path = ''

# Create your models here.
from django.db import models

class PDFUpload(models.Model):
   title = models.CharField(max_length=200)
   pdf_file = models.FileField(upload_to='pdfs/')
   uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

   def __str__(self):
       return self.title

class Question(models.Model):
   pdf = models.ForeignKey(PDFUpload, on_delete=models.CASCADE, related_name='extracted_texts', blank=True, null=True)
   question_preamble = models.TextField(help_text="Any preamble or Information needed for the main question", default="", null=True, blank=True)
   question_main = models.TextField(help_text="Question", null=True, blank=True, max_length=50000)
   question_main_image = models.ImageField(upload_to=questions_image_storage_path, null=True, blank=True, help_text="Upload image in place of Text main question")
   question_remark_for_reviewer = models.TextField(null=True, blank=True)
   question_image_preamble = models.ImageField(upload_to=questions_image_storage_path, null=True, blank=True )
   question_set_by = models.CharField(max_length=200, null=False, blank=False)
   question_authorised_by = models.CharField(max_length=200, null=True, blank=True)
   question_ready_for_review = models.BooleanField(default=False)
   created = models.DateTimeField(auto_now_add=True)
   authorised_date = models.DateTimeField(null=True, blank=True)
   year_of_past_question = models.DateField(null=True, blank=True)
   question_label = models.CharField(max_length=1000, blank=True, null=True)
   a = models.TextField(null=True, blank=True)
   a_image = models.ImageField(upload_to=questions_image_storage_path, null=True, blank=True)
   b = models.TextField(null=False, blank=False)
   b_image = models.ImageField(upload_to=questions_image_storage_path, null=True, blank=True)
   c = models.TextField(null=False, blank=False)
   c_image = models.ImageField(upload_to=questions_image_storage_path, null=True, blank=True)
   d = models.TextField(null=False, blank=False)
   d_image = models.ImageField(upload_to=questions_image_storage_path, null=True, blank=True)
   e = models.TextField(null=True, blank=True)
   e_image = models.ImageField(upload_to=questions_image_storage_path, null=True, blank=True)
   hidden = models.BooleanField(default=False, null=False, blank=False)
   explanation = models.TextField(null=True, blank=True)
   objects = models.Manager()
   assessment_weight = models.PositiveSmallIntegerField(default=0)
   modified = models.DateTimeField(auto_now=True)
   created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

   def __str__(self):
        return f"Extracted Questions for {self.pdf.title}"


