import re
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializers
from rest_framework import status

class HelloAPIView(APIView):
    '''Test API view'''

    def get(self, request, format = None):
        '''Return a list of API View feature'''
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello from test api', 'an_apiview': an_apiview})  

    serializer_class = serializers.HelloSerializer
    def post(self, request):
        '''create a hello message with our name'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})