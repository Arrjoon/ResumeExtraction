# Resume Extracting with Spacy NER

## Introduction
Resumes come in various formats, making it challenging to extract crucial information. NK.com is a platform that hosts resumes and connects them with hiring managers from Fortune 500 companies. Currently, their process relies heavily on manual labor. When a resume is uploaded, a human reviewer goes through it to extract essential details such as the Name, Designation, and Place of Work.

This manual process is labor-intensive and problematic, especially when dealing with thousands of uploaded resumes and a limited workforce. To address this issue develop a resume extractor that can automatically extract key elements from resumes using Machine Learning (ML) and present the results.

---
# Resume_extractor

Resume extractor is a program designed to automate the task of extracting key information from resumes. With this program, you can easily and quickly extract information such as candidate name, email, phone number, education, work experience, and skills from a resume.

The project has been developed by the ADG team, which consists of @kushal-02 , @harshitsarda and @Izhan-07 .

## What is a Resume Extractor?

A resume extractor is a deep learning/AI framework that identifies complete information from resumes, analyzes, store, organize, and enriches it through its taxonomies. Resume parsing software makes the hiring process quick and more productive.

Fast and accurate resume parsing technology improves efficiency and offers an enhanced candidate experience.

It is a component that automatically segregates the information into various fields and parameters like contact information, educational qualification, work experience, skills, achievements, professional certifications to quickly help you identify the most relevant resumes based on your criteria.

A extractor takes input in the form of a sequence of program instructions and tends to build a data structure, a "parse tree," or an abstract syntax tree.


## Dataset Description

To aid in the development of the resume extractor, we use dataset in json. This dataset includes JSON files with labeled information for each resume. The labeled fields include:

- Location
- Designation
- Name
- Years of Experience
- College
- Degree
- Graduation Year
- Companies worked at
- Email address

---

## Objective

To build resume extractor model to automatically identify and extract the key elements from resumes, streamlining the hiring process for NK.com.

---
## NLP Tools and Techniques Used:
### Tokenization

It is the process of splitting textual data into different pieces called tokens. One can either break a sentence into tokens of words or characters; the choice depends on the problem one is interested in solving. It is usually the first step that is performed in any NLP project, and the same will be the case with this resume extractor using NLP project. Tokenization helps in further steps of an NLP pipeline which usually involves evaluating the weights of all the words depending on their significance in the corpus.



### Lemmatization

The larger goal of this resume parsing python application is to decode the semantics of the text. For that, the form of the verb that is used does not have a significant impact. Therefore, lemmatization is used to convert all the words into their root form, called 'lemma.' For example, 'drive,' 'driving, 'drove' all have the same lemma 'drive.'



### Parts-of-Speech Tagging

If you consider the word "Apple," it can have two meanings in a sentence. Depending on whether it has been used as a proper noun or a common noun, you will understand whether one is discussing the multinational tech company or the fruit. This CV extractor python project will understand how POS Tagging is implemented in Python.



### Stopwords Elimination

Stopwords are the words like 'a', 'the,' 'am', 'is', etc., that hardly add any meaning to a sentence. These words are usually deleted to save on processing power and time. In their CV, an applicant may submit their work experience in long paragraphs with many stopwords. For such cases, it becomes essential to know how to extract experience from a resume in python, which you will learn in this project.



### SpaCy

SpaCy is a library in Python that is widely used in many NLP-based projects by data scientists as it offers quick implementation of techniques mentioned above. Additionally, one can use SpaCy to visualize different entities in text data through its built-in visualizer called displacy. Furthermore, SpaCy supports the implementation of rule-based matching, shallow parsing, dependency parsing, etc. This NLP resume extractor project will guide you on using SpaCy for Named Entity Recognition (NER).




