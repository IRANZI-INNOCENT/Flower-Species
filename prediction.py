import joblib
def predict(data):
    clf = joblib.load("C:\\Users\\Admin\\OneDrive\\Desktop\\ML PROJECT\\Iris App\\rf_model.sav")
    return clf.predict(data)