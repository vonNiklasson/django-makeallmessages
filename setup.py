import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-makeallmessages",
    version="0.1.0",
    author="Johan Niklasson",
    author_email="johan@niklasson.me",
    description="Adds the makeallmessages command that will make translations for all domains (including JavaScript)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vonNiklasson/django-makeallmessages",
    packages=setuptools.find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Utilities',
    ],
    python_requires='>=3.6',
)
