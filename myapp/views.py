from django.shortcuts import render,HttpResponse
from pdfminer.high_level import extract_text
from .forms import CustomUploadFileForm
from .models import Resume_Description,Job_Description
import os
import re
#machine learning module imported
import spacy
from spacy_transformers import Transformer
from tqdm import tqdm
import json
from .nlp_utils import SpaCyNER


# Create your views here.

def ner_view(input_text):  
        spacy_ner = SpaCyNER()
        entities = spacy_ner.predict(input_text)
        return entities


def handle_uploaded_file(f):
    upload_dir = 'uploads/'
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    file_path = os.path.join(upload_dir, f.name)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path
def extract_contact_number_from_resume(text):
    contact_number = None

    # Use regex pattern to find a potential contact number
    pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
    match = re.search(pattern, text)
    if match:
        contact_number = match.group()

    return contact_number

def extract_email_from_resume(text):
    email = None

    # Use regex pattern to find a potential email address
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    match = re.search(pattern, text)
    if match:
        email = match.group()
    return email

def extract_linkedin_id(text):
    pattern = r'(?:https?:\/\/)?(?:www\.)?linkedin\.com\/(?:in|profile)\/([\w-]+)'
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    else:
        return None
def extraction_to_text(request):
    if request.method == 'POST':
        form = CustomUploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = handle_uploaded_file(request.FILES['file'])
            # Here you can pass the file_path to any function that needs it
            text=extract_text(file_path)
            # Clean the text by removing \n, \t, and extra spaces
            cleaned_text = re.sub(r'\s+', ' ', text).strip()
            email = extract_email_from_resume(cleaned_text)
            contact = extract_contact_number_from_resume(cleaned_text)
            # linkedin = extract_linkedin_id(text)
            data={'email':email,'contact':contact}
            # return HttpResponse(f'File uploaded successfully: {text}')
            ner_view(cleaned_text)
             # Add entities to the data dictionary
            entities = ner_view(text)
            print(entities)
            print(type(entities))

            #adding to database
            
            try:
            # Initialize variables to store extracted information
                name = 'Unknown'
                location = 'Unknown'
                email = 'Unknown'
                designation='Unknown'
                experience = 'Unknown'
                companies_worked_at = 'Unknown'
                college_name = 'Unknown'
                graduation_year = 'Unknown'
                degree = 'Unknown'

                skills = []

                # Iterate through each entity dictionary
                for entity in entities:
                    if entity['label'] == 'Name':
                        name = entity['text']
                    elif entity['label'] == 'Location':
                        location = entity['text']
                    elif entity['label'] == 'Email Address':
                        email = entity['text']
                    elif entity['label'] == 'Years of Experience':
                        experience = entity['text']
                    elif entity['label'] == 'Degree':
                        degree = entity['text']
                    elif entity['label'] == 'Companies worked at':
                        companies_worked_at=entity['text']
                    elif entity['label'] == 'College Name':
                        college_name = entity['text']
                    elif entity['label'] == 'Graduation Year':
                        graduation_year = entity['text']
                    elif entity['label'] == 'Designation':
                        designation=entity['text']
                    elif entity['label'] == 'Skills':
                        skills.extend([skill.strip() for skill in entity['text'].split(',') if skill.strip()])

                    # Convert skills list to a comma-separated string
                skills_str = ', '.join(skills)


                    # Create and save a new Profile instance
                profile = Resume_Description(
                    name=name,
                    designation=designation,
                    location=location,
                    email_address=email,
                    company_working_at =companies_worked_at,
                    degree=degree,
                    college_name=college_name,
                    graduation_year=graduation_year,
                    experience=experience,
                    skills=skills
                    )
                profile.save()
            except Exception as e:
                # Handle the exception here
                return HttpResponse(f'Error occurred: {str(e)}')
            data = {
                'email': email,
                'contact': contact,
                'entities': entities
            }

            return render(request,'upload.html',{'data':data})
    else:
        form = CustomUploadFileForm()
    return render(request, 'upload.html', {'form': form})

def doc_pdf_converter(request):
    # Extract text from the PDF
    pdf_path = '/content/cv_arjun_nepali.pdf'  # Replace with your PDF file path


def upload_file(request):
    if request.method == 'POST':
        form = CustomUploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = handle_uploaded_file(request.FILES['file'])
            # Here you can pass the file_path to any function that needs it
            text=extract_text(file_path)
            # return HttpResponse(f'File uploaded successfully: {text}')
            return render(request,'converted_text.html',{'text':text})
    else:
        form = CustomUploadFileForm()
    return render(request, 'upload.html', {'form': form})

def save_to_text(request):
    if request.method=='POST':
        text = request.POST.get('text')
        # print(text)
        return HttpResponse("text is test returns")
    

def job_description(request):
    if request.method == 'POST':
        pass
        

    return render(request,'job_description.html')


