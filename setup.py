from sys import version
import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

    setuptools.setup(
        name = 'preprocess_nlp_mikelakoju', # his has to be a unique name
        version = '0.0.3',
        author = 'Mike Lakoju',
        author_email = 'mikelakoju@yahoo.com',
        description = 'This is an NLP Preprocessing Package in Python3',
        long_description = long_description,
        long_description_content_type = 'text/markdown',
        packages = setuptools.find_packages(),
        classifiers = [
            'programming Language :: Python :: 3',
            'License :: OSI Aproved :: MIT License',
            "Operating System :: OS Independent"],
        python_requires = '>=3.5'

    )
