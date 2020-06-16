import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/train')
def train():
    df = pd.read_excel('False Alarm Cases.xlsx')
    df.drop(['Case No.', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', '', 'Unwanted substance deposition(0/1)',
             'H2S Content(ppm)'], axis=1, inplace=True)

    X = df.drop('Spuriosity Index(0/1)', axis=1)
    y = df['Spuriosity Index(0/1)']

    ss = StandardScaler()
    scaled_arr = ss.fit_transform(X)
    X = pd.DataFrame(scaled_arr, columns=X.columns)

    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X, y)

    joblib.dump(knn, 'knn_model.pkl')

    return jsonify({'message': 'Model Trained'})


@app.route('/test', methods=['POST'])
def test():
    data = request.get_json()
    at = data['Temperature']
    cal = data['Calibration']
    hum = data['Humidity']
    nos = data['NoS']

    narr = np.array([at, cal, hum, nos]).reshape(1, 4)

    X_test = pd.DataFrame(narr, columns=['Temperature', 'Calibration', 'Humidity', 'NoS'])
    model = joblib.load('knn_model.pkl')
    y_pred = model.predict(X_test)

    if y_pred == 0:
        return jsonify({'message': 'No Danger'})
    else:
        return jsonify({'message': 'Danger'})

if __name__ == "__main__":
    app.run(debug=True)