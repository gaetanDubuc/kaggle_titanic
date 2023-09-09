""" The input has to be split into test and train sets. """
import pandas as pd
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    df: pd.DataFrame = pd.read_csv("input/titanic/train.csv")
    splits = train_test_split(
        df,
        test_size=0.25,
        random_state=0,
        shuffle=True,
        stratify=df.Survived,
    )

    train: pd.DataFrame = splits[0]
    test: pd.DataFrame = splits[1]

    train.to_csv("input/titanic/train_sampled.csv")
    test.to_csv("input/titanic/test_sampled.csv")
