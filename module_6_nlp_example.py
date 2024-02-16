
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

# Sample text
text = "This is a sample sentence, showing off the stop words filtration."

# Tokenization
tokens = word_tokenize(text)

# Removing stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in tokens if not w.lower() in stop_words]

print(f'Original Tokens: {tokens}')
print(f'Filtered Tokens: {filtered_tokens}')
