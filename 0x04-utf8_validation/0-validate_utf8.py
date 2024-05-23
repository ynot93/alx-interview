#!/usr/bin/python3
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
    except TypeError:
        return False
    except AttributeError:
        return False
    return True
