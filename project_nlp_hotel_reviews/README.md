
# Project: NLP Analysis of European Luxury Hotel Reviews

This project demonstrates a complete Natural Language Processing (NLP) workflow, transforming over 500,000 unstructured hotel reviews into actionable business intelligence.

### The Analytical Process

The core of this project was a multi-stage NLP pipeline designed to extract meaning from raw text:

1.  **Data Preparation:** The raw dataset was cleaned, with `Positive_Review` and `Negative_Review` columns being merged into a single, unified text field for holistic analysis.
2.  **Sentiment Analysis:** The **VADER** sentiment analysis library was used to generate a `sentiment_score` for each of the 515,000 reviews. This score was validated against the human-provided `reviewer_score`, showing a strong positive correlation and confirming its accuracy.
3.  **Text Preprocessing:** A sophisticated preprocessing pipeline was built using `spaCy` to clean the text by lowercasing, removing stop words and punctuation, and reducing words to their root form (lemmatization).
4.  **Keyword & Theme Extraction:** Using `scikit-learn`'s `CountVectorizer`, the most common and impactful two-word phrases (bigrams) were extracted from the cleaned positive and negative reviews.

### Key Actionable Insights

The analysis of the most frequent phrases revealed clear, consistent themes:

*   **Top Drivers of Positive Reviews:**
    1.  **Location:** Overwhelmingly the most praised aspect, with phrases like "great location" and "good location" dominating.
    2.  **Staff:** Excellent service is the second key driver, with "friendly staff" and "helpful staff" appearing frequently.
    3.  **Room Quality:** Core attributes like "clean room" and "comfortable bed" are also crucial.

*   **Top Drivers of Negative Reviews:**
    1.  **Room Issues:** The most common complaints were highly specific and operational, led by **"small room"** and "room small".
    2.  **Amenity Gaps:** Phrases like "tea coffee" and "mini bar" appearing in negative reviews suggest that the absence of expected basic amenities is a significant source of guest dissatisfaction.

This analysis provides a clear, data-driven priority list for hotel management to enhance guest experience by focusing on room improvements while continuing to leverage their key strengths in location and service.

**The full analysis can be found in the notebook:**
*   [View the Notebook](./Hotel_Review_NLP_EDA.ipynb)
*   [View the Clean HTML Report](https://htmlpreview.github.io/?https://raw.githubusercontent.com/jalhane88/Data-Analysis-Portfolio/refs/heads/main/project_nlp_hotel_reviews/Hotel_Review_NLP_EDA.html)
