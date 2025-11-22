from pathlib import Path
from docx import Document
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

IN_DIR = Path("tests/resumes")
OUT_DIR = IN_DIR
OUT_DIR.mkdir(parents=True, exist_ok=True)

styles = getSampleStyleSheet()

for docx_file in sorted(IN_DIR.glob("*.docx")):
    doc = Document(docx_file)
    text = "\n\n".join([p.text for p in doc.paragraphs if p.text])

    pdf_path = OUT_DIR / (docx_file.stem + ".pdf")
    doc_pdf = SimpleDocTemplate(str(pdf_path))
    story = []
    for para in text.split('\n\n'):
        para = para.strip()
        if not para:
            continue
        story.append(Paragraph(para.replace('\n','<br/>'), styles['Normal']))
        story.append(Spacer(1, 8))

    doc_pdf.build(story)
    print(f"Wrote PDF: {pdf_path}")

print("PDF generation done")