import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# reading text file
text = open('read.txt', encoding='UTF-8').read()
#data cleaning
# converting to lowercase
lowercase = text.lower()
# Removing punctuations
cleaned_text = lowercase.translate(str.maketrans('', '', string.punctuation))
tokenized_words=word_tokenize(cleaned_text,"english")

# splitting text into words
#tokenized_words = cleaned_text.split()
"""stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]"""
#tokenized_words = cleaned_text.split() this split() takes lot of time than word_tokenize-it is optimal

# Removing stop words from the tokenized words list
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)
        # NLP Emotion Algorithm
        # 1) Check if the word in the final word list is also present in emotion.txt
        #  - open the emotion file
        #  - Loop through each line and clear it
        #  - Extract the word and emotion using split

        # 2) If word is present -> Add the emotion to emotion_list
        # 3) Finally count each emotion in the emotion list
emotions_list=[]
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word,emotion=clear_line.split(':')

        if word in final_words:
            emotions_list.append(emotion)

print(emotions_list)
w=Counter(emotions_list)
print(w)


def sentiment_analyse(sentiment_text):
    score=SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    neg=score['neg']
    pos=score['pos']
    if neg>pos:
        print("negative sentiment")
    elif pos>neg:
        print("positive sentiment")
    else:
        print("neutral vibe")
sentiment_analyse(cleaned_text)

# Plotting the emotions on the graph
fig,axis1=plt.subplots()
axis1.bar(w.keys(),w.values()) #plt.bar(w.keys(),w.values())
fig.autofmt_xdate() #automatic adjustments
plt.savefig('graph.png')
plt.show()
#maybe use apis to get tweets from twitter but easy w package