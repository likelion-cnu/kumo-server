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
<<<<<<< HEAD
class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = [
           "bookmark_set"
        ]
=======

>>>>>>> 1bb47f7f23db468e565ee23edbc543b75fe14113

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
<<<<<<< HEAD
    #coupon_num = serializers.CharField(source = Coupon.coupon_num)
    #stamp_num = serializers.CharField(source = Coupon.stamp_num)
    class Meta:
        model = ShopUser
        fields = [
            "shop_name", "shop_phone_num", "shop_sector",  "shop_introduction"
        ]
        #"coupon_num", "stamp_num",
=======
    coupon_num = serializers.CharField(source = Coupon.coupon_num)
    stamp_num = serializers.CharField(source = Coupon.stamp_num)
    class Meta:
        model = ShopUser
        fields = [
            "shop_name", "shop_phone_num", "shop_sector", "coupon_num", "stamp_num", "shop_introduction"
        ]
        
>>>>>>> 1bb47f7f23db468e565ee23edbc543b75fe14113
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
<<<<<<< HEAD
        fields = ["image"]
=======
        field = [ 
            "image" 
            #"bookmark_home", "neighborhood_home"
        ]
>>>>>>> 1bb47f7f23db468e565ee23edbc543b75fe14113
