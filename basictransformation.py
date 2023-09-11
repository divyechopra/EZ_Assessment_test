import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
import pandas as pd

def preprocess_text(file_path, max_seq_length=10):
    nltk.download('punkt')
    nltk.download('stopwords')
    
    # Read the CSV file
    df = pd.read_csv(file_path)
    # df = df.head(10)
    
    # Text Cleaning
    def clean_text(text):
        # Remove special characters and punctuation
        text = ''.join([char for char in text if char.isalnum() or char.isspace()])
        return text

    df['Text'] = df['Text'].apply(clean_text)

    # Tokenization and Lowercasing
    df['Tokenized_Text'] = df['Text'].apply(lambda x: word_tokenize(x.lower()))

    # Stop Word Removal
    stop_words_en = set(stopwords.words('english'))
    stop_words_ar = set(stopwords.words('arabic'))

    def remove_stopwords(tokens, lang):
        if lang == 'en':
            return [word for word in tokens if word not in stop_words_en]
        elif lang == 'ar':
            return [word for word in tokens if word not in stop_words_ar]

    df['Tokenized_Text'] = df.apply(lambda row: remove_stopwords(row['Tokenized_Text'], row['Language']), axis=1)

    # Stemming (for English only)
    stemmer_en = SnowballStemmer('english')

    def stem_text(tokens, lang):
        if lang == 'en':
            return [stemmer_en.stem(word) for word in tokens]
        else:
            return tokens

    df['Tokenized_Text'] = df.apply(lambda row: stem_text(row['Tokenized_Text'], row['Language']), axis=1)

    # Padding/Truncation (for a fixed sequence length)
    def pad_or_truncate(tokens):
        if len(tokens) < max_seq_length:
            return tokens + [''] * (max_seq_length - len(tokens))
        else:
            return tokens[:max_seq_length]

    df['Tokenized_Text'] = df['Tokenized_Text'].apply(pad_or_truncate)
    df['Tokenized_Text'] = df['Tokenized_Text'].apply(lambda x: ' '.join(x))
    return df[['Language', 'Tokenized_Text']]

