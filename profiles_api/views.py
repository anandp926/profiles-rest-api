from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):
    """Test Api View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
            'Anand',
            'Singh',
            'Parihar'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, 
                status = status.HTTP_400_BAD_REQUEST
            )
        
    def put(self, request, pk=None):
        """Update"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """partial Update"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """partial Update"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Test',
            'Test Anand',
            'Test Anand Singh Parihar'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=data.request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello name'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    
    def retriev(self, request, pk=None):
        """Handel getting an object by id"""
        return Response({'http_method': 'GET'})
    
    def update(self, request, pk=None):
        """Handel updating an object by id"""
        return Response({'http_method': 'PUT'})
    
    def partial_update(self, request, pk=None):
        """Handel updating a part of an object by id"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handel removing an object by id"""
        return Response({'http_method': 'DELETE'})