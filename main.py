from flask import Flask,render_template,redirect,send_file
from os import path,listdir

app = Flask(__name__)

@app.route('/images/<file>', methods=['GET'])
@app.route('/<path:folder>/images/<file>', methods=['GET'])
def get_image(folder='',file=''):
    return send_file(f'images/{file}', mimetype='image/jpeg')

@app.route('/<path:folder>/lab<no>/<file>', methods=['GET'])
@app.route('/lab<no>/<file>', methods=['GET'])
def getFile(folder='',no='1',file=''):
    file = f"lab{no}/{file}"
    if path.exists(f"templates/{file}"):
        return render_template(file)
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