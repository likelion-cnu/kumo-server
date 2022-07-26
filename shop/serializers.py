from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Review

class QRcodeSerializer(serializers.ModelSerializer):
    pass


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "review_star", "review_photo", "review_caption"
        ]