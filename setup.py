from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in imprest_and_petty_cash_management/__init__.py
from imprest_and_petty_cash_management import __version__ as version

setup(
	name="imprest_and_petty_cash_management",
	version=version,
	description="Imprest Requisition and Surrender, Petty Cash Management",
	author="MCBTechnologies",
	author_email="koriojohn59@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
