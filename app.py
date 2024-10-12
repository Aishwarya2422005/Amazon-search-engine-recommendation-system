import streamlit as st
import pandas as pd
import nltk
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Set page config (must be the first Streamlit command)
st.set_page_config(page_title="Amazon Product Search", page_icon="🔍", layout="wide")

# Download necessary NLTK data
nltk.download('punkt', quiet=True)

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv('amazon_product.csv')
    return data

data = load_data()

# Define tokenizer and stemmer
stemmer = SnowballStemmer('english')
def tokenize_and_stem(text):
    tokens = nltk.word_tokenize(str(text).lower())
    stems = [stemmer.stem(t) for t in tokens]
    return stems

# Create stemmed tokens column
@st.cache_data
def create_stemmed_tokens(data):
    data['stemmed_tokens'] = data.apply(lambda row: tokenize_and_stem(row['Title'] + ' ' + str(row['Description']) + ' ' + str(row['Category'])), axis=1)
    return data

data = create_stemmed_tokens(data)

# Define TF-IDF vectorizer and cosine similarity function
tfidf_vectorizer = TfidfVectorizer(tokenizer=tokenize_and_stem)
def cosine_sim(text1, text2):
    text1_concatenated = ' '.join(text1)
    text2_concatenated = ' '.join(text2)
    tfidf_matrix = tfidf_vectorizer.fit_transform([text1_concatenated, text2_concatenated])
    return cosine_similarity(tfidf_matrix)[0][1]

# Define search function with sorting
@st.cache_data
def search_products(query, sort_by):
    query_stemmed = tokenize_and_stem(query)
    data['similarity'] = data['stemmed_tokens'].apply(lambda x: cosine_sim(query_stemmed, x))
    results = data.sort_values(by=['similarity'], ascending=False).head(10)[['Title', 'Description', 'Category', 'similarity']]
    
    if sort_by == "Category":
        results = results.sort_values(by=['Category', 'similarity'], ascending=[True, False])
    # "Relevance" is default, no need to sort again
    
    return results

# UI Components
st.title("🛍️ Amazon Product Search")
st.markdown("Discover amazing products with our intelligent search engine!")

# Search input
query = st.text_input("🔎 Enter product name", key="search_input")
search_button = st.button('Search')

# Sidebar
st.sidebar.title("About")
st.sidebar.info("This app uses natural language processing and machine learning to find relevant products based on your search query. It analyzes product titles, descriptions, and categories to provide the most accurate results.")

st.sidebar.title("Options")
sort_by = st.sidebar.selectbox("Sort by", ["Relevance", "Category"])

# Display results
if search_button and query:
    with st.spinner('Searching for products...'):
        results = search_products(query, sort_by)
    
    if not results.empty:
        st.success(f"Found {len(results)} relevant products!")
        for _, row in results.iterrows():
            with st.expander(f"{row['Title']} (Similarity: {row['similarity']:.2f})"):
                st.markdown(f"**Description:** {row['Description']}")
                st.markdown(f"**Category:** {row['Category']}")
    else:
        st.warning("No products found. Try a different search term.")

# Footer
st.markdown("---")
st.markdown("Created with ❤️ by Your Aishwarys S")
