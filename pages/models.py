from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"
        
        
        
class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="blogs")
    short_description = models.TextField()
    long_description = models.TextField()
    author = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"
        


class InfoModel(models.Model):
    description = models.TextField()
    man = models.CharField(max_length=255)
    work = models.CharField(max_length=255)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.man

    class Meta:
        verbose_name = "info"
        verbose_name_plural = "infoes"
        
class kitModel(models.Model):
    photo = models.ImageField(upload_to="pages")
    title = models.CharField(max_length=255)
    price = models.FloatField()
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "kit"
        verbose_name_plural = "kits"