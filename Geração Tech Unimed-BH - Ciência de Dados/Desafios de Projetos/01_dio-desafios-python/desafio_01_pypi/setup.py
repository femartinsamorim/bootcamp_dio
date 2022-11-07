from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="projeto.py",
    version="0.0.1",
    author="felipe_amorim",
    author_email="felipeamorim@email.com",
    description="Projeto teste criado para aprendizado",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/femartinsamorim/dio_desafiopypi.git"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)