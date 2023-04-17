# Functions

## packagename_jarne.functions module


### _class_ packagename_jarne.functions.ThreadSafeSingleton()
Bases: `type`

Class to create ThreadSafeSingleton


* **Returns**

    Class object



* **Return type**

    ThreadSafeSingleton



### packagename_jarne.functions.device_exists(path: str)
This functions checks if an device exists in linux


* **Parameters**

    **path** (*str*) – Path to device  (/dev/tty for example)



* **Returns**

    True if device exists



* **Return type**

    bool



### packagename_jarne.functions.set_max_limit(value: int, max: int)
Set maximum limit for an value


* **Parameters**

    
    * **value** (*int*) – value


    * **max** (*int*) – maximum



* **Returns**

    maximum of the 2 values



* **Return type**

    int



### packagename_jarne.functions.set_min_limit(value: int, min: int)
Set minimum limit for an value


* **Parameters**

    
    * **value** (*int*) – value


    * **min** (*int*) – minimum



* **Returns**

    minimum of the 2 values



* **Return type**

    int
