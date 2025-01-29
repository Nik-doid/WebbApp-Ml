from django.shortcuts import render
from django.core.files.storage import default_storage
from .ml_model import analyze_sentiment
from .image_model import classify_image

# Sentiment Analysis View
def sentiment_analysis(request):
    if request.method == "POST":
        text = request.POST.get("text", "")
        sentiment, confidence = analyze_sentiment(text)
        return render(request, "sentiment_analyzer/sentiment_analysis.html", {
            "sentiment": sentiment,
            "confidence": confidence,
            "text": text,
        })
    return render(request, "sentiment_analyzer/sentiment_analysis.html")

# Image Classification View
def image_classification(request):
    if request.method == "POST":
        image_file = request.FILES["image"]
        file_path = default_storage.save(image_file.name, image_file)
        results = classify_image(file_path)
        return render(request, "sentiment_analyzer/image_classification.html", {
            "image_results": results,
            "image_path": file_path,
        })
    return render(request, "sentiment_analyzer/image_classification.html")