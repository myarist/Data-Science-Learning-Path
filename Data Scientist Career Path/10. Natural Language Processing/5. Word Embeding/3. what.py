import spacy

# load word embedding model
nlp = spacy.load('en')

# define word embedding vectors
happy_vec = nlp('happy').vector
print(happy_vec)
sad_vec = nlp('sad').vector
print(sad_vec)
angry_vec = nlp('angry').vector
print(angry_vec)

# find vector length here
vector_length = len(happy_vec)
print(vector_length)