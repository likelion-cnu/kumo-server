from django.contrib import admin
from .models import Coupon, Payment, Review, ShopQna, ShopQuestion

admin.site.register(Coupon)
admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(ShopQna)
admin.site.register(ShopQuestion)
