import streamlit as st
import re
import time
import clipboard
from io import BytesIO
import pathlib

#genai code
import google.generativeai as genai

#key = st.secrets.db.pass
st.write("key = ", st.secrets["key"])
genai.configure(api_key = key)
model = genai.GenerativeModel('gemini-pro')

def is_github_url(url):
    github_url_pattern = r"https://github.com/[-\w]+/[-\w]+"
    return re.match(github_url_pattern, url) is not None

# Define the function to generate README content
def generate_readme(github_repo_url):
    # Call the model to generate README content based on the provided GitHub repository URL
    prompt = f"Please analyze the codebase of the given GitHub repository ({github_repo_url}) and generate a professional README.md file in markdown format that provides comprehensive information about the project. The generated README should include details about the project's purpose, features, technologies used, getting started instructions, git clone,contribution guidelines, license information, and contact details."
    response = model.generate_content(prompt)
    print(response.text)
    return response.text

# Set Streamlit page config
st.set_page_config(layout="wide", page_title="README.MD FILE GENERATOR")

# Tabs for "About" and "Developers"
tabs = st.sidebar.radio("Tabs", ("About", "Developers"))

# Main content
st.write("# 🌈README.MD FILE GENERATOR")
st.write(":dog: Upload your GitHub URL to watch it magically generate a Readme.md file for you.")
st.sidebar.write("## 🌈Upload and copy :gear:")

# User input for GitHub repository URL
github_repo_url = st.text_input("Enter GitHub Repository URL:")

# Check if a GitHub repository URL is provided
if github_repo_url:
    # Validate the GitHub repository URL
    if not is_github_url(github_repo_url):
        st.error("Invalid GitHub Repository URL. Please enter a valid URL in the format https://github.com/username/repository.")
    else:
        # If the URL is valid and the user presses the copy button, generate README
        if st.button("Generate README"):
            st.success("Generating README...")        
            container = st.container(border=True)
            container.write("### readme.md")
            readme_text = generate_readme(github_repo_url)
            container.write(readme_text)
            container.button("Copy", key="copy")
            clipboard.copy(readme_text)

        


image_url2 = "https://media.giphy.com/media/11JTxkrmq4bGE0/giphy.gif"

col2 = st.columns(1)[0]

with col2:
    st.markdown(
        f'<div style="display: flex; justify-content: center;"><img src="{image_url2}" style="max-width: 100%; height: auto;" /></div>',
        unsafe_allow_html=True
    )
    #st.write("Visualize with a GIF")


# Tab: About
if tabs == "About":
    st.write("## About")
    container = st.container(border=True)
    #container.write("🐱Go to the developer section and contact with them. How myself Streamlit as a server have idea about their working concept🐱")
    container.markdown(" :red[🌈 How it Works for generating Readme.md file?]  \n:blue[Go to the developer section and contact with them. How myself Streamlit as a server have idea about their working concept.🐱]")


# Tab: Developers
elif tabs == "Developers":
    st.write("## 🌟 Developers")
    st.write("### Have you want any help?")

    # Developer
    st.image("https://media.licdn.com/dms/image/D4D03AQH-xOdK5K2fHg/profile-displayphoto-shrink_200_200/0/1694320992432?e=1709164800&v=beta&t=L2W5BSfYGiIyPU24tOcnzZHh7yGnXA4WQ1bh_Ykf5tQ", caption="Developer", use_column_width=True, width=40) 
    st.write("**Name:** SOURAV KUMAR")
    st.write("**GitHub:** [sourav kumar](https://github.com/singhsourav0)")
    st.write("**LinkedIn:** [Sourav Kumar](https://www.linkedin.com/in/singhsourav0)")

    st.write("### 🚀 Future Updates")
    container = st.container(border=True)
    container.markdown(
        " :red[Stay tuned for future updates and improvements to the Readme.md Generator!  \nThis project is a stepping stone towards building an readme.md file.  \nIn the future, it will generate with having no any modification from advanced code analysis technology.   \nbut for now use it as the prototype of my actual model.] "

    )

# Add a gif to the sidebar
st.sidebar.image("https://media.giphy.com/media/H7CKd1GO6oiZQo7L5d/giphy.gif", caption="Visualize with a GIF", use_column_width=True)
st.sidebar.image("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" ,caption="Visualize with a GIF", use_column_width=True)
