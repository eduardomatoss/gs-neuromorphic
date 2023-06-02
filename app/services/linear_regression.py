from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression
import numpy as np


def predict_model(df):
    y_prediction = df[["temperature_ext"]]
    x_data = df.drop("temperature_ext", axis=1)

    X_train, X_test, y_train, y_test = train_test_split(
        x_data, y_prediction, test_size=0.2, random_state=42
    )

    lm = LinearRegression()
    lm.fit(X_train, y_train)
    y_pred = lm.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    new_data = np.array([[25.5, 65.2, 26.7, 24.8, 1008.2, 0.1, 500]])

    prediction = lm.predict(new_data)
    prediction = "%.2f" % prediction

    print("Previsao proximas 3 horas", prediction)

    return X_test, y_test, y_pred, r2, mse, mae
