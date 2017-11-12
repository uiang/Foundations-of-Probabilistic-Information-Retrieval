import nltk

with open('stopwords.txt', 'w', encoding='utf-8') as hfile:
    hfile.write('\n'.join(nltk.corpus.stopwords.words('english')))
