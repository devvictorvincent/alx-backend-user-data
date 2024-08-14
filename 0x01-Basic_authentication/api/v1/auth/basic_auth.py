#!/usr/bin/env python3
"""
Basic Authentication
"""
import base64
from .auth import Auth


class BasicAuth(Auth):
    """
    Basic Auth Class
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        extract authorization
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Basic - Base64 decode
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(
                    base64_authorization_header,
                    validation=True,
                    )
            return decoded.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
