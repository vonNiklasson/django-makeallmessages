import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


packages = []
for package in setuptools.find_packages():
    if not package.startswith('tests'):
        packages.append(package)

setuptools.setup(
    name="django-makeallmessages",
    version="0.2.0",
    author="Johan Niklasson",
    author_email="johan@niklasson.me",
    description="Django Makeallmessages is a tool designed to ease the message making in your Django project.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vonNiklasson/django-makeallmessages",
    packages=packages,
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
    python_requires='>=3.5',
)
