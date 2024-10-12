**🛍️ Amazon Product Search Engine**
This is a web application that allows users to search for products using natural language queries. Built with Streamlit, it simulates Amazon-like product search functionality by analyzing product titles, descriptions, and categories to return the most relevant results. The app uses Natural Language Processing (NLP) techniques and machine learning to calculate the relevance of each product to the search query.

**🚀 Features**
Search for Products: Users can input a product name or description, and the app will return the top relevant products based on the search query.
Natural Language Processing (NLP): The app uses tokenization and stemming to preprocess text data for better search results.
TF-IDF Vectorization: Converts product descriptions and search queries into numerical vectors to compute similarities between them.
Cosine Similarity: Measures the similarity between the user query and the product data to rank products.
Sorting Options: Users can sort the search results by relevance (default) or category.
Interactive UI: Built with Streamlit for an intuitive and responsive user experience.

**💻 Demo**
Enter a product name or a query in the search bar.
Click the Search button to retrieve the top 10 relevant products.
Results are ranked by their similarity score and can be sorted by Category.
Expand each result to view the product's Description and Category.
![image](https://github.com/user-attachments/assets/3798ac08-b806-426b-9956-b963d638437d)

![image](https://github.com/user-attachments/assets/19b2cd79-6270-4512-8783-2e240220b5b2)

![image](https://github.com/user-attachments/assets/259b0b23-5fa0-4b91-ada6-3e1a7dcf2295)



**🛠️ Technologies Used**
Streamlit: For building the interactive web application.
Pandas: For handling and manipulating the product dataset.
NLTK: For tokenizing and stemming the text data.
scikit-learn: For applying the TF-IDF Vectorizer and calculating cosine similarity.

**📂 Dataset**
The dataset (amazon_product.csv) contains product details such as:

Title: The name of the product.
Description: A brief description of the product.
Category: The category to which the product belongs.
Note: The dataset must be stored in the same directory as the application, or update the load_data() function with the correct path.

**🔄 How It Works**
Text Preprocessing: The product data is tokenized and stemmed to simplify the text analysis process.
TF-IDF Vectorization: The search query and product data are transformed into numerical vectors using the TF-IDF (Term Frequency-Inverse Document Frequency) approach.
Cosine Similarity: The similarity between the user query and each product is computed using cosine similarity, which helps in ranking the most relevant products.
Sorting: The results are sorted based on the relevance score by default. Users can also choose to sort by product category from the sidebar.
