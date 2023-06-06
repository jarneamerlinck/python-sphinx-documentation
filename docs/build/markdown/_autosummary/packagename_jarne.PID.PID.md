# packagename_jarne.PID.PID


### _class_ PID()
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Set the Proportional Integral Derivative controller

### Methods

| `GenOut`

 | Calculates error

 |
| `Initialize`

                  | Initialize variables

                                     |
| `SetKd`

                       | Set $K_{d}$

                                              |
| `SetKi`

                       | Set $K_{i}$

                                              |
| `SetKp`

                       | Set $K_{p}$

                                              |
| `SetPrevError`

                | Sets previous error

                                      |

#### GenOut(error)
Calculates error


* **Parameters**

    **error** ([*float*](https://docs.python.org/3/library/functions.html#float)) – Value of error



* **Returns**

    PID



* **Return type**

    [float](https://docs.python.org/3/library/functions.html#float)



#### Initialize()
Initialize variables


#### SetKd(invar)
Set $K_{d}$


* **Parameters**

    **invar** ([*float*](https://docs.python.org/3/library/functions.html#float)) – Value to be set in $K_{d}$



#### SetKi(invar)
Set $K_{i}$


* **Parameters**

    **invar** ([*float*](https://docs.python.org/3/library/functions.html#float)) – Value to be set in $K_{i}$



#### SetKp(invar)
Set $K_{p}$


* **Parameters**

    **invar** ([*float*](https://docs.python.org/3/library/functions.html#float)) – Value to be set in $K_{p}$



#### SetPrevError(preverror)
Sets previous error


* **Parameters**

    **preverror** ([*float*](https://docs.python.org/3/library/functions.html#float)) – value of the previous error
