#!/usr/bin/env python3
"""Demonstrate mixins with a Dragon class."""


class SwimMixin:
    """Provide swimming behavior."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Provide flying behavior."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon."""

    def roar(self):
        """Print roaring behavior."""
        print("The dragon roars!")
