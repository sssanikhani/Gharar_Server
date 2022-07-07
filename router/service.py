import sys
import datetime
import time
import requests

from .models import Member
from router.utils import send_ok, send_nok, send_message


def register(username, port, nonce):
    if not username:
        send_nok(port, nonce, "[C]")
        sys.exit()
    if Member.objects.filter(username=username).exists():
        send_nok(port, nonce, "[C]")
        sys.exit()
    try:
        Member.objects.create(username=username, port=port)
    except Exception:
        send_nok(port, nonce, "[X]")
        sys.exit()
    send_ok(port, nonce)


def presence(username, port, nonce):
    member = Member.objects.filter(username=username).first()
    if not member:
        send_nok(port, nonce, "[X]")
        sys.exit()
    try:
        member.last_presence = datetime.datetime.now()
        member.save()
    except Exception as e:
        send_nok(member.port, nonce, "[X]")
        sys.exit()
    send_ok(member.port, nonce)


def unregister(username, port, nonce):
    member = Member.objects.filter(username=username).first()
    if not member:
        send_nok(port, nonce, "[X]")
        sys.exit()
    port = member.port
    try:
        member.delete()
    except Exception:
        send_nok(port, nonce, "[X]")
        sys.exit()
    send_ok(port, nonce)


def message(from_username, to_username, port, message_content, nonce):
    from_ = Member.objects.filter(username=from_username).first()
    if not from_:
        send_nok(port, nonce, "[X]")
        sys.exit()
    try:
        to = Member.objects.get(username=to_username)
    except Member.DoesNotExist:
        send_nok(from_.port, nonce, "[U]")
        sys.exit()
    try:
        res = send_message(to.port, nonce, from_.username, message_content)
    except requests.Timeout:
        send_nok(from_.port, nonce, "[R]")
        sys.exit()
    if res.status_code != 200:
        send_nok(from_.port, nonce, "[X]")
        sys.exit()
    send_ok(from_.port, nonce)
