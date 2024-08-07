#!/usr/bin/env python3
"""
Auth module for the API
"""
from flask import request


class Auth:
    """
    Auth Class
    """
    def require_auth(self, path: srt, excluded_paths: List[str]) -> bool:
        """
        Require Authentication
        Returns:
          - False - path and excluded_paths
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Authorization Header
        Returns:
          - None - request
        """
        return None

    def def current_user(self, request=None) -> TypeVar('User'):
        """
        Current User
        Returns:
          - None - request
        """
        return None
