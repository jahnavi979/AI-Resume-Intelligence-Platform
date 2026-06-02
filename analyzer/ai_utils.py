import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ai_suggestions(resume_text, job_description, missing_keywords):
    prompt = f"""
You are an expert ATS resume reviewer.

Return ONLY valid JSON in this format:
{{
  "summary": "short summary",
  "resume_improvements": ["suggestion 1", "suggestion 2"],
  "interview_questions": ["question 1", "question 2"],
  "cover_letter_tip": "one short tip"
}}

Resume:
{resume_text}

Job Description:
{job_description}

Missing Keywords:
{", ".join(missing_keywords[:20])}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {"role": "system", "content": "You are a helpful AI resume analyst. Return only valid JSON."},
            {"role": "user", "content": prompt}
        ],
    )

    text = response.output_text.strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {
            "summary": text,
            "resume_improvements": [],
            "interview_questions": [],
            "cover_letter_tip": ""
        }