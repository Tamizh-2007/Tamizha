from fpdf import FPDF

# Personal Information
name = "Tamizharasan"
email = "tamizharasan740@gmail.com"
phone = "+91-8778029482"
linkedin = "linkedin.com/in/your-profile"
github = "github.com/your-profile"

# Resume Content
objective = "Motivated IT student pursuing B.Sc. in Information Technology with interest in software development and entrepreneurship."

skills = ["Python", "HTML", "CSS", "JavaScript", "MySQL", "Git"]

education = [
    {"degree": "B.Sc. Information Technology", "institution": "Your College Name", "year": "2025 - Present"},
    {"degree": "HSC (12th Grade)", "institution": "Kazhuvathevar Memorial Matric Higher Secondary School", "year": "2023"}
]

projects = [
    {"title": "Personal Portfolio Website", "description": "Created a responsive portfolio using HTML, CSS, and JavaScript."},
    {"title": "Student Management System", "description": "Built a basic CRUD application using Python and MySQL."}
]

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Header
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, name, ln=True, align='C')

pdf.set_font("Arial", '', 12)
pdf.cell(0, 10, f"Email: {email} | Phone: {phone}", ln=True, align='C')
pdf.cell(0, 10, f"LinkedIn: {linkedin} | GitHub: {github}", ln=True, align='C')
pdf.ln(5)  # Space after header

# Objective
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Objective", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, objective)
pdf.ln(2)

# Skills
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Skills", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, ", ".join(skills))
pdf.ln(2)

# Education
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Education", ln=True)
pdf.set_font("Arial", '', 12)
for edu in education:
    pdf.cell(0, 10, f"{edu['degree']} - {edu['institution']} ({edu['year']})", ln=True)
pdf.ln(2)

# Projects
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Projects", ln=True)
pdf.set_font("Arial", '', 12)
for project in projects:
    pdf.cell(0, 10, project['title'], ln=True)
    pdf.multi_cell(0, 10, f"    {project['description']}")
pdf.output("Tamizharasan_Resume.pdf")

print("Resume generated successfully!")
