import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB, ComplementNB
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import pickle

# Load the dataset
df = pd.read_csv('bbc-text.csv')

X = df['text']
Y = df['category']

# Split the dataset
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=143)

# Define pipelines for the models
pipeMNB = Pipeline([('tfidf', TfidfVectorizer(stop_words='english')), ('clf', MultinomialNB())])
pipeCNB = Pipeline([('tfidf', TfidfVectorizer(stop_words='english', ngram_range=(1, 3))), ('clf', ComplementNB())])
pipeSVC = Pipeline([('tfidf', TfidfVectorizer(stop_words='english', ngram_range=(1, 3))), ('clf', LinearSVC())])

# Train and evaluate each model
pipeMNB.fit(X_train, Y_train)
print(f"MultinomialNB Accuracy: {accuracy_score(Y_test, pipeMNB.predict(X_test)):.2f}")

pipeCNB.fit(X_train, Y_train)
print(f"ComplementNB Accuracy: {accuracy_score(Y_test, pipeCNB.predict(X_test)):.2f}")

pipeSVC.fit(X_train, Y_train)
print(f"LinearSVC Accuracy: {accuracy_score(Y_test, pipeSVC.predict(X_test)):.2f}")

# Save the pipelines
pickle.dump(pipeMNB, open('naive_bayes_model.pkl', 'wb'))
pickle.dump(pipeCNB, open('complement_nb_model.pkl', 'wb'))
pickle.dump(pipeSVC, open('svm_model.pkl', 'wb'))
