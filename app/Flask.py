#!/usr/bin/env python
# coding: utf-8

# # Приложение для демонстрации

# **Примечание:** Flask-приложения, которые необходимо разворачивать на сервере, создаются в виде файлов с расширением **.py**
# 
# В данном уроке используется формат Jupyter Notebook исключительно для удобства *демонстрации*

# In[ ]:





# In[ ]:


from flask import Flask, render_template, request
# псевдокод:
# из файла my_module.py импортируем функции
# from my_module import func1, func2, ...
# Например: model.py, preprocessing.py, visualisation.py | postprocessing.py

app = Flask(__name__)


# псевдокод
# def get_model():
#     return model
#-----------------


def check_username(username, password):
    if len(username) < 3:
        message = "Incorrect username"
    else:
        message = f"User {username} has password {password}"
    return message


@app.route("/")
def index():
    return "Главная страница"


@app.route("/login/", methods=["post", "get"])
def get_password():
#     model = get_model()
    message = "Test"
    
    if request.method == "POST":
        u = request.form.get("username")
        p = request.form.get("password")
        
        message = check_username(u, p)
    
    return render_template("login.html", message=message)


app.run()


# In[ ]:





# In[ ]:





# In[ ]:




