import streamlit as st
from github import Github
from streamlit_option_menu import option_menu

st.set_page_config(
  page_title="Hackshpere",
  page_icon="⚡"
  )

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
  upload = st.file_uploader("Choose a file")
  if upload is not None:
      content = upload.read()
      filename = upload.name
      repo_path = f'uploads/{filename}'
      try:
          contents = repo.get_contents(repo_path)
          # Update the file if it exists
          repo.update_file(repo_path, "Committing files", content, contents.sha, branch="main")
          st.success(f'{filename} updated successfully!')
      except:
          # Create the file if it doesn't exist
          repo.create_file(repo_path, "Committing files", content, branch="main")
          st.success(f'{filename} uploaded successfully!')
  else:
      st.warning("Please upload a file.")

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

  
