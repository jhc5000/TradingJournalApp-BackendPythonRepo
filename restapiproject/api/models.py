# Create your models here.
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class TradingJournalEntry(models.Model):
    Date=models.DateField()
    Symbol=models.CharField(max_length=255)
    Market_Bias=models.CharField(max_length=255,verbose_name="Market Bias")
    Setup_Strategy=models.CharField(max_length=255,verbose_name="Setup Strategy")
    Option_Type=models.CharField(max_length=255,verbose_name="Option Type")
    Strike=models.CharField(max_length=255,verbose_name="Strike")
    Entry=models.DecimalField(max_digits=6, decimal_places=2)
    Stop=models.DecimalField(max_digits=6, decimal_places=2)
    Target=models.DecimalField(max_digits=6, decimal_places=2)
    Outcome=models.DecimalField(max_digits=6, decimal_places=2)
    Rule_Adherence=models.CharField(max_length=255,verbose_name="Rule Adherence")
    Entry_Quality=models.PositiveIntegerField(verbose_name="Entry Quality")
    Emotional_State=models.CharField(max_length=255,verbose_name="Emotional State")
    Why_this_trade=models.CharField(max_length=255,verbose_name="Why this trade")
    Chart_Screenshot=models.CharField(max_length=255,verbose_name="Chart Screenshot")
    def __str__(self):
        return str(self.Date)
   

       