import pickle
import numpy as np
from os.path import exists
from abc import ABC, abstractmethod
from sklearn.metrics import accuracy_score
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import fetch_20newsgroups
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer



FILE_WEIGTHS_NAME = 'nltk_weights.ppp'

class BaseTagger(ABC):
    @abstractmethod
    def get_tags(self, texts: list[str]) -> list[list[str]]:
        """['Text1', 'Text2', ...] -> [['text1_tag1', 'text1_tag2', ...], ...]"""
        pass


class nltkTagger(BaseTagger):
    def __init__(self):

        self.classifier =LogisticRegression()
        '''
            SGDClassifier(learning_rate='adaptive', eta0=0.1, loss='modified_huber',
                                        penalty='elasticnet',
                                        tol=1e-5, alpha=1e-5, max_iter=50, early_stopping=True,
                                        random_state=4
        '''
        test_data = fetch_20newsgroups(subset='test', shuffle=True)
        train_data = fetch_20newsgroups(subset='train', shuffle=True)

        # print  (train_data)

        self.test_data = test_data
        self.y_test = test_data.target  # _names
        self.x_test = test_data.data
        self.x_train = train_data.data
        self.y_train = train_data.target  # _names
        self.vectorizer = CountVectorizer()

    def fit(self):
        # print (self.x_train.shape)

        if exists(FILE_WEIGTHS_NAME):
            print('Load model weights from ' + FILE_WEIGTHS_NAME)
            self.classifier = pickle.load(open(FILE_WEIGTHS_NAME, 'rb'))
            x_train_vectors = self.vectorizer.fit_transform(self.x_train)
        else:

            x_train_vectors = self.vectorizer.fit_transform(self.x_train)
            x_train_vectors = TfidfTransformer().fit_transform(x_train_vectors)
            print('Fitting  the  model ' + str(x_train_vectors.shape))
            self.classifier.fit(x_train_vectors, self.y_train)
            pickle.dump(self.classifier, open(FILE_WEIGTHS_NAME, 'wb'))

    def transform(self):

        x_test_vectors = self.vectorizer.transform(self.x_test)
        x_test_vectors = TfidfTransformer().fit_transform(x_test_vectors)

        y_pred = self.classifier.predict(x_test_vectors)
        score = accuracy_score(self.y_test, y_pred)
        print(f'Accuracy score {score}')

    def get_tags(self, texts: list[str]) -> list[list[str]]:

        x_test_vectors = self.vectorizer.transform(texts)
        x_test_vectors = TfidfTransformer().fit_transform(x_test_vectors)

        '''
        y_pred = self.classifier.predict(x_test_vectors)
        for i in range(len(y_pred)):
            print(self.test_data.target_names[y_pred[i]])
        '''

        result = []
        y_pred_proba = self.classifier.predict_proba(x_test_vectors)
        for i in range(len(y_pred_proba)):

            amax = np.argmax(y_pred_proba[i])

            result_tag = self.test_data.target_names[amax]
            result_tag_prob  = y_pred_proba[i][amax]
            print(f'predicted value {result_tag:23s} '
                  f'probability = {result_tag_prob:.4f} ')

        result.append(result_tag)
        return result


texts = [
    "In software engineering, a software design pattern is a general, reusable solution to a commonly occurring problem within a given context in software design. It is not a finished design that can be transformed directly into source or machine code. Rather, it is a description or template for how to solve a problem that can be used in many different situations. Design patterns are formalized best practices that the programmer can use to solve common problems when designing an application or system.",
    "Object-oriented design patterns typically show relationships and interactions between classes or objects, without specifying the final application classes or objects that are involved. Patterns that imply mutable state may be unsuited for functional programming languages. Some patterns can be rendered unnecessary in languages that have built-in support for solving the problem they are trying to solve, and object-oriented patterns are not necessarily suitable for non-object-oriented languages.",
    "Design patterns may be viewed as a structured approach to computer programming intermediate between the levels of a programming paradigm and a concrete algorithm.",
    "I sell floppy disks",
    'Oh my God!'
]
tagger = nltkTagger()
tagger.fit()
tagger.transform()
tagger.get_tags(texts)
