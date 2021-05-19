from setuptools import setup, find_packages

setup(
    long_description=open("README.rst", "r").read(),
    name="pyrunnable",
    version="0.43",
    description="threading.Thread wrapper with convenient functions",
    author="Pascal Eberlein",
    author_email="pascal@eberlein.io",
    url="https://github.com/smthnspcl/pyrunnable",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords="threading.Thread wrapper",
    packages=find_packages(),
    long_description_content_type="text/markdown"
)
