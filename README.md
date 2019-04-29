
# Package ie_pandas

IE MBD OCT 2018 | Group H | April 2019  
Leandro Handal | Martin Hofbauer | Ashley O'Mahony | Gerald Walravens

***

**ie_pandas** is a group project.

The environment *only_np.yml* has been prepared with Python 3.7 and the packages Numpy 1.16.2 and statistics 1.0.3.5 only, to avoid uncontrolled dependencies during development.

Once the environment is installed in Anaconda, it should be activated with `conda activate only_np`.  

To install the package, navigate to the directory *ie_pandas* with `cd`, then run `pip install --editable .`. Check if the package has been installed using `conda list`.

To re-install the package, use `pip install -e .`.

To import the package in Python, use `from ie_pandas.DataFrame import *`.

To run the tests, install pytest with `pip install pytest`. The tests can be ran writing `pytest` in the ie_pandas folder. The total coverage of the test for the complete package with `pytest-cov`.