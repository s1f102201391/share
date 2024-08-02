import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import POSStopFilter, LowerCaseFilter
from IPython.core.display import display

csv_in = 'dogs.csv'
df = pd.read_csv(csv_in, skiprows=0, delimiter=',', header=0,encoding='shift-jis')
print('Read {} train data'.format(df.shape[0]))

X_train = df['text']
y_train = df['category']

vectorizer = CountVectorizer(token_pattern='(?u)\\b\\w+\\b')
vectorizer.fit(X_train)

X_train_bow = vectorizer.transform(X_train)
model = MultinomialNB(alpha=1.0)
model.fit(X_train_bow, y_train)

token_filters = [ POSStopFilter(['助詞','助動詞']),
                  LowerCaseFilter(),
                ]
tokenizer = Tokenizer()
analyzer = Analyzer(tokenizer=tokenizer, token_filters=token_filters)

while True:
  s = input('X_text: ')
  if s == '': break
  X_test = [' '.join([t.base_form for t in analyzer.analyze(s)])]
  print(X_test[0])
  X_test_bow = vectorizer.transform(X_test)
  proba = model.predict_proba(X_test_bow)
  results = pd.DataFrame(proba, columns=model.classes_)
  display(results)
  print('Prediction:', model.predict(X_test_bow)[0])
