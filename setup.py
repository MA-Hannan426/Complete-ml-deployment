import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.1.0"

REPO_NAME = "Complete-ml-deployment"
AUTHOR_USER_NAME = "MA-Hannan426"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "ma.hannan230@gmail.com"
LICENSE = "MIT"
DESCRIPTION = "A complete machine learning deployment project" 
PACKAGE_NAME = "complete_ml_deployment" # This should match your src directory name 

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)