from flask import Flask, render_template, request
import marks as m

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])

def hello():
    if request.method == 'POST':
        hrs = request.form['hrs']
        score_pred = m.marks_prediction(hrs)
        mk = score_pred
    return render_template("index.html", score = mk)



# @app.route("/sub", methods=['POST'])

# def submit():
#     # Sending data from HTML to Python 
    
#     if request.method == 'POST':
#         name = request.form['username']
#         # sending from python to HTML
#     return render_template('sub.html', n = name)

if __name__ == "__main__":
    app.run(debug=True)