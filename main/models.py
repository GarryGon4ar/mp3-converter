from django.db import models


# class AbstractModel(models.Model):
#     created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True, null=True)
#     updated_at = models.DateTimeField(verbose_name='дата обновления', auto_now=True, null=True)
#
#     def __unicode__(self):
#         pass
#
#     def __str__(self):
#         return self.__unicode__()
#
#     class Meta:
#         abstract = True

class Song(models.Model):
    link = models.URLField(max_length=250)
    created_at = models.DateTimeField(verbose_name='request sent', auto_now_add=True, null=True)

    def __unicode__(self):
        return self.link

    def __str__(self):
        return self.__unicode__()

