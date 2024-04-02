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

def read_template(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

cover_letter_template = None
if selected_job_type and company_name:
    st.header('Cover Letter')
    

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

    # cover_letter_template = cover_letter_template + "\nShuyu Zhou"

    # st.text_area("Content:", cover_letter_template, height=300)


## Role prompt
prompt_role = "Please act as an experienced hiring manager and help me improve my cover letter based on the company and job requirements."

## Emotional appeal
emotional_appeal = "Your modification on my cover letter is very important as I totally depend on you to get this job!"

## Company and job info prompt
prompt_basic_info = f"I am applying for the [JOB POSITION] at {company_name}."
if selected_job_type in ["Others", "Intern"]:
    prompt_basic_info = prompt_basic_info.replace("[JOB POSITION]", other_job_type)
else:
    prompt_basic_info = prompt_basic_info.replace("[JOB POSITION]", selected_job_type)

prompt_company_info = f"The brief introduction of this company goes as: {company_brief}"

## Job responsibility prompt
prompt_res = f"The job responsibilities are described as: {job_responsibility}"

## Job requirements prompt
prompt_req = f"The job requirements are described as: {job_requirement}"

## Experience highlight prompt
prompt_highlight = f"Based on the given information, please help me customize my cover letter provided below in triple quotes. Remember to highlight my relevant experience in {selected_highlight_type}:"

cover_letter = f"'''\n{cover_letter_template}\n'''"


prompts = [prompt_role, emotional_appeal, prompt_basic_info, prompt_company_info, prompt_res, prompt_req, prompt_highlight, cover_letter]
prompts = "\n".join(prompts)

# if selected_job_type and company_name and company_brief and job_responsibility and job_requirement and selected_highlight_type:

if all([selected_job_type, company_name, company_brief, job_responsibility, job_requirement, selected_highlight_type]):
    st.text_area("Prompt:", prompts, height=300)
   