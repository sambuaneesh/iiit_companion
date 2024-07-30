from setuptools import setup, find_packages

setup(
    name="iiit_companion",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit>=1.10.0",
    ],
    entry_points={
        "console_scripts": [
            "iiit-companion=app.main:run_builder_app",
        ],
    },
)
