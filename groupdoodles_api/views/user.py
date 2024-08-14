from groupdoodles_api.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

class UserSerializer(serializers.ModelSerializer):
    """
    JSON Serializer for Rare Users
    """
    class Meta:
        model = User
        fields = "__all__"

@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated Gamer

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    user = User.objects.filter(uid=uid).first()

    # If authentication was successful, respond with their token
    if user is not None:
        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'date_registered': user.date_registered,
            'uid': user.uid,
        }
        return Response(data)
    else:
        data = { 'valid': False }
        return Response(data)
    
class UserView(ViewSet):
    def create(self, request):
        """
        function to create a new user
        """
        user = User.objects.create(
            username = request.data["username"],
            uid = request.data["uid"],
            email = request.data["email"],
        )
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """
        function to update a user
        """

        user = User.objects.get(pk=pk)
        user.username = request.data["username"]
        user.uid = request.data["uid"]
        user.email = request.data["email"]
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """
        function to delete a user
        """
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)