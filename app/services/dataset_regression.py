from sklearn.model_selection import train_test_split
import numpy as np
import lightgbm as lgb


def predict_model(df):
    pred_temp_ext = predict_temperature_ext(df)
    pred_humidity = predict_humidity_dht(df)

    return pred_temp_ext, pred_humidity


def predict_temperature_ext(dataframe):
    y_prediction = dataframe[["temperature_ext"]]
    x_data = dataframe.drop(columns=["temperature_ext", "humidity_dht"], axis=1)

    X_train, X_test, y_train, y_test = train_test_split(
        x_data, y_prediction, test_size=0.2, random_state=42
    )

    train_data = lgb.Dataset(X_train, label=y_train)
    params = {
        "objective": "regression",
        "metric": "rmse",
        "num_leaves": 31,
        "learning_rate": 0.05,
        "feature_fraction": 0.9,
    }

    model = lgb.train(params, train_data, num_boost_round=100)

    # Fazer a previsão para as próximas 3 horas
    new_data = np.array([[25.5, 65.2, 24.8, 1008.2, 0.1, 500]])

    y_pred = model.predict(new_data)
    y_pred = "%.2f" % y_pred

    print("Previsao proximas 3 horas", y_pred)
    return y_pred


def predict_humidity_dht(dataframe):
    y_prediction = dataframe[["humidity_dht"]]
    x_data = dataframe.drop(columns=["temperature_ext", "humidity_dht"], axis=1)

    X_train, X_test, y_train, y_test = train_test_split(
        x_data, y_prediction, test_size=0.2, random_state=42
    )

    train_data = lgb.Dataset(X_train, label=y_train)
    params = {
        "objective": "regression",
        "metric": "rmse",
        "num_leaves": 31,
        "learning_rate": 0.05,
        "feature_fraction": 0.9,
    }

    model = lgb.train(params, train_data, num_boost_round=100)

    # Fazer a previsão para as próximas 3 horas
    new_data = np.array([[25.5, 26.7, 24.8, 1008.2, 0.1, 500]])

    y_pred = model.predict(new_data)
    y_pred = "%.2f" % y_pred

    print("Previsao proximas 3 horas", y_pred)
    return y_pred
