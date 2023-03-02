"""
Getting rid of pylint errors.
"""

import requests


class docstring_example: 
    """ 
    Docstring example.

    A more detailed explanation.
    """
    def getRequest():
        """ 
        Get response from Google.

        Parameters: None
        """
        response = requests.get("https://google.com")
        print(response)