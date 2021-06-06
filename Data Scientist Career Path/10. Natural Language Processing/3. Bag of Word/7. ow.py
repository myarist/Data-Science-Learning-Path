import nltk, re, random
from nltk.tokenize import word_tokenize
from collections import defaultdict, deque, Counter
from document import oscar_wilde_thoughts

# Change sequence_length:
sequence_length = 1

class MarkovChain:
  def __init__(self):
    self.lookup_dict = defaultdict(list)
    self.most_common = []
    self._seeded = False
    self.__seed_me()

  def __seed_me(self, rand_seed=None):
    if self._seeded is not True:
      try:
        if rand_seed is not None:
          random.seed(rand_seed)
        else:
          random.seed()
        self._seeded = True
      except NotImplementedError:
        self._seeded = False
    
  def add_document(self, str):
    preprocessed_list = self._preprocess(str)
    self.most_common = Counter(preprocessed_list).most_common(50)
    pairs = self.__generate_tuple_keys(preprocessed_list)
    for pair in pairs:
      self.lookup_dict[pair[0]].append(pair[1])
  
  def _preprocess(self, str):
    cleaned = re.sub(r'\W+', ' ', str).lower()
    tokenized = word_tokenize(cleaned)
    return tokenized

  def __generate_tuple_keys(self, data):
    if len(data) < sequence_length:
      return

    for i in range(len(data) - 1):
      yield [ data[i], data[i + 1] ]
      
  def generate_text(self, max_length=50):
    context = deque()
    output = []
    if len(self.lookup_dict) > 0:
      self.__seed_me(rand_seed=len(self.lookup_dict))
      chain_head = [list(self.lookup_dict)[0]]
      context.extend(chain_head)
      if sequence_length > 1:
        while len(output) < (max_length - 1):
          next_choices = self.lookup_dict[context[-1]]
          if len(next_choices) > 0:
            next_word = random.choice(next_choices)
            context.append(next_word)
            output.append(context.popleft())
          else:
            break
        output.extend(list(context))
      else:
        while len(output) < (max_length - 1):
          next_choices = [word[0] for word in self.most_common]
          next_word = random.choice(next_choices)
          output.append(next_word)
    return " ".join(output)

my_markov = MarkovChain()
my_markov.add_document(oscar_wilde_thoughts)
random_oscar_wilde = my_markov.generate_text()
print(random_oscar_wilde)