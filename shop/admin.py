from django.contrib import admin
from .models import Coupon, Payment, Review, Review_Comment ,ShopQna, ShopQuestion

admin.site.register(Coupon)
admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(Review_Comment)
admin.site.register(ShopQna)
admin.site.register(ShopQuestion)
