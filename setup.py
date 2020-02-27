from setuptools import setup, find_packages

setup(
    name='ci_githubactions',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example of CI with GitHub Actions',
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    url='https://github.com/gnayuy/ci_githubactions',
    author='gnayuy',
    author_email='gnayuy@gmail.com'
)
