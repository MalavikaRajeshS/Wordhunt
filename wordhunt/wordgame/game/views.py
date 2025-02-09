from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import WordLevel, WordAnswer
import random

def home(request):
    return render(request, 'index.html')

def get_word(request, level):
    words = WordLevel.objects.filter(level=level)
    if words.exists():
        word = random.choice(words)
        return JsonResponse({'word': word.word})
    return JsonResponse({'error': 'No words found'})


def check_answers(request):
    if request.method == "POST":
        print("🔹 Request Data:", request.POST)  # Debugging
        print("🔹 User Words List:", request.POST.getlist("user_words[]"))  # Debugging

        word = request.POST.get("word")  # Get the word
        user_words = request.POST.getlist("user_words[]")  # Get the list of user words

        try:
            word_level = WordLevel.objects.get(word=word)
            correct_answers = list(WordAnswer.objects.filter(word_level=word_level).values_list("valid_word", flat=True))

            print(f"✅ Correct Answers for '{word}':", correct_answers)  # Debugging
            print(f"✅ User Words Submitted:", user_words)  # Debugging

            # Check if ALL user words are correct
            if all(user_word in correct_answers for user_word in user_words):
                return JsonResponse({"status": "passed"})
            else:
                return JsonResponse({"status": "failed", "correct_answers": correct_answers})  

        except WordLevel.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Word not found!"})

    return JsonResponse({"status": "error", "message": "Invalid request"})


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt  # This disables CSRF protection for testing (not recommended in production)
def check_answers(request):
    if request.method == "POST":
        return JsonResponse({"message": "Answer received!"})

