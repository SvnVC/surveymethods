# surveymethods
Python wrapper for the surveymethods api.

## Usage
All methods return a json object.

example:

```
from smapi.api import surveymethods

surveymethods = Surveymethods(apikey, login)

data = surveymethods.<method>
```


## In development
This library doesn't contain all api functions available, but is focused on getting data from the executed surveys.
