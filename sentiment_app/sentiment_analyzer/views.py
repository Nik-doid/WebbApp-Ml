from django.shortcuts import render
from ml_model import analyze_sentiment

def home(request):
    if request.method == "POST":
        text = request.POST.get("text", "")
        sentiment, confidence = analyze_sentiment(text)
        return render(request, "sentiment_analyzer/home.html", {
            "sentiment": sentiment,
            "confidence": confidence,
            "text": text,
        })
    return render(request, "sentiment_analyzer/home.html")