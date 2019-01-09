# surveymethods
Python wrapper for the surveymethods api.

## Usage
All methods return a json object.

example:

from smapi.api import surveymethods

surveymethods = Surveymethods(apikey, login)

data = surveymethods.<method>
