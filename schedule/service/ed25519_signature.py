from schedule.domain.interfaces.signature_provider import SignatureProvider

class Ed25519Signature(SignatureProvider):

    def sign(self, payload: str) -> str:
        raise NotImplementedError("In progress")