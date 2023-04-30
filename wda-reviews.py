# GooglePlayStore key words and topics

f1=open("GooglePlayStoreDivvyReviews.csv",encoding="UTF-8")
data1=pd.read_csv(f1)
review1=list(data1["content"])
import nltk
token_d11 = [nltk.word_tokenize(doc) for doc in review1]
from nltk.corpus import stopwords
tokenlower1=[[w.lower() for w in doc] for doc in token_d11]
stop_words_removed1 = [[token for token in doc if not token in
stopwords.words('english') if token.isalpha()] for doc in tokenlower1]
stop_words_removed11=[[token.replace("bike","").replace("divvy","") for token in doc] for doc in stop_words_removed1]
lemmatizer1 = nltk.stem.WordNetLemmatizer()
lemmatized_token_d11 =[" ".join([lemmatizer1.lemmatize(j) for j in i ]) for i in stop_words_removed11]
#from sklearn.feature_extraction.text import CountVectorizer
#remove stop words, convert documents to a matrix of token counts including uni-gram and bi-gram.
#minimal document frequency for each term is 5
v11 = CountVectorizer(stop_words='english', ngram_range=(2, 3), min_df=6)
x1=v11.fit_transform(lemmatized_token_d11)

#get topics
terms1 = v11.get_feature_names()
from sklearn.decomposition import LatentDirichletAllocation
#use sklearn to assign topics for each review
lda1 = LatentDirichletAllocation(n_components=4,max_iter=200, random_state = 999).fit(x1)
lda_topics1=lda1.transform(x1)

for topic_idx, topic in enumerate(lda1.components_):
    print("Topic %d:" % (topic_idx))
    print(" ".join([terms1[i] for i in topic.argsort()[:-5-1:-1]]))

#get key words
from sklearn.feature_extraction.text import TfidfTransformer
transformer1=TfidfTransformer()
tfidf1=transformer1.fit_transform(x1)
word1=v11.get_feature_names()
weight1=tfidf1.toarray().sum(axis=0)
data11={"word":word1,"tfidf":weight1.tolist()}
df=pd.DataFrame(data11)
print(df.sort_values(by='tfidf',ascending=False).head(10))





# IOSappPlayStore key words and topics
f2=open("iOSAppStoreDivvyReviews.csv",encoding="UTF-8")
data2=pd.read_csv(f2)
review2=list(data2["review"])
import nltk
token_d2 = [nltk.word_tokenize(doc) for doc in review2]
from nltk.corpus import stopwords
tokenlower2=[[w.lower() for w in doc] for doc in token_d2]
stop_words_removed2 = [[token for token in doc if not token in stopwords.words('english') if token.isalpha()] for doc in tokenlower2]
stop_words_removed22=[[token.replace("bike","").replace("divvy","") for token in doc] for doc in stop_words_removed2]
lemmatizer2 = nltk.stem.WordNetLemmatizer()
lemmatized_token_d2 =[" ".join([lemmatizer2.lemmatize(j) for j in i]) for i in stop_words_removed22]
#from sklearn.feature_extraction.text import CountVectorizer
#remove stop words, convert documents to a matrix of token counts including uni-gram and bi-gram.
#minimal document frequency for each term is 5
v2 = CountVectorizer(stop_words='english', ngram_range=(2, 3), min_df=6)
x2=v2.fit_transform(lemmatized_token_d2)

#GET TOPICS
terms2 = v2.get_feature_names()
from sklearn.decomposition import LatentDirichletAllocation
#use sklearn to assign topics for each review
lda2 = LatentDirichletAllocation(n_components=4,max_iter=200, random_state = 999).fit(x2)
lda_topics2=lda2.transform(x2)

for topic_idx, topic in enumerate(lda2.components_):
    print("Topic %d:" % (topic_idx))
    print(" ".join([terms2[i] for i in topic.argsort()[:-5-1:-1]]))


#GET KEY WORDS
from sklearn.feature_extraction.text import TfidfTransformer
transformer2=TfidfTransformer()
tfidf2=transformer2.fit_transform(x2)
word2=v2.get_feature_names()
weight2=tfidf2.toarray().sum(axis=0)
data22={"word":word2,"tfidf":weight2.tolist()}
df=pd.DataFrame(data22)
print(df.sort_values(by='tfidf',ascending=False).head(10))


# TRIPADVISOR key words and topics
f3=open("Divvy_Tripadvisor.csv")
names=["name","location","contributions","Rating_bubbles","Brief","Ride date","Date of review","Review"]
data3=pd.read_csv(f3,names=names)
review3=list(data3["Review"])

import nltk
token_d3 = [nltk.word_tokenize(doc) for doc in review3]
from nltk.corpus import stopwords
tokenlower3=[[w.lower() for w in doc] for doc in token_d3]
stop_words_removed3 = [[token for token in doc if not token in stopwords.words('english') if token.isalpha()] for doc in tokenlower3]
stop_words_removed32=[[token.replace("bike","").replace("divvy","") for token in doc] for doc in stop_words_removed3]
lemmatizer3 = nltk.stem.WordNetLemmatizer()
lemmatized_token_d3 =[" ".join([lemmatizer3.lemmatize(j) for j in i]) for i in stop_words_removed32]
#from sklearn.feature_extraction.text import CountVectorizer
#remove stop words, convert documents to a matrix of token counts including uni-gram and bi-gram.
#minimal document frequency for each term is 5
v3 = CountVectorizer(stop_words='english', ngram_range=(2, 3), min_df=4)
x3=v3.fit_transform(lemmatized_token_d3)

