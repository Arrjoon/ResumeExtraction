from django.shortcuts import render
import csv
from django.http import HttpResponse
from myapp.models import Job_Description
# Create your views here.
from django.shortcuts import render
from django.core.files.storage import default_storage
from .forms import JobDescriptionForm
from PyPDF2 import PdfReader
import docx
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ''
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = '\n'.join([para.text for para in doc.paragraphs])
    return text

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()
    return text

def extract_features(texts):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    return tfidf_matrix, vectorizer

def calculate_similarity(job_desc_features, resumes_features):
    similarity_scores = cosine_similarity(job_desc_features, resumes_features)
    return similarity_scores.flatten()

def rank_resumes(job_desc, resumes):
    all_texts = [job_desc] + resumes
    tfidf_matrix, vectorizer = extract_features(all_texts)
    
    job_desc_features = tfidf_matrix[0:1]
    resumes_features = tfidf_matrix[1:]
    
    similarity_scores = calculate_similarity(job_desc_features, resumes_features)
    ranked_resumes = sorted(zip(resumes, similarity_scores), key=lambda x: x[1], reverse=True)
    
    return ranked_resumes

def ranking_resume(request):
    if request.method == 'POST':
        form = JobDescriptionForm(request.POST, request.FILES)
        if form.is_valid():
            job_desc = form.cleaned_data['job_description']
            resume_files = request.FILES.getlist('resumes')
            
            resumes_texts = []
            for resume_file in resume_files:
                if resume_file.name.endswith('.pdf'):
                    text = extract_text_from_pdf(resume_file)
                elif resume_file.name.endswith('.docx'):
                    text = extract_text_from_docx(resume_file)
                else:
                    continue
                resumes_texts.append(clean_text(text))
            
            job_desc = clean_text(job_desc)
            ranked_resumes = rank_resumes(job_desc, resumes_texts)
            
            return render(request, 'matching_score.html', {'ranked_resumes': ranked_resumes})
    else:
        form = JobDescriptionForm()
    
    return render(request, 'job_description.html', {'form': form})



def export_jobs_to_csv(request):
    # Define the HTTP response with the appropriate CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="job_descriptions.csv"'

    # Create a CSV writer
    writer = csv.writer(response)
    fieldnames = [
        'job_role', 
        'company_description', 
        'role_description', 
        'qualification', 
        'degree', 
        'experience', 
        'skills'
    ]

    # Write the header row
    writer.writerow(fieldnames)

    # Write job description data
    jobs = Job_Description.objects.all()
    for job in jobs:
        writer.writerow([
            job.job_role,
            job.company_description,
            job.role_description,
            job.qualification,
            job.degree,
            job.experience,
            job.skills
        ])

    return response

