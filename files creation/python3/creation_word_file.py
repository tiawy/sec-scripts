import docx

for i in range(1, 11):
    doc = docx.Document()
    doc.add_paragraph(f"This is document {i}.")
    doc.save(f"document_{i}.docx")
