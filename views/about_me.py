import streamlit as st

from forms.contact import contact_form


@st.experimental_dialog("Contact Me")
def show_contact_form():
    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile_image.jpeg", width=230)

with col2:
    st.title("Serdal Aslantas", anchor=False)
    st.write(
        "Data Scientist, assisting enterprises by supporting data-driven decision-making."
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 5 Years experience extracting actionable insights from data
    - Strong hands-on experience and knowledge in Python
    - Good understanding of statistical principles and their respective applications
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: Python (Scikit-learn, Pandas), SQL
    - Data Visualization: PowerBi, MS Excel, Plotly
    - Modeling: Logistic regression, linear regression, decision trees
    - Databases: Postgres, MongoDB, MySQL
    """
)
