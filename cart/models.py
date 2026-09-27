from django.db import models

class Cart(models.Model):
    session_key = models.CharField(max_length=40, unique=True)

    def __init__(self, request):
        self.session = request.session
        self.session_key = self.session.session_key

    def __str__(self):
        return self.session_key
