
# Package ie_pandas

IE MBD OCT 2018 | ADVANCED PYTHON | Group H | May 2019  
Leandro Handal | Martin Hofbauer | Ashley O'Mahony | Gerald Walravens

***

## Introduction
**ie_pandas** is a Python package developed for a group project. It allows the user to create `DataFrame` objects, in a *pandas* style.  

All the files of this project are saved in a [GitHub repository](https://github.com/ashomah/ie_pandas).  
&nbsp;  

## Features  
`DataFrame` objects can be created from:  
* a list  
* a *numpy* array  
* a list of lists  
* a dictionary of lists  
* a dictionary of *numpy* arrays  
&nbsp;  

`DataFrame` can handle data of types:  
* `int`: integer (`1`, `2`, `3`...)  
* `float`: decimal (`1.0`, `1.1`, `1.2`...)  
* `bool`: boolean (`True`, `False`)  
* `string`: alphanumeric (`a`, `b`, `c`...)  

Columns can contain different data types, however, the **data type should be consistent within the column**.  
&nbsp;  

`DataFrame` objects are structured with:  
* `.df`: contains the data of the `DataFrame` object, stored in a dictionary.  
* `.colindex`: contains the column names, stored in a list of strings.  
* `.rowindex`: contains the row names, stored in a list of strings.  
&nbsp;  

The data of `DataFrame` objects can be accessed by:  
* `df[1]` or `df['C1']`  
A dictionary-style way to call columns, using the column *numerical index* or *column name*.  
Column contents are returned in a *numpy* array.  
* `.get_row(1)` or `.get_row('R1')`  
Method to call rows, using the row *numerical index* or *column name*.  
Row contents are returned in a list.  
&nbsp;  

Calculations can be done on `DataFrame` numerical columns (data types `int`, `float` or `bool`):  
* `.sum()`: provides the sum of the elements of each column,  
* `.min()`: provides the minimum value of the elements of each column,  
* `.max()`: provides the maximum value of the elements of each column,  
* `.mean()`: provides the mean value of the elements of each column,  
* `.median()`: provides the median value of the elements of each column.  

Calculation results are returned in a list.  
&nbsp;  

The Jupyter Notebook `Demo.ipynb` provides some usage examples of `DataFrame`.  
&nbsp;  

## Installation  

#### Dependencies  
`ie_pandas` is developed in *Python 3.7* and uses the package *numpy* (version 1.16 at the time of development).  
&nbsp;  

#### Users  
To install the package with Terminal (macOS):  
* Navigate to the directory *ie_pandas* with `cd`,  
* Run `pip install --editable .`,  
* Check if the package has been installed using `conda list`.  

To import the package in Python, use `from ie_pandas import DataFrame`.  
&nbsp;  

#### Developers  
The environment *only_np.yml* has been prepared to avoid uncontrolled dependencies during development. Available in `/environment`, it contains:  
* Python | version 3.7.3  
* Pip | version 19.0.3  
* Numpy | version 1.16.2  
* Pytest | version 4.4.1  
* Pytest-cov | version 2.6.1  
* Black | version 19.3b0  
* Jupyter | version 1.0.0  

To install the environment in Anaconda with Terminal (macOS), run `conda env create -f only_np.yml`.  
Once the environment is installed in Anaconda, it should be activated with `conda activate only_np`.  
&nbsp;  

To install the package with Terminal (macOS):  
* Navigate to the directory *ie_pandas* with `cd`,  
* Run `pip install --editable .`,  
* Check if the package has been installed using `conda list`.  

For modifications to the package code to be considered, re-install the package using `pip install -e .`.  
To import the package in Python, use `from ie_pandas import DataFrame`.  
&nbsp;  

For testing, install the packages with Terminal (macOS):  
* *pytest* with `pip install pytest`,  
* *pytest-cov* with `pip install pytest-cov`.  

To run the tests and check their coverage, run:  
`pytest --cov=ie_pandas 'test' --cov-report term-missing -vv`  
&nbsp;  

## DataFrame Object Creation  
Creating a `DataFrame` by passing a dictionary of lists, letting `ie_pandas` create default integer indexes:  
```
obj = {'str':['a', 'b', 'c', 'd', 'e'],
       'int':[1, 2, 3, 4, 5],
       'float':[1.1, 2.2, 3.3, 4.4, 5.5],
       'bool':[True, False, True, False, True]}

df = DataFrame(obj)
df

Out[1]:    str  int  float   bool
        0    a    1    1.1   True
        1    b    2    2.2  False
        2    c    3    3.3   True
        3    d    4    4.4  False
        4    e    5    5.5   True
```
&nbsp;  

Creating a `DataFrame` by passing a list of lists, defining column names:  
```
obj = [['a', 'b', 'c', 'd', 'e'],
       [1, 2, 3, 4, 5],
       [1.1, 2.2, 3.3, 4.4, 5.5],
       [True, False, True, False, True]]

df = DataFrame(obj,
               colindex = ['STRING', 'INTEGER', 'FLOAT', 'BOOLEAN'])
df

Out[1]:    STRING  INTEGER  FLOAT   BOOLEAN
        0       a        1    1.1      True
        1       b        2    2.2     False
        2       c        3    3.3      True
        3       d        4    4.4     False
        4       e        5    5.5      True
```
&nbsp;  

Creating a `DataFrame` by passing a dictionary of *numpy* arrays, defining column and row names:  
```
import numpy as np
obj = {'str':np.array(['a', 'b', 'c', 'd', 'e']),
       'int':np.array([1, 2, 3, 4, 5]),
       'float':np.array([1.1, 2.2, 3.3, 4.4, 5.5]),
       'bool':np.array([True, False, True, False, True])}

df = DataFrame(obj,
               colindex = ['STRING', 'INTEGER', 'FLOAT', 'BOOLEAN'],
               rowindex = ['A', 'B', 'C', 'D', 'E'])
df

Out[1]:    STRING  INTEGER  FLOAT  BOOLEAN
        A       a        1    1.1     True
        B       b        2    2.2    False
        C       c        3    3.3     True
        D       d        4    4.4    False
        E       e        5    5.5     True
```
&nbsp;  

Creating a `DataFrame` by passing a dictionary of lists as rows, defining column names:  
```
obj = {'REC1':[1, 1, 1, 1, 1],
       'REC2':[2, 2, 2, 2, 2],
       'REC3':[3, 3, 3, 3, 3],
       'REC4':[4, 4, 4, 4, 4]}

df = DataFrame(obj,
               axis = 1,
               colindex = ['W', 'X', 'Y', 'Z'])
df

Out[1]:       W  X  Y  Z
        REC1  1  1  1  1
        REC2  2  2  2  2
        REC3  3  3  3  3
        REC4  4  4  4  4
```  
