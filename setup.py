from setuptools import setup,find_packages
from typing import List
def get_requirements()->List[str]:
    '''
    This function will return the list of requirements
    '''
    try:
        requirements_lst:List[str]=[]
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirements=line.strip()
                ## ignore the empty lines and -e.
                if requirements and not requirements.startswith('-e'):
                    requirements_lst.append(requirements)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirements_lst

print(get_requirements())

setup(
    name="networksecurity",
    version="0.1.0",
    packages=find_packages(),
    install_requires=get_requirements(),
    author="Preeti Kumari",
    author_email="preetikumari24445@gmail.com"
)

