import threading

from rest_framework.response import Response
from rest_framework.views import APIView

from router.service import message, unregister, register, presence


class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        port = request.data.get('port')
        nonce = request.GET.get('nonce')
        th = threading.Thread(target=register, args=(username, port, nonce,))
        th.start()
        return Response()


class PresenceView(APIView):
    def post(self, request):
        username = request.data.get('username')
        port = request.data.get('port')
        nonce = request.GET.get('nonce')
        th = threading.Thread(target=presence, args=(username, port, nonce))
        th.start()
        return Response()


class UnregisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        port = request.data.get('port')
        nonce = request.GET.get('nonce')
        th = threading.Thread(target=unregister, args=(username, port, nonce))
        th.start()
        return Response()


class MessageView(APIView):
    def post(self, request):
        from_username = request.data.get('username')
        to_username = request.data.get('to')
        port = request.data.get('port')
        message_content = request.data.get('message')
        nonce = request.GET.get('nonce')
        th = threading.Thread(target=message, args=(from_username, to_username, port, message_content, nonce))
        th.start()
        return Response()
