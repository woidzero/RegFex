# main.py
# Get regular expressions from .re files!
# https://github.com/woidzero/RegFex.git


from dataclasses import dataclass
import re


@dataclass
class loadFile:
    """
    Read a .re file and returns its contents.
    
    ### Arguments
    - `filePath (str)`: Path to local file.
    """

    filePath: str

    def getKey(self, key: str) -> str:
        """
        Tries to get key from .re file if possible.

        ### Arguments
        - `key`: The key to find.
        """
        with open(self.filePath, 'r') as f:
            content = f.read()

        res = re.findall(fr'({key}:)(.+)', content)

        for val in res:
            val = ''.join(val)
            val = val.replace(key, '')
            val = val.replace(':', '')
            val = val.replace(' ', '')

            return val