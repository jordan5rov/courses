from django.db import models


class Trait(models.Model):
    name = models.CharField(max_length=15)
    effect = models.TextField(max_length=150, null=False)


class Champion(models.Model):
    name = models.CharField(max_length=15)
    ability = models.TextField(max_length=150, null=False)
    first_trait = models.ForeignKey(Trait,
                                    on_delete=models.CASCADE,
                                    null=False,
                                    related_name='first_trait')
    second_trait = models.ForeignKey(Trait,
                                     on_delete=models.CASCADE,
                                     null=False,
                                     related_name='second_trait')
    third_trait = models.ForeignKey(Trait,
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True,
                                    related_name='third_trait')

