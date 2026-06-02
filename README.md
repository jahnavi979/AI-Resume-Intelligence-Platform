# AI Resume Intelligence Platform

An AI-powered Resume Analyzer built using **Django**, **Python**, **NLP**, and **OpenAI** that helps job seekers optimize their resumes against job descriptions. The platform calculates an ATS score, identifies matched and missing keywords, provides improvement suggestions, generates AI-powered feedback, and allows users to download PDF reports.

---

## 🚀 Features

### Authentication

* User Registration
* User Login
* User Logout
* Secure Authentication using Django Auth

### Resume Analysis

* Upload Resume (PDF/DOCX)
* Enter Job Description
* Extract Resume Text
* ATS Score Calculation
* Keyword Matching
* Missing Keyword Detection
* Resume Improvement Suggestions

### AI-Powered Features

* Resume Summary Generation
* Resume Improvement Recommendations
* Interview Question Suggestions
* Cover Letter Tips
* OpenAI Integration

### Report Generation

* Generate PDF Report
* Download Analysis Report
* View Previous Analysis History

### Dashboard

* User Dashboard
* Analysis History
* Resume Statistics

---

# 🛠️ Technologies Used

## Backend

* Python
* Django 5.x

## Frontend

* HTML5
* CSS3
* Bootstrap

## Database

* SQLite (Development)
* PostgreSQL (Production Ready)

## AI & NLP

* OpenAI API
* NLTK
* Scikit-Learn

## Resume Parsing

* PDFPlumber
* Python-Docx

## PDF Reports

* ReportLab

## Deployment

* Render
* Gunicorn
* WhiteNoise

---

# 📂 Project Structure

```plaintext
AI-Resume-Intelligence-Platform/
│
├── analyzer/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── parser.py
│   ├── ai_utils.py
│   ├── report_utils.py
│   ├── auth_views.py
│   └── urls.py
│
├── resume_ai/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── static/
├── media/
├── requirements.txt
├── build.sh
├── manage.py
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/jahnavi979/AI-Resume-Intelligence-Platform.git

cd AI-Resume-Intelligence-Platform
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key

DEBUG=True

OPENAI_API_KEY=your-openai-api-key
```

---

# 🗄️ Database Setup

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Create admin user:

```bash
python manage.py createsuperuser
```

---

# ▶️ Run Application

```bash
python manage.py runserver
```

Open:

```plaintext
http://127.0.0.1:8000
```

---

# 📊 ATS Score Calculation Workflow

### Step 1

Upload Resume

### Step 2

Provide Job Description

### Step 3

Resume Text Extraction

### Step 4

Text Cleaning using NLP

### Step 5

TF-IDF Vectorization

### Step 6

Cosine Similarity Calculation

### Step 7

Generate ATS Score

### Step 8

Display Results

* ATS Score
* Matched Keywords
* Missing Keywords
* Suggestions

---

# 🤖 AI Analysis Workflow

```plaintext
Resume + Job Description
            │
            ▼
      OpenAI API
            │
            ▼
    AI Resume Analysis
            │
            ▼
 ┌─────────────────────┐
 │ Resume Summary      │
 │ Improvements        │
 │ Interview Questions │
 │ Cover Letter Tips   │
 └─────────────────────┘
```

---

# 📄 PDF Report Generation

The application generates downloadable PDF reports containing:

* ATS Score
* Matched Keywords
* Missing Keywords
* Suggestions
* Analysis Summary

---

# 🌐 Deployment on Render

## Build Command

```bash
bash build.sh
```

## Start Command

```bash
gunicorn resume_ai.wsgi:application
```

### Environment Variables

```env
SECRET_KEY=your-secret-key

DEBUG=False

OPENAI_API_KEY=your-openai-api-key
```

---

# 📸 Screenshots

### Login Page

* User Authentication

### Dashboard

* Upload Resume
* Enter Job Description

### Analysis Report

* ATS Score
* AI Suggestions

### History Page

* Previous Analyses

---

# 🔮 Future Enhancements

* Resume Template Generator
* Multi-Language Resume Analysis
* LinkedIn Profile Analyzer
* Job Recommendation Engine
* AI Cover Letter Generator
* Resume Ranking System
* Recruiter Dashboard
* Email Notifications

---

# 👨‍💻 Author

**Potharlanka Jahnavi**

GitHub Repository:

[AI Resume Intelligence Platform Repository](https://github.com/jahnavi979/AI-Resume-Intelligence-Platform?utm_source=chatgpt.com)

---

# ⭐ Resume Project Description

**AI Resume Intelligence Platform** is a full-stack Django application that leverages Natural Language Processing (NLP) and Generative AI to analyze resumes against job descriptions. The system computes ATS compatibility scores using TF-IDF and Cosine Similarity, identifies skill gaps, generates AI-powered recommendations using OpenAI, and provides downloadable PDF reports to improve job application success rates.
