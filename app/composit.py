#!/usr/bin/env python
# coding: utf-8
# 
from flask import Flask, render_template, request
from joblib import load
from sklearn.preprocessing import StandardScaler, MinMaxScaler, Normalizer
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
import numpy as np

# Загрузить модель с диска
# Перенести процесс предобработки

app = Flask(__name__)

model1 = load('Модуль упругости при растяжении, ГПа.joblib')
model2 = load('Прочность при растяжении.joblib')
@app.route('/', methods=['POST', 'GET'])
def doit():
    mess1 = ''
    mess2 = ''
    if request.method == 'POST':
        Xst = []
        Xst.append(request.form.get("feature0"))   
        Xst.append(request.form.get("feature1"))
        Xst.append(request.form.get("feature2"))
        Xst.append(request.form.get("feature3"))
        Xst.append(request.form.get("feature4"))
        Xst.append(request.form.get("feature5"))
        Xst.append(request.form.get("feature6"))
        Xst.append(request.form.get("feature7"))
        Xst.append(request.form.get("feature8"))
        Xst.append(request.form.get("feature9"))
        Xst.append(request.form.get("feature10"))

        X = [float(i) for i in Xst if i.replace('.', '').isdigit()]

        if len(X) != 11:
            mess1 = f"Неверное количество параметров {len(X)}, должно быть 11"
        else:
            X[6] = X[6] ** 0.5
            X = np.array(X).reshape(1, -1)

            mess1 = f'Ожидаемый модуль упругости при растяжении, ГПа: {round(model1.predict(X)[0], 3)}'
            mess2 = f'Ожидаемая прочность при растяжении, МПа: {round(model2.predict(X)[0], 3)}'

    return render_template('index.html',
                           message='Прогноз модуля упругости при растяжении, прочности при растяжении',
                           message1=mess1,
                           message2=mess2
                           )

app.run()
