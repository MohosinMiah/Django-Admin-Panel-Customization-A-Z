from django.db import models


class Country(models.Model):
#    Make Plural Country Model Name
    class Meta:
        verbose_name_plural = "Countries"

    country_name = models.CharField(max_length=200)
    country_short_code = models.CharField(max_length=50)
    country_history = models.TextField(blank = True)


    def __str__(self):

       return self.country_name


class Food(models.Model):
#    Make Plural Food Model Name
    class Meta:
        verbose_name_plural = "Foods"

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    food_item = models.CharField(max_length=200)
    created_at = models.DateField()



    # user pass : BD_WORLD