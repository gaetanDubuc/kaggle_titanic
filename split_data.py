""" The input has to be split into test and train sets. """
import pandas as pd
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    df = pd.read_csv('./kaggle/input/train.csv')
    train, test = train_test_split(
        df, test_size=0.25, random_state=0, shuffle=True, stratify=df.Survived,)
    pd.DataFrame(train, columns=df.columns).to_csv(
        './kaggle/input/train_sampled.csv')
    pd.DataFrame(test, columns=df.columns).to_csv(
        './kaggle/input/test_sampled.csv')
