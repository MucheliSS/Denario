import streamlit as st
from denario import Denario

# If needed, set your project directory here:
project_dir = "/home/user/projects/Denario/project"  # or wherever files/data live locally
den = Denario(project_dir=project_dir)

st.title("Denario - Scientific Research Multi-Agent System")
st.markdown(f"Using Denario from: `{project_dir}`")
description = st.text_area("Describe your research/data prompt:")
if st.button("Set Description"):
    den.set_data_description(description)
    st.success("Prompt saved to Denario project.")

# (Add more Denario agent workflows... get_idea, get_method, etc.)
