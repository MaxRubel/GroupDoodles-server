from groupdoodles_api.models import Doodle, User, DoodleCollab
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class DoodleCollabView(ViewSet):
    @action(detail=False, methods=['post'], url_path='add_doodle_collab' )
    def add_doodle_collab(self, request):
        try:
            doodle = Doodle.objects.get(pk=request.data['doodle_id'])
            collab = User.objects.get(email=request.data['email'])

            if Doodle.objects.filter(pk=doodle.id, owner=collab).exists():
                return Response({"error": "This is your own doodle"}, status=status.HTTP_400_BAD_REQUEST)

            if DoodleCollab.objects.filter(doodle=doodle, collab=collab).exists():
                return Response({"error": "This collaborator is already connected"}, status=status.HTTP_400_BAD_REQUEST)
            
            DoodleCollab.objects.create(
                doodle = doodle,
                collab = collab
            )

            return Response({"success":"collab created"}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response(
                {"error": "User does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Doodle.DoesNotExist:
            return Response(
                {"error": "Doodle does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )
        
    @action(detail=False, methods=['post'], url_path='remove_doodle_collab' )
    def remove_doodle_collab(self, request):

        try:
            doodle = Doodle.objects.get(pk=request.data['doodle_id'])
            collab = User.objects.get(pk=request.data['user_id'])

            doodleCollab = DoodleCollab.objects.filter(doodle=doodle, collab=collab)
            doodleCollab.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except User.DoesNotExist:
            return Response(
                {"error": "User does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Doodle.DoesNotExist:
            return Response(
                {"error": "Doodle does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )