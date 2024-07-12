from flask import Flask, request, render_template


app = Flask(import_name="__init__" , template_folder="" , static_folder="static")
app.secret_key = "my_secret"

@app.route("/")
def root():
    return  render_template("templates/index.html" )
