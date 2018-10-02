from django.db import models

class Files(models.Model):
    name = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Kullanıcı")
    files = models.CharField(verbose_name ="Dosya",max_length=50)

    def __str__(self):
        return self.files
