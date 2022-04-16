from sklearn.model_selection import train_test_split
import sklearn.datasets as datasets
import numpy as np

from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from collections import Counter


class EnsembleFacade:

    def __init__(self, _classifiers) -> None:
        # <YOUR CODE HERE>
        self.classifiers = _classifiers

    def fit(self, _x_trian, _y_train):
        # <YOUR CODE HERE>
        """
        Fit classifiers from the initialization stage
        """

        for classifier in self.classifiers:
            print('Train: ', classifier)
            classifier.fit(_x_trian, _y_train)

    def predict(self, _x_test, _y_test):
        # <YOUR CODE HERE>
        """
        Get predicts from all the classifiers and return
        the most popular answers
        """
        y_preds = []
        for classifier in self.classifiers:
            y_pred = classifier.predict(_x_test)

            accuracy = accuracy_score(_y_test, y_pred)

            y_preds.append(y_pred)
            print(f'Accuracy  for {classifier} is {accuracy:.5} ')


        print ('-'*20)
        cnt = Counter(np.array(y_preds).flatten())
        print(f'Most  popular  answer  is: {cnt.most_common(1)} ')


if __name__ == "__main__":
    # ###<YOUR CODE HERE>
    """
    1. Load iris dataset
    2. Shuffle data and divide into train / test.
    3. Prepare classifiers to initialize <StructuralPatternName> class.
    4. Train the ensemble
    """

    ds = datasets.load_iris()
    X_data = ds['data']
    y_targets = ds['target']
    X_train, X_test, y_train, y_test = train_test_split(X_data, y_targets, test_size=0.3)

    print("Train shape:", X_train.shape)
    print("Test_shape:", X_test.shape)

    classifiers = [SVC(gamma='auto'),
                   RandomForestClassifier(max_depth=5),
                   KNeighborsClassifier(7),
                   GaussianNB()]

    ensemble = EnsembleFacade(classifiers)
    ensemble.fit(X_train, y_train)
    ensemble.predict(X_test, y_test)
