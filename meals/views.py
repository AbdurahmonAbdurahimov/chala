
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def view_meals(request):
    return Response({"message": "This is meals view (demo). Add logic here."})
