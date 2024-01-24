import streamlit as st
from github import Github
from streamlit_option_menu import option_menu
import subprocess

st.set_page_config(
  page_title="Hackshpere",
  page_icon="⚡"
  )
st.toast("Welcome to Hacktiv8or's Hackpshere!")
st.toast("By~ Hacktiv8or aka Harsh")
st.warning("🛠️ Website under heavy Development 🛠")
tab = option_menu(
  menu_title = None,
  options = ["Upload","Download","Stats"],
  icons = ["cloud-arrow-up","download","graph-up"],
  default_index = 0,
  orientation = "horizontal",
  styles = {
      "icon": {"color": "lime", "font-size": "20px"},
      "nav-link": {
          "font-size": "20px",
          "text-align": "center",
          "margin": "0px",
          "--hover-color": "#eee"
      },
      "nav-link-selected": {"background-color": "red"}
  }
)


g = Github("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")
username = 'Hacktiv8or'
repo_name = 'Storage'
user = g.get_user(username)
repo = user.get_repo(repo_name)

if tab == "Upload":
  st.title("Hackshpere")
  uploads = st.file_uploader("Choose a file", accept_multiple_files=True)
  if uploads is not None:
    for upload in uploads:
            content = upload.read()
            filename = upload.name
            repo_path = f'uploads/{filename}'

            file_size = len(content) / (1024 * 1024)  # Size in MB
            st.write(f"File size: {file_size:.2f} MB")

            if file_size > 100:
              st.warning("File size exceeds 100 MB. Uploading with Git LFS.")
            
        try:
            contents = repo.get_contents(repo_path)
            # Update the file if it exists
            repo.update_file(repo_path, "Committing files", content, contents.sha, branch="main", use_lfs=True)
            st.success(f"File '{filename}' uploaded successfully!")
        except Exception as e:
            # Create the file if it doesn't exist
            repo.create_file(repo_path, "Committing files", content, branch="main", use_lfs=True)
            st.success(f"File '{filename}' uploaded successfully!")
            else:
               try:
                  contents = repo.get_contents(repo_path)
                  # Update the file if it exists
                  repo.update_file(repo_path, "Committing files", content, contents.sha, branch="main")
                  st.success(f'{repo_path} UPDATED')
               except:
                 repo.create_file(repo_path, "Committing files", content, branch="main")
                 st.success(f'{repo_path} CREATED')
      
               st.toast("Files uploaded successfully!", icon="✔️")
               st.toast("Thanks for Uploading!", icon="🚀")


if tab == "Download":
  # List all files in the "uploads" folder
  uploads_folder_contents = repo.get_contents('uploads')
  
  st.header("Files in the 'uploads' folder:")
  for file in uploads_folder_contents:
      # Display file name
      st.write(file.name)
  
      # Create a download link next to each file name
      download_link = f'<a href="{file.download_url}" download="{file.name}">Download</a>'
      st.markdown(download_link, unsafe_allow_html=True)

  
