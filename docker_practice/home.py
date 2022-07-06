from rest_framework import views, status
from rest_framework.response import Response


class HomePage(views.APIView):
    
    def get(self, request, *args, **kwargs):
        return Response(data={"Home":"Hello world"}, status=status.HTTP_200_OK)