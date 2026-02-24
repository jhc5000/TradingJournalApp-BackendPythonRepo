from rest_framework import serializers
from .models import Task
from .models import TradingJournalEntry

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TradingJournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TradingJournalEntry
        fields = '__all__'
        