#!/usr/bin/env python3
"""
Basic Authentication
"""
from .auth import Auth


class BasicAuth(Auth):
    """
    Basic Auth Class
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        extract authorization
        """
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        if not authorization_header.startsqith("Basic "):
            return None
        return authorization_header[len("Basic "):]
