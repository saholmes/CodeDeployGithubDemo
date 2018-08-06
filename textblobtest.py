from textblob import TextBlob
str = open('/Users/stephenholmes/Documents/testoutput.txt', 'r').read()
blob = TextBlob(str)
blob.tags