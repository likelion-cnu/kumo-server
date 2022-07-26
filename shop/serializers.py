from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Coupon, Review
from accounts.models import ShopUser, User


class QRcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = [
            "writer", "shopname"
        ]


class ShopUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "user", "shop_name", "shop_phone_num", "shop_location", "shop_introduction", "shop_sector"
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "review_star", "review_photo", "review_caption"
        ]