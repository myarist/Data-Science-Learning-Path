import spacy
from scipy.spatial.distance import cosine
from processing import most_common_words, vector_list

# print word and vector representation at index 347
print(most_common_words[347], vector_list[347])

# define find_closest_words
def find_closest_words(word_list, vector_list, word_to_check):
    return sorted(word_list,
                  key=lambda x: cosine(vector_list[word_list.index(word_to_check)], vector_list[word_list.index(x)]))[:10]

# find closest words to food
close_to_food = find_closest_words(most_common_words, vector_list, 'food')
print(close_to_food)

# find closest words to summer
close_to_summer = find_closest_words(most_common_words, vector_list, 'summer')
print(close_to_summer)