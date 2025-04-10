from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import statsmodels.api as sm

app = Flask(__name__)

# 真实数据
data = {
    'Y_obs': [137, 118, 124, 124, 120, 129, 122, 142, 128, 114,
              132, 130, 130, 112, 132, 117, 134, 132, 121, 128],
    'W': [0, 1, 1, 1, 0, 1, 1, 0, 0, 1,
          1, 0, 0, 1, 0, 1, 0, 0, 1, 1],
    'X': [19.8, 23.4, 27.7, 24.6, 21.5, 25.1, 22.4, 29.3, 20.8, 20.2,
          27.3, 24.5, 22.9, 18.4, 24.2, 21.0, 25.9, 23.2, 21.6, 22.8]
}

df = pd.DataFrame(data)

# 模型训练
X_train = df[['W', 'X']]
X_train = sm.add_constant(X_train)  # 加截距项
model = sm.OLS(df['Y_obs'], X_train).fit()

@app.route("/predict")
def predict():
    W = float(request.args.get("W", 0))
    X_value = float(request.args.get("X", 0))
    input_data = np.array([[1, W, X_value]])  # 注意1是alpha截距
    y_pred = model.predict(input_data)[0]

    return jsonify({"W": W, "X": X_value, "Predicted Engagement Score": y_pred})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