#GET TOPICS
terms3 = v3.get_feature_names()
from sklearn.decomposition import LatentDirichletAllocation
#use sklearn to assign topics for each review
lda3 = LatentDirichletAllocation(n_components=4,max_iter=200, random_state = 999).fit(x3)
lda_topics3=lda3.transform(x3)

for topic_idx, topic in enumerate(lda3.components_):
    print("Topic %d:" % (topic_idx))
    print(" ".join([terms3[i] for i in topic.argsort()[:-5-1:-1]]))

#GET KEYWORDS
from sklearn.feature_extraction.text import TfidfTransformer
transformer3=TfidfTransformer()
tfidf3=transformer3.fit_transform(x3)
word3=v3.get_feature_names()
weight3=tfidf3.toarray().sum(axis=0)
data32={"word":word3,"tfidf":weight3.tolist()}
df=pd.DataFrame(data32)
print(df.sort_values(by='tfidf',ascending=False).head(10))


# EBIKE REVIEW key words and topics
import pandas as pd
data = pd.read_excel("reviewsebike.xlsx",engine='openpyxl')
review=list(data["Review"])

import nltk
token_d1 = [nltk.word_tokenize(doc) for doc in review]
from nltk.corpus import stopwords
tokenlower=[[w.lower() for w in doc] for doc in token_d1]
stop_words_removed = [[token for token in doc if not token in stopwords.words('english') if token.isalpha()] for doc in tokenlower]
stop_words_removed1=[[token.replace("bike","").replace("divvy","") for token in doc] for doc in stop_words_removed]
lemmatizer = nltk.stem.WordNetLemmatizer()
lemmatized_token_d =[" ".join([lemmatizer.lemmatize(j) for j in i]) for i in stop_words_removed1]
from sklearn.feature_extraction.text import CountVectorizer
#remove stop words, convert documents to a matrix of token counts including uni-gram and bi-gram.
#minimal document frequency for each term is 5
v4 = CountVectorizer(stop_words='english', ngram_range=(2, 3), min_df=4)
x4=v4.fit_transform(lemmatized_token_d)

#GET TOPICS
terms4 = v4.get_feature_names()
from sklearn.decomposition import LatentDirichletAllocation
#use sklearn to assign topics for each review
lda4 = LatentDirichletAllocation(n_components=4,max_iter=200, random_state = 999).fit(x4)
lda_topics4=lda4.transform(x4)

for topic_idx, topic in enumerate(lda4.components_):
    print("Topic %d:" % (topic_idx))
    print(" ".join([terms4[i] for i in topic.argsort()[:-5-1:-1]]))

#GET KEYWORDS
from sklearn.feature_extraction.text import TfidfTransformer
transformer4=TfidfTransformer()
tfidf4=transformer4.fit_transform(x4)
word4=v4.get_feature_names()
weight4=tfidf4.toarray().sum(axis=0)
data41={"word":word4,"tfidf":weight4.tolist()}
df=pd.DataFrame(data41)
print(df.sort_values(by='tfidf',ascending=False).head(10))

# APPREVIEW key words and topics
f5=open("appreview.csv",encoding="UTF-8")
data5=pd.read_csv(f5)
review5=list(data5["Review"])

import nltk
token_d5 = [nltk.word_tokenize(doc) for doc in review5]
from nltk.corpus import stopwords
tokenlower5=[[w.lower() for w in doc] for doc in token_d5]
stop_words_removed5 = [[token for token in doc if not token in stopwords.words('english') if token.isalpha()] for doc in tokenlower5]
stop_words_removed55=[[token.replace("bike","").replace("divvy","") for token in doc] for doc in stop_words_removed5]
lemmatizer5 = nltk.stem.WordNetLemmatizer()
lemmatized_token_d5 =[" ".join([lemmatizer5.lemmatize(j) for j in i]) for i in stop_words_removed55]
#from sklearn.feature_extraction.text import CountVectorizer
#remove stop words, convert documents to a matrix of token counts including uni-gram and bi-gram.
#minimal document frequency for each term is 5
v5 = CountVectorizer(stop_words='english', ngram_range=(2, 3), min_df=6)
x5=v5.fit_transform(lemmatized_token_d5)

#GET TOPICS
terms5 = v5.get_feature_names()
from sklearn.decomposition import LatentDirichletAllocation
#use sklearn to assign topics for each review
lda5 = LatentDirichletAllocation(n_components=4,max_iter=200, random_state = 999).fit(x5)
lda_topics5=lda5.transform(x5)

for topic_idx, topic in enumerate(lda5.components_):
    print("Topic %d:" % (topic_idx))
    print(" ".join([terms5[i] for i in topic.argsort()[:-5-1:-1]]))


#GET KEYWORDS
from sklearn.feature_extraction.text import TfidfTransformer
transformer2=TfidfTransformer()
tfidf2=transformer2.fit_transform(x2)
word2=v2.get_feature_names()
weight2=tfidf2.toarray().sum(axis=0)
data22={"word":word2,"tfidf":weight2.tolist()}
df=pd.DataFrame(data22)
print(df.sort_values(by='tfidf',ascending=False).head(10))

