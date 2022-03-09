from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.admin import User
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from backend.models import GuestBook
from backend.serializers import GuestBookSerializer
from .serializers import UserSerializer


class UserCreate(CreateAPIView):
    """
    Register user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class ListAPIView(ListAPIView):
    """
    This endpoint list of the GuestBook from the database
    """

    queryset = GuestBook.objects.all()
    serializer_class = GuestBookSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class RetrieveAPIView(RetrieveAPIView):
    """
    This endpoint list of the GuestBook from the database
    """

    queryset = GuestBook.objects.all()
    serializer_class = GuestBookSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class CreateAPIView(CreateAPIView):
    """
    This endpoint allows for creation of a GuestBook
    """
    queryset = GuestBook.objects.all()
    serializer_class = GuestBookSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class UpdateAPIView(UpdateAPIView):
    """
    This endpoint allows for updating a GuestBook according to given ID
    """
    queryset = GuestBook.objects.all()
    serializer_class = GuestBookSerializer


@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
class DeleteAPIView(DestroyAPIView):
    """
    This endpoint allows for deleting a GuestBook according to given ID
    """
    queryset = GuestBook.objects.all()
    serializer_class = GuestBookSerializer
