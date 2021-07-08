from rest_framework.permissions import BasePermission
import ipdb




class AdminCreateOnlyPermisson(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        if request.method == 'GET':
            return True

        return False

# usuario:
# "is_superuser": false,
# "is_staff": false
#
# critico:
# "is_superuser": false,
# "is_staff": true
#
# admin:
# "is_superuser": true,
# "is_staff": true

# Critica
class ReviewCreateOnlyPermission(BasePermission):
    def has_permission(self, request, view):

        if not request.user.is_superuser and request.user.is_staff:
            return True

        if request.method == 'GET':
            return True

        return False

class CommentCreateOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_superuser and request.user.is_staff:
            return True

        if request.methot == 'GET':
            return True

        return False


