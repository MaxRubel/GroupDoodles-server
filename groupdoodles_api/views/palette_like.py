from groupdoodles_api.models import Palette, User, PaletteLike
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class PaletteLikeView(ViewSet):
    @action(detail=False, methods=['post'], url_path='like_palette' )
    def like_palette(self, request):
        try:
            palette = Palette.objects.get(pk=request.data['palette_id'])
            user = User.objects.get(pk=request.data['user_id'])

            if Palette.objects.filter(pk=palette.id, owner=user).exists():
                return Response({"error": "This is your own palette"}, status=status.HTTP_400_BAD_REQUEST)

            paletteLike = PaletteLike.objects.filter(palette=palette, user=user)

            if paletteLike.exists():
                paletteLike.delete()
            else:
                PaletteLike.objects.create(
                palette=palette,
                user=user
                )

            return Response(status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response(
                {"error": "User does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Palette.DoesNotExist:
            return Response(
                {"error": "Palette does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        