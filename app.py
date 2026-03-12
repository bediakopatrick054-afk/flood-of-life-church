from flask import Flask, render_template, session, redirect 
from config import Config 
from database.db import init_db, db 
 
def create_app(): 
    app = Flask(__name__) 
    app.config.from_object(Config) 
    init_db(app) 
    return app 
 
app = create_app() 
 
if __name__ == '__main__': 
    app.run(debug=True) 
