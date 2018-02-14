from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route("/")
def hello():    
    return "My first app flask"

@app.route("/melhormundo")
def eleicao():
    data = [{'id':1, 'name':'Neymar', 'time':'PSG'}, {'id':2, 'name':'Ronaldo', 'time':'Madrid'}, {'id':3, 'name':'Messi', 'time':'Barça'}]
    return render_template('index.html', **{'data':data})

if __name__=='__main__':
    app.run()