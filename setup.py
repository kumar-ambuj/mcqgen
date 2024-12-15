from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Ambuj Kumar',
    author_email='ambuj.kumar@hotmail.com',
    install_requires=["openai","google-generativeai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)