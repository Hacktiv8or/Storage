import streamlit as st
from github import Github

g = Github("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")
username = 'Hacktiv8or'
repo_name = 'Storage'
user = g.get_user(username)
repo = user.get_repo(repo_name)

st.title("GitHub File Uploader")

st.write("Hello World")
upload = st.file_uploader("Choose a file")
# if upload is not None:
#     # Read the content of the BytesIO object
#     content = upload.getvalue()

if upload is not None:
    # Read the content of the uploaded file
    content = upload.read()
    filename = upload.name

    # Specify the path where you want to upload the file in the repository
    repo_path = f'uploads/{filename}'

    # Check if the file already exists in the repository
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


files = repo.get_contents("uploads")
for file in files:
    file_name = file.name
    st.text(file_name)
    download_button = st.button(f"Download {file_name}")

    # When the download button is clicked, provide a link for download
    if download_button:
        file_url = f"https://github.com/{username}/{repo_name}/raw/main/uploads/{file_name}"
        st.markdown(f"[Download {file_name}]({file_url})")

# Read the content of the local file
# with open(local_file_path, 'rb') as file:
#     content = file.read()


# # Specify the path where you want to upload the file in the repository
# repo_path = f'uploads/asdf.py'

# # Check if the file already exists
# try:
#     contents = repo.get_contents(repo_path)
#     # Update the file if it exists
#     repo.update_file(repo_path, "Committing files", content, contents.sha, branch="main")
#     print(f'{repo_path} UPDATED')
# except:
#     # Create the file if it doesn't exist
#     repo.create_file(repo_path, "Committing files", content, branch="main")
#     print(f'{repo_path} CREATED')
