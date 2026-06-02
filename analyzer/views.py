from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from .forms import ResumeAnalyzeForm
from .models import ResumeUpload, AnalysisResult
from .parser import extract_text
from .utils import clean_text, remove_stopwords, get_match_score, keyword_gap, generate_suggestions

@login_required
def dashboard(request):
    analyses = AnalysisResult.objects.filter(user=request.user).order_by('-created_at')[:5]
    total_analyses = AnalysisResult.objects.filter(user=request.user).count()
    average_score = AnalysisResult.objects.filter(user=request.user).aggregate(avg=Avg('ats_score'))['avg'] or 0

    return render(request, 'analyzer/dashboard.html', {
        'analyses': analyses,
        'total_analyses': total_analyses,
        'average_score': round(average_score, 2),
    })

@login_required
def analyze_resume(request):
    if request.method == 'POST':
        form = ResumeAnalyzeForm(request.POST, request.FILES)
        if form.is_valid():
            resume_file = form.cleaned_data['resume_file']
            job_description = form.cleaned_data['job_description']

            resume_obj = ResumeUpload.objects.create(user=request.user, file=resume_file)

            resume_text = extract_text(resume_obj.file, resume_obj.file.name)
            cleaned_resume = remove_stopwords(clean_text(resume_text))
            cleaned_jd = remove_stopwords(clean_text(job_description))

            score = get_match_score(cleaned_resume, cleaned_jd)
            matched, missing = keyword_gap(cleaned_resume, cleaned_jd)
            suggestions = generate_suggestions(score, missing)

            analysis = AnalysisResult.objects.create(
                user=request.user,
                resume=resume_obj,
                job_description=job_description,
                ats_score=score,
                matched_keywords=", ".join(matched[:30]),
                missing_keywords=", ".join(missing[:30]),
                suggestions=" | ".join(suggestions)
            )

            return render(request, 'analyzer/report.html', {'analysis': analysis})
    else:
        form = ResumeAnalyzeForm()

    return render(request, 'analyzer/analyze.html', {'form': form})

@login_required
def history(request):
    analyses = AnalysisResult.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'analyzer/history.html', {'analyses': analyses})

@login_required
def report(request, analysis_id):
    analysis = get_object_or_404(AnalysisResult, id=analysis_id, user=request.user)
    return render(request, 'analyzer/report.html', {'analysis': analysis})