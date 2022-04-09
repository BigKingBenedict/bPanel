from createserver import create
from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/panel", code=302)

@app.route('/panel')
def loginPage():
    return render_template('auth/login.html')

@app.route('/panel', methods=['POST'])
def loginProcced():
    user=request.form['username']
    password=request.form['password']

    import accounts
    if accounts.login(str(user),str(password)) is True:
        return loadPanel(user)
    else:  
        return render_template('auth/login.html', err=" (Login Failed!)")  

@app.route('/')
def loadPanel(user=str):
    if user is None:
        return render_template('auth/login.html') 
    else:
        import server_list
        server_list.load_servers(user)
        return render_template('panel/index.html', user=user)    

@app.errorhandler(TypeError)
def error(ex):
    return loginPage()

@app.errorhandler(404)
def error(ex):
    return render_template('errors/404.html')    

def passorusererror():
    return    

if __name__ == '__main__':
    app.run(host = 'localhost', port = 80, debug=True)