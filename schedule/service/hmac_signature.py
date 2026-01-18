import hmac
import hashlib
from schedule.domain.interfaces.signature_provider import SignatureProvider

class HmacSignature(SignatureProvider):

    def __init__(self, secret_key: str):
        self.secret_key = secret_key.encode()

    def sign(self, payload: str) -> str:
        return hmac.new(self.secret_key, payload.encode(), hashlib.sha256).hexdigest()
