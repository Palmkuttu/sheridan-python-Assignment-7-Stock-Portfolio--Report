from setuptools import setup, find_packages

setup(
    name="portfolio-report",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "portfolio_report=portfolio.portfolio_report:main"
        ]
    },
    author="Your Name",
    description="Stock Portfolio Performance Report Generator"
)
