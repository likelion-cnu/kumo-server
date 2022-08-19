from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from .validators import validate_score

from accounts.models import User, CustomerUser, ShopUser
# Create your models here.

class BaseModel(models.Model):

    class Meta:
        # 아래 코드를 통해 실제 DB에 적용되지 않고, 추상 클래스로 만들어진다.
        abstract = True


# 쿠폰 테이블
class Coupon(models.Model):
    writer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, related_name="shop_writer")
    shopname = models.ForeignKey(ShopUser, on_delete=models.CASCADE, related_name="shop_shopname")
    shop_name = models.CharField(null=True, max_length=10)
    shop_sector = models.CharField(null=True, max_length=10)
    shop_logo = models.ImageField(null=True)
    coupon_num = models.IntegerField(default=0 ,blank=True)
    stamp_num = models.IntegerField(default=0, blank=True)
    created_at = models.DateField(auto_now_add=True)

    # stamp 개수가 10개 이상이면 0개로 만들고, 쿠폰 개수를 1개 추가
    def save(self,*args,**kwargs):
        self.stamp_num += 1
        if self.stamp_num >= 10:
            self.coupon_num += 1
            self.stamp_num -= 10
        super().save(*args,**kwargs)


# 결제 테이블
class Payment(models.Model):
    payment_at = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    shopname = models.ForeignKey(ShopUser, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=10, null=True)


# 리뷰 테이블
class Review(models.Model):
    writer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, related_name="review_writer")
    shopname = models.ForeignKey(ShopUser, on_delete=models.CASCADE, related_name="review_shopname")
    review_star = models.IntegerField(default=3, validators=[validate_score])
    review_photo = models.ImageField(blank=True)
    review_caption = models.TextField(max_length=100)


# 리뷰 댓글 테이블
class Review_Comment(BaseModel):
    writer = models.ForeignKey(ShopUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Review, on_delete=models.CASCADE)
    message = models.TextField(max_length=200)

    class Meta:
        ordering = ['-id']


# 업주 QnA 테이블
class ShopQna(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)


# 업주 질문 테이블
class ShopQuestion(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)




