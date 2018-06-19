 from flask import Flask, Response
from twilio.jwt.client import ClientCapabilityToken

app = Flask(__name__)


@app.route('/token', methods=['GET'])
def get_capability_token():
    """Respond to incoming requests."""

    # Find these values at twilio.com/console
    account_sid = 'AC50e703c81b0f481620791d6ae77140c1'
    auth_token = '3bae1713efdd12d1e340d7e0b65a067c'

    capability = ClientCapabilityToken(account_sid, auth_token)

    # Twilio Application Sid
    application_sid = 'AP359f96e476d9996131fcd693d95670c2'
    capability.allow_client_outgoing(application_sid)
    capability.allow_client_incoming('red')
    token = capability.to_jwt()

    return Response(token, mimetype='application/jwt')


if __name__ == "__main__":
    app.run(debug=True)
