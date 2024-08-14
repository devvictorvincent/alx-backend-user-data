#!/usr/bin/env python3
"""
Basic Authentication
"""
import base64
import re
from typing import TypeVar
from .auth import Auth
from models.user import User


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

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Gets user Object based on
        email and correct password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        if len(users) <= 0:
            return None
        if users[0].is_valid_password(user_pwd):
            return users[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the user from a request.
        """
        auth_header = self.authorization_header(request)
        b64_auth_token = self.extract_base64_authorization_header(auth_header)
        auth_token = self.decode_base64_authorization_header(b64_auth_token)
        email, password = self.extract_user_credentials(auth_token)
        return self.user_object_from_credentials(email, password)
