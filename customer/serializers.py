from urllib import request
from rest_framework import serializers
from shop.models import Coupon, Review, Review_Comment
from accounts.models import ShopUser, CustomerUser, User
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404


#MYPROFILE
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = [
            "nickname", "level", "profile_img"
        ]


#MYPROFILE
class NearShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopUser
        fields = [
            "shop_name", "lat", "lng", "shop_phone_num"
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
            "nickname", "phone_num", "profile_img"
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




# class BookmarkSerializer(serializers.ModelSerializer):
#     shop_name = serializers.SerializerMethodField(method_name='bookmark_shop')
#     class Meta:
#         model = CustomerUser
#         fields = [
#            "bookmark_set", "shop_name"
#         ]

#     def bookmark_shop(self, obj):
#         shop_queryset = ShopUser.objects.get(user=self.bookmark_set)
#         shop_name = ShopNameSerializer(data=request.data)
#         return shop_name


#SHOPPROFILE
class ShopNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopUser
        fields = [
           "shop_name"
        ]




#SHOPPROFILE
class ShopbriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopUser
        fields = [
           "shop_name", "shop_phone_num", "shop_sector"
        ]


###SHOPDETAIL
class ShopDetailSerializer(serializers.ModelSerializer):
    #is_bookmarked = serializers.SerializerMethodField(method_name='bookmark')
    class Meta:
        model = ShopUser
        fields = [
           "bookmarked_set", "shop_name", "shop_phone_num", "shop_sector", "shop_introduction"
        ]
        
    # def bookmark(self, obj):        
    #     #shop = ShopUser.objects.get(shop_name=obj.user.username)      
    #     article = get_object_or_404(ShopUser, user=obj.user.username)
    #     if CustomerUser.objects.filter(bookmark_set=article) is not None:
    #         is_bookmarked = True
    #     else:
    #         is_bookmarked = False
    #     # if shop.user in cu.bookmark_set.all():
    #     #     is_bookmarked = True
    #     # else:
    #     #     is_bookmarked = False
        
    #     return "hi"
    
# #SHOPPROFILE
# class ShopbookmarjSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ShopUser
#         fields = [
#            "is_bookmarked", "shop_phone_num", "shop_sector"
#         ]

# class ShopDetailSerializer(serializers.Serializer):
#     is_bookmarked = serializers.BooleanField()
#     shop_name = serializers.CharField()
#     shop_phone_num = serializers.CharField()
#     shop_sector = serializers.CharField()
#     shop_introduction = serializers.CharField()

#     def create(self, validated_data):
#         return super().create(validated_data)



class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "review_star", "review_photo", "review_caption"
        ]


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