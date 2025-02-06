# Sentiment Analysis and Image Classification Web App

This is a Django web application that integrates two machine learning models:  

- **Sentiment Analysis:** Analyzes the emotional tone of a given text (positive, negative, or neutral).  
- **Image Classification:** Predicts the content of an uploaded image using a pre-trained MobileNet model.  

## 🚀 Features  

### 📖 Sentiment Analysis  
- Users can input text and get the sentiment (positive, negative, or neutral) along with a confidence score.  

### 🖼️ Image Classification  
- Users can upload an image and get the top 3 predicted categories (e.g., "Labrador Retriever") along with confidence scores.  

### 🎨 User-Friendly Interface  
- Separate pages for sentiment analysis and image classification.  
- Easy navigation between the two features.  

## 🛠️ Technologies Used  

### **Backend**  
- Django (Python web framework)  
- Hugging Face Transformers (for sentiment analysis)  
- TensorFlow (for image classification)  

### **Frontend**  
- HTML, CSS  

### **Database**  
- SQLite (default Django database)  

## 📌 How It Works  

### **Sentiment Analysis**  
1. The user enters text into a form.  
2. The text is processed by a pre-trained sentiment analysis model from Hugging Face's transformers library.  
3. The sentiment (positive, negative, or neutral) and confidence score are displayed.  

### **Image Classification**  
1. The user uploads an image.  
2. The image is processed by a pre-trained MobileNet model from TensorFlow.  
3. The top 3 predicted categories and their confidence scores are displayed.  
