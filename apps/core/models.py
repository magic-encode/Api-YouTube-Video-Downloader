from django.db import models


class TelegramUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.BigIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'user profile'
        verbose_name_plural = 'user profiles'


class Videos(models.Model):
    user = models.ForeignKey(TelegramUser, blank=True, null=True, on_delete=models.DO_NOTHING) # noqa
    youtube_link = models.TextField(unique=True, null=True, blank=True)
    file_id = models.TextField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.youtube_link

    class Meta:
        verbose_name = 'user video'
        verbose_name_plural = 'user videos'
