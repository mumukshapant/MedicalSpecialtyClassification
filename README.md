# Medical Specialty Classification

Youtube link for Demo : https://www.youtube.com/watch?v=2Ss_knLWzi8&t=1s

## Overview
In this project, we use a variety of machine learning and deep learning techniques to tackle the problem of categorizing medical transcriptions into their corresponding specialties.
We concentrate on well-known yet potent models like Random Forests, Logistic Regression, Support Vector Machine (SVM), RoBERTa, and LSTM. Using these models, we investigate how to strike a balance between interpretability, performance, and model simplicity. Preprocessing the medical transcriptions to extract relevant features, training the models on labeled datasets, and methodically assessing the models' performance using accepted metrics are all part of the suggested methodology. 

Three vectorizers were employed in this project: Word2Vec, ClinicalBERT, and TfidfVectorizer.

For this analysis, five machine learning models were implemented and evaluated, commonly used for text classification : Logisitc Regression, SVM, Random Forest, LSTM and RoBERTa.

With an accuracy of 69%, a weighted average F1-score of 68%, SVM with TF-IDF outperformed the other models in terms of overall performance, demonstrating its efficacy in handling textual features represented by TF-IDF.
