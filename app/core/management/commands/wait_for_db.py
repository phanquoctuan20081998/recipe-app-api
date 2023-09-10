"""
Django command to wait for the databbase to be available.
"""
from typing import Any
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""
    
    def handle(self, *args: Any, **options: Any):
        pass