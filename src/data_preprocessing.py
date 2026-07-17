import pandas as pd


def preprocess_input(data):

    data = pd.get_dummies(
        data,
        drop_first=True
    )

    return data


print("Preprocessing module loaded ✅")