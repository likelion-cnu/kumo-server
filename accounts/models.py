from email.policy import default
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models

import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
import random


# 통합 유저
class User(AbstractUser):
    username = models.CharField(primary_key=True, max_length=10, unique=True)
    nickname = models.CharField(max_length=10, null=True)
    phone_num = models.CharField(
        max_length=13,
        blank=False,
        validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_shop = models.BooleanField(blank=False, null=True)
    image = models.ImageField(upload_to='qrcode', null=True)
    
    # 유저가 회원가입 될 때 QR 코드 생성 구현
    def save(self,*args,**kwargs):
        qrcode_img=qrcode.make(self.username)
        canvas=Image.new("RGB", (300,300),"white")
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        buffer=BytesIO()
        canvas.save(buffer,"PNG")
        self.image.save(f'image{random.randint(0,9999)}.png',File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)


# 고객 유저
class CustomerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_img = models.ImageField(null=True)
    nickname = models.CharField(max_length=10, blank=True)
    points = models.IntegerField(default=0, blank=True)
    level = models.IntegerField(default=0, blank=True)
    phone_num = models.CharField(
        max_length=13,
        blank=False,
        validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")],
    )
    bookmark_set = models.ManyToManyField('ShopUser', blank=True)

    # QR 체크시 고객 유저를 저장함으로서 points 추가
    def save(self,*args,**kwargs):
        self.points += 100
        if self.level == 0:
                if self.points >= 2000:
                    self.level += 1
                    self.points -= 2000
        elif self.level == 1:
                if self.points >= 3000:
                    self.level += 1
                    self.points -= 3000
        else:
            if self.points >= 4000:
                self.level += 1
                self.points -= 4000
        super().save(*args,**kwargs)


# 업주 유저
class ShopUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    shop_name = models.CharField(max_length=15, blank=False)
    shop_runtime = models.CharField(max_length=10, null=True)
    shop_phone_num = models.CharField(
        max_length=13,
        blank=False,
        validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")],
    )
    is_Premium = models.BooleanField(default=False)
    shop_location = models.CharField(blank=False, max_length=100)
    
    shop_logo = models.ImageField(null=True)
    shop_image1 = models.ImageField(null=True)
    shop_image2 = models.ImageField(null=True)
    shop_image3 = models.ImageField(null=True)
    shop_image4 = models.ImageField(null=True)

    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    
    shop_introduction = models.TextField(blank=False)
    shop_sector = models.CharField(blank=False, max_length=10)
    bookmarked_set = models.ManyToManyField('CustomerUser', blank=True)
    is_bookmarked = models.BooleanField(null=True)
    







