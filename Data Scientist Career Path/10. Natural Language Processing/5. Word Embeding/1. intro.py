import spacy
from scipy.spatial.distance import cosine

# load model
nlp = spacy.load('en')

# define vectors
summer_vec = nlp("summer").vector
winter_vec = nlp("winter").vector

# compare similarity
print(f"The cosine distance between the word embeddings for 'summer' and 'winter' is: {cosine(summer_vec, winter_vec)}\n")

# define vectors
mustard_vec = nlp("mustard").vector
amazing_vec = nlp("amazing").vector

# compare similarity
print(f"The cosine distance between the word embeddings for 'mustard' and 'amazing' is: {cosine(mustard_vec, amazing_vec)}\n")

# display word embeddings
# print(f"'summer' in vector form: {summer_vec}")
# print(f"'winter' in vector form: {winter_vec}")
# print(f"'mustard' in vector form: {mustard_vec}")
# print(f"'amazing' in vector form: {amazing_vec}")