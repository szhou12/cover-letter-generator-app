import streamlit as st


# Set up the title of the web app
st.title('Cover Letter Generator')


st.header('Job Type')

# Define job types
job_types = ["Software Engineer", "Data Scientist", "ML Engineer", "Intern", "Others"]


# Use radio buttons for job type selection
selected_job_type = st.radio("Select the job type:", job_types, horizontal=True)

if selected_job_type in ["Others", "Intern"]:
    other_job_type = st.text_input("Specify the job title:", key="other_job_type")


st.header('Company')
company_name = st.text_input("Company Name:", placeholder="e.g. Google")


## Read template
sde_template_path = "templates/sde_template.txt"
ds_template_path = "templates/ds_template.txt"
ai_template_path = "templates/ai_template.txt"
intern_template_path = "templates/intern_template.txt"

def read_template(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

if selected_job_type and company_name:
    st.header('Cover Letter')
    cover_letter_template = None

    match selected_job_type:
        case "Software Engineer":
            cover_letter_template = read_template(sde_template_path)
        case "Data Scientist":
            cover_letter_template = read_template(ds_template_path)
        case "ML Engineer":
            cover_letter_template = read_template(ai_template_path)
        case "Intern":
            cover_letter_template = read_template(intern_template_path)
        case _:
            cover_letter_template = read_template(sde_template_path)

    cover_letter_template = cover_letter_template.replace("company_name", company_name)
    
    if selected_job_type in ["Others", "Intern"]:
        cover_letter_template = cover_letter_template.replace("job_position", other_job_type)
    else:
        cover_letter_template = cover_letter_template.replace("job_position", selected_job_type)

    cover_letter_template = cover_letter_template + "\nShuyu Zhou"

    st.text_area("Content:", cover_letter_template, height=300)