from flask import Flask
app =Flask(__name__)
@app.route("/")
def hello():
    return "Hello DevOps! this is test for change in Github."
if __name__ == "__Main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


