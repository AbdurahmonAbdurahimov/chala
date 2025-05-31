
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def monthly_report(request):
    return Response({"report": "Monthly report coming soon."})
