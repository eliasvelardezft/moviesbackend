from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action

from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserSerializer, LoginSerializer

class UserViewSet(viewsets.ModelViewSet):
  serializer_class = UserSerializer
  queryset = User.objects.all()
  authentication_classes = [TokenAuthentication]
  permission_classes = [AllowAny]

  def get_serializer_class(self):
    if self.action in ['login']:
      return LoginSerializer
    else:
      return UserSerializer

  def create(self, request):
      print('******* CREATING USER *******')
      serializer = UserSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)

      user = User.objects.create_user(
        first_name = serializer.validated_data['first_name'],
        last_name = serializer.validated_data['last_name'],
        username = serializer.validated_data['username'],
        password = serializer.validated_data['password'],
      )
      if isinstance(user, User):
        Token.objects.get_or_create(user=user)
        return Response({"code": "ok"})
      else:
        return user
  
  @action(methods=['POST'], detail=False)
  def login(self, request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token = Token.objects.get(user=user)
    return Response({
      'user': serializer.data,
      'token': token.key
    })
  
  
  