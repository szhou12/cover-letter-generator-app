import streamlit as st


# Set up the title of the web app
st.title('Cover Letter Generator')


st.header('Job Type')

# Function to set the selected job type in the session state
def set_job_type(job_type):
    st.session_state.selected_job_type = job_type
    # Clear any text in the other job type input unless "Others" or "Intern" is selected
    if job_type not in ["Intern", "Others"]:
        st.session_state.other_job_type = ""

# Custom CSS to style the buttons to look like rectangle boxes
st.markdown("""
<style>
div.stButton > button {
    background-color: #eeeeee; 
    color: #000000;
    height: 5em; 
    width: 8.5em; 
    border-radius: 10px 10px 10px 10px;
    border: 2px solid #eeeeee;
    margin: 0.5em; /* Add margin around buttons */
    display: block; /* Ensure buttons take the full width available */
}
div.stButton > button:hover {
    background-color: #eeeeee;
    border-color: #8caba8; /* Optional: Change border color on hover for more noticeable effect */
    color: #8caba8;
}
</style>""", unsafe_allow_html=True)

# Initialize session state variables if they don't exist
if 'selected_job_type' not in st.session_state:
    st.session_state['selected_job_type'] = None
if 'other_job_type' not in st.session_state:
    st.session_state['other_job_type'] = ""

# Define job types
job_types = ["Software Engineer", "Data Scientist", "ML Engineer", "Intern", "Others"]


cols = st.columns(len(job_types))

# Create buttons in each column
# for col, job_type in zip(cols, job_types):
#     # Button styling to resemble rectangular boxes can be added via custom CSS in st.markdown
#     if col.button(job_type, key=f"btn_{job_type}"):
#         set_job_type(job_type)

for col, job_type in zip(cols, job_types):
    # Determine if the current job type is selected
    is_selected = (job_type == st.session_state.selected_job_type)
    # Button label reflects selection
    btn_label = f"✓ {job_type}" if is_selected else job_type
    
    # Use the `key` parameter to uniquely identify each button
    if col.button(btn_label, key=f"btn_{job_type}"):
        set_job_type(job_type)


# Show input field if "Others" or "Intern" is selected
if st.session_state.selected_job_type in ["Others", "Intern"]:
    # Adjust placeholder text based on selection
    placeholder_text = "e.g., Data Science and Engineering Intern" if st.session_state.selected_job_type == "Intern" else "e.g., AI Engineer"
    other_job_type = st.text_input("Specify the job type:", key="other_job_type_input", value=st.session_state.other_job_type, placeholder=placeholder_text)
    # Update session state with the input
    st.session_state.other_job_type = other_job_type


selected_job = None
# Optional: Display the selected or input job type
if st.session_state.selected_job_type and st.session_state.selected_job_type not in ["Others", "Intern"]:
    selected_job = st.session_state.selected_job_type
elif st.session_state.other_job_type:
    selected_job = st.session_state.other_job_type


st.header('Company')
company_name = st.text_input("Company Name:", placeholder="e.g. Google")


## Read template
sde_template_path = "templates/sde_template.txt"
ds_template_path = "templates/ds_template.txt"
ai_template_path = "templates/ai_template.txt"

def read_template(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

if selected_job and company_name:
    st.header('Cover Letter')
    cover_letter_template = None

    match selected_job:
        case "Software Engineer":
            cover_letter_template = read_template(sde_template_path)
        case "Data Scientist":
            cover_letter_template = read_template(ds_template_path)
        case "ML Engineer":
            cover_letter_template = read_template(ai_template_path)
        case _:
            cover_letter_template = read_template(sde_template_path)

    cover_letter_template = cover_letter_template.replace("company_name", company_name)
    cover_letter_template = cover_letter_template.replace("job_position", selected_job)

    st.text_area("Content:", cover_letter_template, height=300)