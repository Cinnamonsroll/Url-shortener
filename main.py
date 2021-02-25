from flask import Flask, redirect, request, render_template
app = Flask(__name__)
import random
import string
import pymongo
conn = pymongo.MongoClient("mongo uri")
db = conn['python']
objects = db['urls']
@app.route('/', methods = ["GET", "POST"])
def index():
  if request.method == "POST":
    letters = string.ascii_lowercase
    id = ''.join(random.choice(letters) for i in range(10))
    objects.insert_one({
      "code":id,
      "url": request.form['url']
    })
    return render_template('index.html', id = id)
  else:
    return render_template('index.html')
@app.route('/<id>')
def id(id):
  doc =  objects.find_one({"code": id})
  if doc:
    return  redirect(doc['url'])
  else:
    return redirect("/")
if __name__ == '__main__':
    app.run(debug=True,	host='0.0.0.0')
