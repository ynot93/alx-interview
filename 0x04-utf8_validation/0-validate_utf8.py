#!/usr/bin/env python3
"""
This module deals with character encoding formats

"""


def validUTF8(data):
    """
    Determines if a given dataset represents a valid
    UTF-8 encoding

    """
    try:
        bytes(data).decode('utf-8')
    except UnicodeDecodeError:
        return False
    except ValueError:
        return False
    return True
