# Generated by Django 3.2.7 on 2024-11-01 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_preamble', models.TextField(blank=True, default='', help_text='Any preamble or Information needed for the main question', null=True)),
                ('question_main', models.TextField(blank=True, help_text='Question', max_length=50000, null=True)),
                ('question_main_image', models.ImageField(blank=True, help_text='Upload image in place of Text main question', null=True, upload_to='')),
                ('question_remark_for_reviewer', models.TextField(blank=True, null=True)),
                ('question_image_preamble', models.ImageField(blank=True, null=True, upload_to='')),
                ('question_set_by', models.CharField(max_length=200)),
                ('question_authorised_by', models.CharField(blank=True, max_length=200, null=True)),
                ('question_ready_for_review', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('authorised_date', models.DateTimeField(blank=True, null=True)),
                ('year_of_past_question', models.DateField(blank=True, null=True)),
                ('question_label', models.CharField(blank=True, max_length=1000, null=True)),
                ('a', models.TextField(blank=True, null=True)),
                ('a_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('b', models.TextField()),
                ('b_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('c', models.TextField()),
                ('c_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('d', models.TextField()),
                ('d_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('e', models.TextField(blank=True, null=True)),
                ('e_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('hidden', models.BooleanField(default=False)),
                ('explanation', models.TextField(blank=True, null=True)),
                ('assessment_weight', models.PositiveSmallIntegerField(default=0)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
