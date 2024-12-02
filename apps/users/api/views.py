from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.api.serializers import UserSerializer
from utils.responseformat import success_response, fail_response

User = get_user_model()


class UserViews(APIView):

    def get_objects(self, user_id):

        user = User.objects.filter(id=user_id)
        return user.first()

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(success_response(serializer.data))
        return Response(fail_response(serializer.errors))

    def get(self, request):
        user = self.get_objects(request.user.id)
        if user:
            serializer = UserSerializer(user, many=False)
            return Response(success_response(serializer.data))
        return Response(fail_response(None, status.HTTP_404_NOT_FOUND))

    def put(self, request):
        user = self.get_objects(request.data['user_id'])
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(success_response(serializer.data))
        return Response(fail_response(None, status.HTTP_400_BAD_REQUEST))

    def delete(self):
        user = self.get_objects(self.request.data["user_id"])
        serializer = UserSerializer(user, data={"is_active": False}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(success_response(serializer.data))
        return Response(fail_response(None, status.HTTP_400_BAD_REQUEST))
