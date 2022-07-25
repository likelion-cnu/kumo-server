from rest_framework import permissions

class IsAuthorOrReadonly(permissions.BasePermission):
    # 인증된 유저에 한해, 목록조회/포스팅등록을 허용
    def has_permission(self, request, view):
        return request.user.is_authenticated  # 인증이 되야만 허용

    # 작성자에 한해, Record에 대한 수정/삭제 허용
    def has_object_permission(self, request, view, obj):
        # 조회 요청(GET, HEAD, OPTIONS) 에 대해서는 인증여부에 상관없이 허용
        if request.method in permissions.SAFE_METHODS:  # SAFE_METHODS = ('GET', HEAD', 'OPTIONS')
            return True

        # PUT, DELETE 요청에 대해, 작성자일 경우에만 요청 허용
        return obj.author == request.user