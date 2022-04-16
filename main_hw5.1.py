import sklearn as sklearn
import sklearn as sklearn
import sklearn.datasets as datasets
import sklearn.utils
from sklearn.linear_model import LinearRegression

print('scikit-learn  version: ',sklearn.__version__)


class CreationalPatternName:
    def __init__(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def get_subsample(self, df_share):
        # <YOUR CODE HERE>
        """
        1. Copy train dataset
        2. Shuffle data (don't miss the connection between X_train and y_train)
        3. Return df_share %-subsample of X_train and y_train
        """
        x_train_copy = self.X_train.copy()
        y_train_copy = self.y_train.copy()
        x_shuffled, y_shuffled = sklearn.utils.shuffle(x_train_copy, y_train_copy)

        return sklearn.utils.resample(x_shuffled, y_shuffled, n_samples=df_share)


if __name__ == "__main__":
    # <YOUR CODE HERE>
    """
    1. Load iris dataset
    2. Shuffle data and divide into train / test.
    """
    ds = datasets.load_iris()

    print(ds.keys())

    X_train = ds['data']
    y_train = ds['target']

    print(X_train.shape)

    pattern_item = CreationalPatternName(X_train, y_train)
    for df_share in range(10, 101, 10):
        curr_X_train, curr_y_train = pattern_item.get_subsample(df_share)
        # <YOUR CODE HERE>
        """
        1. Preprocess curr_X_train, curr_y_train in the way you want
        2. Train Linear Regression on the subsample
        3. Save or print the score to check how df_share affects the quality
        """
        model = sklearn.linear_model.LinearRegression()
        reg = model.fit(curr_X_train, curr_y_train)
        score = reg.score(curr_X_train, curr_y_train)
        print(f'Sample size: {df_share:3} Score  {score:.4}')
