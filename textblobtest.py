from textblob import TextBlob
str = open('/Users/stephenholmes/Documents/testoutput1.txt', 'r').read()
blob = TextBlob(str)
blob.tags
