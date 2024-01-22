import streamlit as st
from github import Github
import os

g = Github("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")
username = 'Hacktiv8or'
repo_name = 'Storage'
user = g.get_user(username)
repo = user.get_repo(repo_name)

st.write("Hello World")
upload = st.file_uploader("Choose a file")
if upload is not None:
  with open(upload, 'rb') as file:
    content = file.read()

# Read the content of the local file
# with open(local_file_path, 'rb') as file:
#     content = file.read()
filename = os.path.basename(upload)

# Specify the path where you want to upload the file in the repository
repo_path = f'uploads/{filename}'

# Check if the file already exists
try:
    contents = repo.get_contents(repo_path)
    # Update the file if it exists
    repo.update_file(repo_path, "Committing files", content, contents.sha, branch="main")
    print(f'{repo_path} UPDATED')
except:
    # Create the file if it doesn't exist
    repo.create_file(repo_path, "Committing files", content, branch="main")
    print(f'{repo_path} CREATED')
