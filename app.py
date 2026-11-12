
import streamlit as st
from pypdf import PdfReader

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and analyze your career opportunities.")

name = st.text_input("Enter your name")

job_description = st.text_area("Paste Job Description")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)


# Function to extract text from PDF
def extract_resume_text(pdf_file):

    reader = PdfReader(pdf_file)

    resume_text = ""

    for page in reader.pages:
        resume_text += page.extract_text() or ""

    return resume_text



if st.button("Analyze Resume"):

    if name and job_description and uploaded_file:

        st.success(f"Welcome {name}!")

        # Extract PDF text
        extracted_text = extract_resume_text(uploaded_file)

        st.subheader("Extracted Resume Text")

        st.text_area(
            "Your Resume Content",
            extracted_text,
            height=300
        )

        # Available skills
        skills = [
            "Python", "Java", "SQL", "HTML",
            "CSS", "JavaScript", "Django",
            "Flask", "React", "C++", "Kotlin",
            "Git","Machine Learning", "AWS", 
            "Docker", "REST API"
        ]

        # Detect resume skills
        resume_skills = set()

        for skill in skills:
            if skill.lower() in extracted_text.lower():
                resume_skills.add(skill)

        # Detect job skills
        job_skills = set()

        for skill in skills:
            if skill.lower() in job_description.lower():
                job_skills.add(skill)

        # Compare skills
        matched_skills = job_skills.intersection(resume_skills)

        missing_skills = job_skills.difference(resume_skills)

        # Calculate percentage
        if job_skills:
            match_percentage = (
                len(matched_skills) / len(job_skills)
            ) * 100

            st.subheader("🎯 Resume Analysis")

            st.metric(
                "Job Match Percentage",
                f"{match_percentage:.2f}%"
            )
            st.progress(int(match_percentage))

            
            col1, col2 = st.columns(2)

            with col1:
                st.success("✅ Matching Skills")
                st.write(list(matched_skills))
                st.metric("Skills Matched", len(matched_skills))

            with col2:
                st.error("❌ Missing Skills")
                st.write(list(missing_skills))
                st.metric("Skills Missing", len(missing_skills))


            # Resume Improvement Suggestions
            st.subheader("💡 How to Improve Your Resume")

            if missing_skills:

                st.write("You should focus on learning these skills:")

                for skill in missing_skills:

                    if skill == "Python":
                        st.write("📘 Learn Python programming fundamentals.")

                    elif skill == "SQL":
                        st.write("📘 Practice SQL queries and database management.")

                    elif skill == "Django":
                        st.write("📘 Learn Django framework for backend development.")

                    elif skill == "Git":
                        st.write("📘 Learn Git and GitHub for version control.")

                    elif skill == "React":
                        st.write("📘 Learn React for frontend development.")

                    else:
                        st.write(f"📘 Improve your knowledge of {skill}.")

            else:
                st.success("Great! Your resume covers all detected job skills.")

        else:
            st.warning("No supported skills found in Job Description.")

    else:
        st.warning(
            "Please fill all details and upload your resume."
        )
