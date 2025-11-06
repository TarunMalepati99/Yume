!pip install PyPDF2 reportlab
from PyPDF2 import PdfReader
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from google.colab import files
import re

# Step 1: Upload your PDF
uploaded = files.upload()
pdf_path = next(iter(uploaded))

# Step 2: Extract text from PDF
reader = PdfReader(pdf_path)
full_text = ""
for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        full_text += page_text + "\n"

# Step 3: Clean text for consistent parsing
full_text = full_text.replace('\r', ' ')
full_text = re.sub(r'\s+', ' ', full_text)  # normalize spaces
full_text = full_text.strip()

# Save the extracted text for inspection
with open("stored_script.txt", "w", encoding="utf-8") as out:
    out.write(full_text)

# Optional: preview snippet to confirm it worked
print("📖 Extracted text sample:\n", full_text[:400], "\n---")

# Step 4: Correct regex pattern (case-insensitive, flexible spacing)
pattern = r'(?i)\b(INT|EXT)\s*\.?\s*(.*?)(?=\bINT\b|\bEXT\b|$)'

matches = list(re.finditer(pattern, full_text))

print(f"✅ Found {len(matches)} scene splits")

# Step 5: Generate a new PDF with the split scenes
output_filename = "scene_breakdown.pdf"
c = canvas.Canvas(output_filename, pagesize=LETTER)
width, height = LETTER
y_position = height - 80

c.setTitle("Scene Breakdown")
c.setFont("Helvetica-Bold", 16)
c.drawString(100, y_position, "Scene Breakdown")
y_position -= 40

# Step 6: Add each scene to the output PDF
for i, match in enumerate(matches, start=1):
    header = match.group(1).upper()  # INT or EXT
    content = match.group(2).strip()

    c.setFont("Helvetica-Bold", 12)
    c.drawString(80, y_position, f"Scene {i} ({header})")
    y_position -= 20

    c.setFont("Helvetica", 11)
    for line in re.findall('.{1,90}', content):  # wrap lines
        if y_position < 100:  # new page
            c.showPage()
            y_position = height - 80
            c.setFont("Helvetica", 11)
        c.drawString(100, y_position, line)
        y_position -= 15
    y_position -= 25

# Step 7: Save and download the result
c.save()
files.download(output_filename)

# Step 8: Keep scenes for future use
scenes = [match.group(0).strip() for match in matches]
