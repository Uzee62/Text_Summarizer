from flask import Flask, render_template, request
from main import summarizer


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summary', methods=["GET","POST"])
def summary():
    if request.method=="POST":
        userText= request.form['Text']
        originalDoc,summary,len_orig_text,len_summary =  summarizer(userText)
        
        return render_template('summary.html', originalDoc=originalDoc, summary=summary,len_orig_text=len_orig_text,len_summary=len_summary)

if __name__ == "__main__":
    app.run(debug=True)
