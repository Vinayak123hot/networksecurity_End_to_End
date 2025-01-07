"""The setup.py file is a critical component of modular machine learning (ML) 
projects, especially when they are intended to be reusable, shareable, 
or deployed in different environments.
It is used by setuptools (or distutils in older python versions) to define configuration
of your project, such as metadata, dependencies, and more"""

from setuptools import find_packages , setup
from typing import List

#it will scan full folders whereever it find packages specified with __init__.py

def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """

    req_list = []

    try:
        with open("requirements.txt" , 'r') as file:
            # read each line from the file
            lines = file.readlines()

            # process the lines
            for line in lines:
                requirement = line.strip()

                # ignore empty lines and -e.
                if requirement and requirement != '-e .':
                    req_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return req_list

setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Vinayak Bhat",
    author_email = "bvssvinu@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)

