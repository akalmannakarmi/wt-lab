from flask import Flask,render_template,redirect
from os import path,listdir

app = Flask(__name__)

@app.route('/<folder>/<file>',methods=["GET"])
def getFile(folder,file):
    p = f"/{folder}/{file}"
    if path.exists(f"templates/{p}"):
        return render_template(p)
    return redirect('/')

@app.route("/",methods=["GET"])
def index():
    templates_dir = path.join(app.root_path, 'templates')
    folders = [f for f in listdir(templates_dir) if path.isdir(path.join(templates_dir, f))]
    data = {}
    for folder in folders:
        folder_path = path.join(templates_dir, folder)
        files = [f for f in listdir(folder_path) if path.isfile(path.join(folder_path, f))]
        data[folder] = files
    return render_template("labs.html",data=data)

if __name__ == "__main__":
    app.run(debug=True)