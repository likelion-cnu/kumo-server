from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissons import IsCustomer 
# Create your views here.


# 루트 페이지에 로그인 되어있는지와 고객 유저인지 확인
class RootView(APIView):
    # 고객만 접근 가능하게 permissoin 설정
    permission_classes = [IsCustomer]
    pass   
        

# 가게를 검색하는 뷰
class SearchView(APIView):
    # 고객만 접근 가능하게 permissoin 설정
    permission_classes = [IsCustomer]
    pass


# 고객 프로필을 띄우는 뷰
class ProfileView(APIView):
    # 고객만 접근 가능하게 permissoin 설정
    permission_classes = [IsCustomer]
    pass


# 북마크한 리스트를 띄우는 뷰
class BookmarkView(APIView):
    # 고객만 접근 가능하게 permissoin 설정
    permission_classes = [IsCustomer]
    pass


# 근처 가게를 띄우는 뷰
class NeighborhoodView(APIView):
    # 고객만 접근 가능하게 permissoin 설정
    permission_classes = [IsCustomer]
    pass


# 고객의 스탬프 갯수를 띄우는 뷰
class StampView(APIView):
    # 고객만 접근 가능하게 permissoin 설정
    permission_classes = [IsCustomer]
    pass


# 고객의 QNA를 띄우는 뷰
class CustomerQnaView(APIView):
    # 고객만 접근 가능하게 permissoin 설정
    permission_classes = [IsCustomer]
    pass