#!/usr/bin/env python3
"""
Auth module for the API
"""
from flask import request
from typing import List, TypeVar
import fnmatch


class Auth:
    """
    Auth Class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Require Authentication
        Returns:
          - False - path and excluded_paths
        """
        if path is None:
            return True

        if not excluded_paths or not isinstance(excluded_paths, list):
            return True

        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Authorization Header
        Returns:
          - None - request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Current User
        Returns:
          - None - request
        """
        return None
