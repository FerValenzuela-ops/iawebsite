
"""
Created on Thu Jan 13 17:01:18 2022

@author: Ferna
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Este sera el sitio web'
    
app.run()    