from django.db import models

class WordLevel(models.Model):
    LEVEL_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]
    word = models.CharField(max_length=50)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)

    def __str__(self):
        return self.word

class WordAnswer(models.Model):
    word_level = models.ForeignKey(WordLevel, on_delete=models.CASCADE)
    valid_word = models.CharField(max_length=50)

    def __str__(self):
        return self.valid_word
