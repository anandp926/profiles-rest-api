from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
            'Anand',
            'Singh',
            'Parihar'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})