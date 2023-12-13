from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers


class NewLoginSerializer(LoginSerializer):
    # emial = serializers.EmailField(required = False, allow_blank = True)
    # password = serializers.CharField(style={'input_type': 'password'})
    pass 

class NewRegisterSerializer(RegisterSerializer):
    # first_name = serializers.CharField()
    # last_name = serializers.CharField()
    nickname = serializers.CharField()
    def custom_signup(self, request, user):
        # user.first_name = request.data['first_name']
        # user.last_name = request.data['last_name']
        user.nickname = request.data['nickname']
        user.save()
    pass

