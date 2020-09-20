from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns list of APIView features"""
        an_apiview=[
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a tradtional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manully to URls',
        ]

        return Response({'messages': 'Hello!', 'an_apiview':an_apiview})
