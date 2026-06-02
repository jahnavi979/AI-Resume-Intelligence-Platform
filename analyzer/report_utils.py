from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf_report(file_path, analysis):
    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    y = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "AI Resume Analysis Report")

    y -= 40
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"ATS Score: {analysis.ats_score}%")

    y -= 20
    c.drawString(50, y, "Matched Keywords:")
    y -= 20
    text = c.beginText(70, y)
    text.textLines(analysis.matched_keywords or "None")
    c.drawText(text)

    y -= 80
    c.drawString(50, y, "Missing Keywords:")
    y -= 20
    text = c.beginText(70, y)
    text.textLines(analysis.missing_keywords or "None")
    c.drawText(text)

    y -= 80
    c.drawString(50, y, "Suggestions:")
    y -= 20
    text = c.beginText(70, y)
    text.textLines(analysis.suggestions or "None")
    c.drawText(text)

    c.save()