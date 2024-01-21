from flask import Flask, request, send_file, render_template, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# root route
@app.route('/')
def index():
  # Get the list of files in your uploads folder
  files_in_folder = os.listdir(app.config['UPLOAD_FOLDER'])

  # Create a list of dictionaries containing the file names
  files = [{'name': file} for file in files_in_folder]

  # Render the template with the list of files
  return render_template('index.html', files=files)


# Upload route
@app.route('/upload', methods=['POST'])
def upload_file():
  uploaded_file = request.files['file']
  if uploaded_file.filename != '':
    file_path = os.path.join(app.config['UPLOAD_FOLDER'],
                             uploaded_file.filename)
    uploaded_file.save(file_path)
    return 'File uploaded successfully!'
  else:
    return 'No file selected!'


# Download route
@app.route('/upload/<filename>', methods=['GET'])
def download_file(filename):
  file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
  if os.path.exists(file_path):
    return send_file(file_path, as_attachment=True)
  else:
    return 'File not found!'


def get_icon(filename):
  extension = filename.split('.')[-1]  # Get file extension
  # Logic to match file extension with icons
  icon_mapping = {
      'txt': 'txt.png',
      'py': 'py.png',
      'ino': 'ardu.png',
      'jpg': 'img.png',
      'jpeg': 'img.png',
      'png': 'img.png',
      'MOV': 'vid.png',
      'h': 'wt.png',
      'pt': 'wt.png',
      'zip': 'zip.png',
      'docx': 'doc.png'
  }
  return icon_mapping.get(extension, 'icons/idk.png')


# Add the get_icon function to the Jinja context
app.jinja_env.globals.update(get_icon=get_icon)

if __name__ == '__main__':
  os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
  app.run(host='0.0.0.0', port=5000, debug=True)
