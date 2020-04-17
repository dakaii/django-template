from rest_framework import permissions, status, views
from rest_framework.response import Response
from .serializers import AccountOwnerSerializer


class SignUpView(views.APIView):
    """
    POST api/signup/
    """
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        """
        Create a new user.
        """
        serializer = AccountOwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


# class UserList(views.APIView):

#     # permission_classes = (permissions.IsAdminUser,)
#     # permission_classes = ()
#     permission_classes = (permissions.IsAuthenticated,)

#     def get(self, request, format=None):
#         """
#         List all users
#         """
#         users = User.objects.all()
#         serializer = UserSerializer(
#             users, context={'request': request}, many=True)
#         return Response(serializer.data)


# class UserDetail(views.APIView):

#     permission_classes = (permissions.IsAuthenticated,)

#     def patch(self, request, pk):
#         """
#         modify a user.
#         """
#         try:
#             user = User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Response(data={
#                 "message":
#                 "An item with the specified ID was not found"
#             }, status=status.HTTP_404_NOT_FOUND)
#         serializer = UserSerializer(user, data=request.data, partial=True)
#         serializer.is_valid(raise_excepion=True)
#         serializer.save()
#         return Response(
#             serializer.data,
#             status=status.HTTP_202_ACCEPTED)

#     def delete(self, request, pk):
#         """
#         delete a user.
#         """
#         try:
#             user = User.objects.get(pk=pk)
#             user.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except User.DoesNotExist:
#             return Response(data={
#                 "message":
#                 "An item with the specified ID was not found"
#             }, status=status.HTTP_404_NOT_FOUND)
