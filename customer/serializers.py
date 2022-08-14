from rest_framework import serializers
from shop.models import Coupon, Review, Review_Comment
from accounts.models import ShopUser, CustomerUser, User

#MYPROFILE
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = [
            "nickname", "level"
        ]

class CouponHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = [
            "writer", "shopname", "created_at", "coupon_num"
        ]

class UserProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = [
            "nickname", "phone_num"
        ]


#MYSTAMP
class MyStampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = [
            "writer", "shopname", "coupon_num", "stamp_num"
        ]

#BOOKMARK
class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = [
           "bookmark_set"
        ]

#NEIGHBORHOOD

#SHOPPROFILE
class ShopbriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopUser
        fields = [
           "shop_name", "shop_phone_num", "shop_sector"
        ]

###SHOPDETAIL
class ShopDetailSerializer(serializers.ModelSerializer):
    coupon_num = serializers.CharField(source = Coupon.coupon_num)
    stamp_num = serializers.CharField(source = Coupon.stamp_num)
    class Meta:
        model = ShopUser
        fields = [
            "shop_name", "shop_phone_num", "shop_sector", "coupon_num", "stamp_num", "shop_introduction"
        ]
        
class ReviewCreatSerializer(serializers.ModelSerializer):
    message = serializers.CharField(source = Review_Comment.message)
    class Meta:
        model = Review
        fields = [
            "review_writer", "review_star", "review_photo", "review_caption", "message"
        ]
    
    class Meta:
        ordering = ['-id']


#SEARCH        
class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopUser
        fields = [
           "shop_name", "shop_phone_num", "shop_sector", 
        ]
    

#HOEM
class HomeSerializer(serializers.ModelSerializer):
#    bookmark_home = models.ImageField(upload_to='', null=True)
#    neighborhood_home = models.ImageField(upload_to='', null=True)
    class Meta:
        model = User
        fields = ["image"]