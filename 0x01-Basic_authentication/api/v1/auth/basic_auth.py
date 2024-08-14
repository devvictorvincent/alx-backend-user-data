#!/usr/bin/env python3
"""
Basic Authentication
"""
import base64
import re
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
                    validate=True,
                    )
            return decoded.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
        return

    def extract_user_credentials(
                self, decoded_base64_authorization_header: str) -> (str, str):
        """ Extracts User credentials from base 64-decode
            authorization header
            """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        pattern = r'(?P<user>[^:]+):(?P<password>.+)'
        match = re.fullmatch(
                pattern,
                decoded_base64_authorization_header.strip(),
        )
        if match is not None:
            user = match.group('user')
            password = match.group('password')
            return user, password
        return None, None
