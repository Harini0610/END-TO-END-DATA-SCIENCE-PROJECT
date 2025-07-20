# END-TO-END-DATA-SCIENCE-PROJECT

COMPANY: CODTECH IT SOLUTIONS

NAME: HARINI P

INTERN ID:CT04DH454

DOMAIN: DATA SCIENCE

DURATION: 4 WEEKS

MENTOR: NEELA SANTHOSH KUMAR

# DESCRIPTION

EDITOR USED: VISUAL STUDIOS

As part of Task 3 in my Data Science Internship, I developed a complete Fake News Detection system using Natural Language Processing (NLP) and Machine Learning, and deployed it as a web application using Flask. This project was especially rewarding because it involved building a real-world solution from scratch — starting from raw data to deploying a usable web app interface — all using Python scripts.

The dataset I used for this project was the fake_or_real_news.csv dataset, which contains over 6000 news articles labeled either FAKE or REAL. Each entry consists of the news title, the full article text, and the classification label. This dataset is publicly available and can be downloaded from Kaggle:
🔗 https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

To build the backend logic, I used core Python libraries such as pandas for loading and handling the dataset, and scikit-learn for text preprocessing and machine learning. I started by reading the dataset in a Python file (model_training.py), selecting the relevant text column, and converting it into numerical form using TfidfVectorizer, which transforms the text into weighted word frequency vectors suitable for model training.

I chose Logistic Regression as the classification algorithm, which is simple yet powerful for binary text classification tasks. Once trained, the model was evaluated and then saved along with the TfidfVectorizer using the pickle module. These saved files (fake_news_model.pkl and tfidf_vectorizer.pkl) are then loaded by the Flask app at runtime for making predictions.

The web interface was created using Flask and a simple HTML template (index.html). The layout includes:

1. A styled textarea where users can paste a news article

2. A “Check” button that returns the model’s prediction (Fake or Real)

3. A “Clear” button to reset the textarea after submission

I applied CSS to ensure the form appears beautifully centered on the page with smooth spacing and padding. The form retains the user’s input after a prediction is made, enhancing user experience.

* Model Building
Libraries Used: pandas, sklearn, nltk, Flask, HTML/CSS
Feature Extraction: TF-IDF (Term Frequency–Inverse Document Frequency)
Model: Logistic Regression
Evaluation: Accuracy, Confusion Matrix
Deployment: Flask App

This task taught me how to handle the full machine learning pipeline — not just training a model, but actually integrating it into an application that others can interact with. Working purely with .py files made the deployment feel very practical and production-like. I also learned how to handle form submissions using Flask routes, render dynamic content using Jinja2, and build a maintainable project folder structure with separate files for training, prediction, and templates.

This kind of Fake News Detection model has broad applications today — from journalism and social media platforms to government fact-checking tools. The techniques used here can easily be extended to more advanced NLP models like LSTM, BERT, or integrated into larger content moderation systems.

In conclusion, Task 3 was a complete and deeply educational experience for me. It reinforced my Python programming skills, gave me practical exposure to deploying models via Flask, and helped me understand the end-to-end lifecycle of an AI solution. This project gave me both confidence and motivation to take on more advanced machine learning and deployment challenges in the future.

# OUTPUT

