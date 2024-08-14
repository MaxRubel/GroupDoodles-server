from groupdoodles_api.models import Doodle, User
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class DoodleSerializer(serializers.ModelSerializer):
    """
    JSON Serializer for Doodles
    """
    class Meta:
        model = Doodle
        fields = "__all__"

class DoodleSerializerSmall(serializers.ModelSerializer):
    class Meta:
        model = Doodle
        fields = ["owner", "name", "date_created", "collaborators"]
        depth = 1

class DoodleView(ViewSet):
    @action(detail=False, methods=['get'], url_path='get_user_doodles')
    def get_user_doodles(self, request):
        user_id = request.query_params.get('user_id')
        user = User.objects.get(pk=user_id)
        
        your_doodles= Doodle.objects.filter(owner=user)
        joined_doodles = user.doodles.all()

        yours_serializer = DoodleSerializerSmall(your_doodles, many=True)
        others_serializer = DoodleSerializerSmall(joined_doodles, many=True)
        
        return Response({
            "yourDoodles": yours_serializer.data,
            "otherDoodles": others_serializer.data
            },
            status=status.HTTP_200_OK)
        
    def retrieve(self, request, pk):
        doodle = Doodle.objects.get(pk=pk)
        serialzer = DoodleSerializer(doodle)
        return Response(serialzer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """
        function to create a new doodle
        """
        user = User.objects.get(pk=request.data['user_id'])
        doodle = Doodle.objects.create(
            owner = user,
            name = request.data["name"],
            data = request.data["data"],
        )
        serializer = DoodleSerializer(doodle)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """
        function to update a doodle
        """
        user = User.objects.get(pk=request.data['user_id'])
        doodle = Doodle.objects.get(pk=pk)
        doodle.owner = user
        doodle.name = request.data["name"]
        doodle.date_created = request.data["date_created"]
        doodle.data = request.data["data"]
        doodle.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """
        function to delete a user
        """
        doodle = Doodle.objects.get(pk=pk)
        doodle.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)