from django.db import models
from post.models import House, Auto
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):
    body = models.TextField()
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name='auto_comments', null=True, blank=True, verbose_name='Авто')
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house_comments', null=True, blank=True, verbose_name='Дом')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f' comment from {self.author} to {self.auto if self.auto else self.house}'

class Rating(models.Model):
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name='auto_ratings', null=True, blank=True, verbose_name='Авто')
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house_ratings', null=True, blank=True, verbose_name='Дом')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')

    def __str__(self):
        return f'{self.rating} - {self.auto if self.auto else self.house}'

class Like(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name='auto_likes', null=True, blank=True, verbose_name='Авто')
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house_likes', null=True, blank=True, verbose_name='Дом')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f'{self.auto if self.auto else self.house} liked by {self.author}'
