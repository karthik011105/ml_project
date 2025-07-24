from setuptools import setup, find_packages
def get_requirements(file_path:str)->list[str]:
    """
    This function will return a list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements if req.strip() and not req.startswith('-')]
    if '-e .' in requirements:
        requirements.remove('-e .')
    return requirements

setup(
    name='ml_project',
    version='0.0.1',
    packages=find_packages(),
    author='Karthik',
    author_email='k.v.karthik1105@gmail.com',
    install_requires=get_requirements('requirements.txt'),
)