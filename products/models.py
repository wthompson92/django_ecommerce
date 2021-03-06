from django.db import models
import random
# def upload_image_path(instance, filename):
#     print(instance)
#     print(filename)
#     new_file_name = random.randint
#     return
class Product(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField()
    price = models.DecimalField(decimal_places = 2, max_digits = 10, null = True)
    image = models.FileField(upload_to = 'products/', null = True, blank = True )

    def __str__(self):
        return self.title
