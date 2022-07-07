import requests


def send_ok(port, nonce):
    requests.post(f"http://localhost:{port}/ok?nonce={nonce}")


def send_nok(port, nonce, reason):
    requests.post(f"http://localhost:{port}/nok?nonce={nonce}", data={"reason": reason})


def send_message(port, nonce, from_username, message):
    return requests.post(
        f"http://localhost:{port}/message?nonce={nonce}",
        data={"from": from_username, "message": message},
        timeout=5
    )
