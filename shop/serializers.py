from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Coupon, Review, Payment, Review_Comment
from accounts.models import ShopUser, User, CustomerUser

# QR코드 Serializer
class QRcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = [
            "writer", "shopname"
        ]


# Shop User Serializer
class ShopUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopUser
        fields = [
            "user", "shop_logo", "shop_image1","shop_image2","shop_image3","shop_image4", "shop_name", "shop_phone_num", "shop_location", "shop_introduction", "shop_sector"
        ]


# Shop 프로필에서 Shop User 데이터 
class ShopProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopUser
        fields = [
            "user", "shop_name", "is_Premium"
        ]


# Shop 프로필 Serializer
class ShopProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
            model = ShopUser
            fields = [
                "shop_name", "shop_phone_num"
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
            "writer", "shopname", "shop_name"
        ]


class CouponeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = [
            "coupon_num", "stamp_num", "created_at"
        ]
