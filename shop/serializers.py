from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Coupon, Review, Payment, Review_Comment
from accounts.models import ShopUser, User, CustomerUser


class QRcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = [
            "writer", "shopname"
        ]


# Shop User 데이터 입력받기
class ShopUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopUser
        fields = [
            "user", "shop_name", "shop_phone_num", "shop_location", "shop_introduction", "shop_sector"
        ]


# Shop 프로필에서 Shop User 데이터 
class ShopProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopUser
        fields = [
            "user", "shop_name", "is_Premium"
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "writer", "shopname", "review_star", "review_photo", "review_caption"
        ]


class ReviewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review_Comment
        fields = [
            "writer", "post", "message"
        ]


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "writer", "shopname"
        ]


class CouponeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = [
            "writer", "shopname", "coupon_num", "stamp_num", "created_at"
        ]
