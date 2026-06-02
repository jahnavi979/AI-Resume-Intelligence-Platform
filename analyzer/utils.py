import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def remove_stopwords(text):
    words = text.split()
    filtered = [w for w in words if w not in STOPWORDS]
    return " ".join(filtered)

def get_match_score(resume_text, jd_text):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text, jd_text])
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(score * 100, 2)

def keyword_gap(resume_text, jd_text):
    resume_words = set(resume_text.split())
    jd_words = set(jd_text.split())

    matched = sorted(list(resume_words.intersection(jd_words)))
    missing = sorted(list(jd_words.difference(resume_words)))

    return matched, missing

def generate_suggestions(score, missing_keywords):
    suggestions = []

    if score >= 80:
        suggestions.append("Strong match. Keep the resume aligned with this job profile.")
    elif score >= 60:
        suggestions.append("Moderate match. Add more role-specific keywords and projects.")
    else:
        suggestions.append("Low match. Rewrite the resume to fit the job description better.")

    if missing_keywords:
        suggestions.append("Include missing technical skills from the job description.")
        suggestions.append("Use the same wording as the job description where it is truthful.")

    suggestions.append("Add measurable achievements with numbers and results.")
    suggestions.append("Use clear sections like Summary, Skills, Experience, Projects, and Education.")

    return suggestions