import streamlit as st
import pyperclip



# Set up the title of the web app
st.title('Cover Letter Generator')


st.header('Job Type')

# Define job types
# job_types = ["Software Engineer", "Data Scientist", "ML Engineer", "Intern", "Others"]
job_types = ["Full-Time", "Intern"]

# Use radio buttons for job type selection
selected_job_type = st.radio("Select Job Type:", job_types, horizontal=True)

# if selected_job_type in ["Others", "Intern"]:
#     other_job_type = st.text_input("Specify the job title:", key="other_job_type")

job_title = st.text_input("Specify Job Title:", key="job_title", placeholder="e.g. Software Engineer")

st.header('Company')
company_name = st.text_input("Name:", placeholder="e.g. Google")
company_brief = st.text_area("Brief Introduction:", height=100)

st.header('Job Requirements')
# Add a text area for users to type in job requirements
job_responsibility = st.text_area("Responsibilities:", placeholder="The job responsibilities listed as: ...",  height=200)
job_requirement = st.text_area("Requirements:", placeholder="The job requirements listed as: ...", height=200)

st.header('Highlights')
highlight_types = ["Software Engineer", "Data Science", "Machine Learning", "Artificial Intelligence", "Others"]
# Use radio buttons for highlight type selection
selected_highlight_type = st.radio("Select the experience to highlight:", highlight_types, horizontal=True)

if selected_highlight_type in ["Others"]:
    selected_highlight_type = st.text_input("Specify the experience:", key="other_highlight_type")


## Read template
sde_template_path = "templates/sde_template.txt"
ds_template_path = "templates/ds_template.txt"
ai_template_path = "templates/ai_template.txt"
intern_template_path = "templates/intern_template.txt"
resume_intern_path = "templates/resume_doc_template.txt"
resume_path = "templates/resume_template.txt"

def read_template(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

resume_template = None
if selected_job_type in ["Intern"]:
    resume_template = read_template(resume_intern_path)
else:
    resume_template = read_template(resume_path)


# cover_letter_template = None
# if selected_job_type and company_name:
#     st.header('Cover Letter')
#     match selected_job_type:
#         case "Software Engineer":
#             cover_letter_template = read_template(sde_template_path)
#         case "Data Scientist":
#             cover_letter_template = read_template(ds_template_path)
#         case "ML Engineer":
#             cover_letter_template = read_template(ai_template_path)
#         case "Intern":
#             cover_letter_template = read_template(intern_template_path)
#         case _:
#             cover_letter_template = read_template(sde_template_path)
#     cover_letter_template = cover_letter_template.replace("company_name", company_name)
#     if selected_job_type in ["Others", "Intern"]:
#         cover_letter_template = cover_letter_template.replace("job_position", other_job_type)
#     else:
#         cover_letter_template = cover_letter_template.replace("job_position", selected_job_type)



#### Prepare Prompts ####
st.header('Prompt')

## Role prompt
prompt_role = "Please act as an experienced hiring manager. I will provide you with company background, job requirements, and my information. Please help me draft a competitive cover letter based on these information.\n"

## Emotional appeal
prompt_emotional_appeal = "Your job is very important! If you do it well, you will change my whole life!\n"

## Company and job info prompt
prompt_basic_info = f"I am applying for the {job_title} at {company_name}.\n"

prompt_company_info = f"The brief introduction of this company goes as: {company_brief}\n"

## Job responsibility prompt
prompt_res = f"The job responsibilities are described as: {job_responsibility}\n"

## Job requirements prompt
prompt_req = f"The job requirements are described as: {job_requirement}\n"

# cover_letter = f"'''\n{cover_letter_template}\n'''"

prompt_resume = f"Below in triple quotes is my resume: '''\n{resume_template}\n'''\n"

## Experience highlight prompt
prompt_highlight = f"When you draft the cover letter, please pick up and highlight my working experience and projects that are closely relevant to {selected_highlight_type}!\n"


prompts = [prompt_role, 
           prompt_emotional_appeal, 
           prompt_basic_info, 
           prompt_company_info, 
           prompt_res, 
           prompt_req, 
           prompt_resume,
           prompt_highlight]

prompts = "\n".join(prompts)

# if selected_job_type and company_name and company_brief and job_responsibility and job_requirement and selected_highlight_type:

if all([selected_job_type, job_title, company_name, company_brief, job_responsibility, job_requirement, selected_highlight_type]):
    text_to_copy = st.text_area("Prompt:", prompts, height=300)
    # Create a button
    if st.button("Copy"):
        # Copy the text to the clipboard
        pyperclip.copy(text_to_copy)

        # Display a message to the user
        st.success("Text copied to clipboard!")
   