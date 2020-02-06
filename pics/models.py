from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length =30)
  description = models.CharField(max_length =200)

  @classmethod
  def all_categs(cls):
    categories = cls.objects.all()

    return categories

  def __str__(self):
        return self.name

class Location(models.Model):
  name = models.CharField(max_length=30)

  @classmethod
  def all_locs(cls):
    locations = cls.objects.all()

    return locations

  def __str__(self):
        return self.name


class Picture(models.Model):
  image = models.ImageField(upload_to = 'pictures/')
  pic_name = models.CharField(max_length =30)
  pic_desc =models.CharField(max_length =200)
  category = models.ForeignKey(Category)
  location = models.ForeignKey(Location)

  @classmethod
  def all_pics(cls):
    pics = cls.objects.all()
    return pics

  def __str__(self):
        return self.pic_name