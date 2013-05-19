from django.db import models

class Race(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=200)
    market_id = models.IntegerField(unique=True)
    exchange = models.IntegerField(max_length=1)
    location = models.CharField(max_length=200)
    open_time = models.DateTimeField()
    market_time = models.DateTimeField()
    matched_amount = models.DecimalField(max_digits=19, decimal_places=2)

class Horse(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=200, unique=True)
    horse_id = models.IntegerField(unique=True)

class RaceData(models.Model):
    def __unicode__(self):
        return self.time_id
    horse = models.ForeignKey(Horse)
    race = models.ForeignKey(Race)
    time_id = models.IntegerField(unique=True)
    bp1 = models.DecimalField(max_digits=6, decimal_places=2)
    bv1 = models.DecimalField(max_digits=6, decimal_places=2)
    bp2 = models.DecimalField(max_digits=6, decimal_places=2)
    bv2 = models.DecimalField(max_digits=6, decimal_places=2)
    lp1 = models.DecimalField(max_digits=6, decimal_places=2)
    lv1 = models.DecimalField(max_digits=6, decimal_places=2)
    lp2 = models.DecimalField(max_digits=6, decimal_places=2)
    lv2 = models.DecimalField(max_digits=6, decimal_places=2)


