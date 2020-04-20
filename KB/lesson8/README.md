# Lesson8 / Libraries, PIP, and Virtual Environments

- [ ] 1. Importing Libraries
Video link https://vimeo.com/259422351
Length is 5 minutes
 
- [ ] 2. sys.path and PYTHONPATH
Video link https://vimeo.com/259423316
Length is 7 minutes
 
- [ ] 3. pip
Video link https://vimeo.com/259424573
Length is 7 minutes
 
- [ ] 4. Virtual Environments
Video link https://vimeo.com/259426537
Length is 6 minutes
 
- [ ] 5. Creating a Simple Python Module
Video link https://vimeo.com/259427586
Length is 4 minutes


## Additional Content:

- [ ] [A non-magical introduction to Pip and Virtualenv for Python beginners​](https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/)

- [ ] [Common Python Tools: Using virtualenv, Installing with Pip, and Managing Packages​](https://www.digitalocean.com/community/tutorials/common-python-tools-using-virtualenv-installing-with-pip-and-managing-packages)

Read the "Using pip" section.


## Exercises

Reference code for these exercises is posted on GitHub at:
https://github.com/ktbyers/pynet/tree/master/learning_python/lesson8


- [ ] 1a. Import the 'datetime' library. Print out the module that is being imported by datetime (the \_\_file\_\_ attribute)

Import the Python ipaddress library. Print out the module that is being imported by ipaddress (the \_\_file\_\_ attribute). If you are using Python 2.7, you will need to pip install the ipaddress library.

Import sys and use pprint to pprint sys.path


- [ ] 1b. In a separate Python file named 'my_devices.py', define a dictionary named 'rtr1' with the following key-value pairs:

      host = rtr1.domain.com
      username = cisco
      password = cisco123
      device_type = cisco_ios

Import my_devices into this program, and print the rtr1 dictionary to the screen using pprint.


- [ ] 1c. In a Python shell, try importing the 'my_devices' when my_devices.py is not in your current working directory.

What exception do you get when you do this?

Update your PYTHONPATH environment variable so that you are successfully able to import this module.


- [ ] 2a. Create a new virtual environment on your system named 'test_venv'.

b. Activate the virtual environment

c. Use 'which python' to see the path of the Python that you are using.

d. Use 'pip list' to see the packages you have installed.

e. Use pip to install Netmiko and the requests library.

f. Use 'pip list' to see the updated list of installed packages.


- [ ] 3a. Using the same 'test_venv' that you created in exercise2, install netmiko version 2.0.1. Verify that this version is installed by executing the following from the Python shell:

      >>> import netmiko
      >>> netmiko.__version__
      '2.0.1'

b. Using pip, upgrade your version of Netmiko to the latest version.

c. Deactivate your virtual environment. See 'which python' is now being used.


- [ ] 4a. Activate your 'test_venv' virtual environment.

b. Use pip to uninstall the Netmiko library.

c. Verify that Netmiko is no longer installed.

d. Use pip to install the 'develop' branch of Netmiko.


## CLASS OUTLINE
1. Importing Libraries (VIDEO1)
   1. import re   [00:04]
   2. re.\_\_file\_\_   (where is the library)   [00:34]
   3. How using 'import' affects the namespace   [2:19]
   4. from re import search   [3:08]
   5. How using 'from' affects the namespace   [3:47]

2. sys.path and PYTHONPATH (VIDEO2)
   1. Where is Python looking   [00:30]
   2. sys.path   [1:02]
   3. PYTHONPATH   [2:30]
   4. Example of a failure   [4:27]

3. Pip (VIDEO3)
   1. How to install libraries   [00:01]
      1. pip install netmiko   [00:21]
      2. pip install netmiko==2.1.0   [1:26]
      3. pip uninstall netmiko   [1:53]
      4. pip install --upgrade netmiko   [2:13]
      5. pip list   [3:01]
      6. pip installing from git repo   [3:19]

4. Virtual Environments (VIDEO4)
   1. Virtual environment options   [00:28]
   2. Activating the virtual environment   [00:47]
   3. pip list on a new clean virtual environment   [2:33]
   4. Deactivate   [5:03]

5. Simple Python Module (VIDEO5)
   1. Creating your own module   [00:06]
   2. Define devices and importing them   [1:29]
