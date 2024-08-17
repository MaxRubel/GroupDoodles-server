from groupdoodles_api.models import Palette, User
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class PaletteSerializer(serializers.ModelSerializer):
    """
    JSON Serializer for Palettes
    """
    class Meta:
        model = Palette
        fields = "__all__"
        depth= 1

class PaletteView(ViewSet):
    
    @action(detail=False, methods=['get'], url_path='get_user_palettes' )
    def get_user_palettes(self, request):
        user_id = request.query_params.get('user_id')
        user = User.objects.get(pk=user_id)
        palettes = Palette.objects.filter(owner=user)
        serializer = PaletteSerializer(palettes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='get_liked_palettes' )
    def get_liked_palettes(self, request):
        user_id = request.query_params.get('user_id')
        
        user = User.objects.get(pk=user_id)
        liked_palettes = user.palettes.all()
        
        serializer = PaletteSerializer(liked_palettes, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def list(self, request):
        palettes = Palette.objects.all()[:50] 
        serializer = PaletteSerializer(palettes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """
        function to create a new palette
        """
        user = User.objects.get(pk=request.data['user_id'])
        palette = Palette.objects.create(
            owner = user,
            name = request.data["name"],
            colors = request.data["colors"],
        )
        serializer = PaletteSerializer(palette)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """
        function to update a palette
        """
        user = User.objects.get(pk=request.data['user_id'])
        palette = Palette.objects.get(pk=pk)
        palette.owner = user
        palette.name = request.data["name"]
        palette.date_created = request.data["date_created"]
        palette.colors = request.data["colors"]
        palette.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """
        function to update a palette
        """
        palette = Palette.objects.get(pk=pk)
        palette.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)