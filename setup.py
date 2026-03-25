from setuptools import setup, find_packages
setup(
    name="trastornos-neurocognitivos-demencia-america-latina-2000-2025",
    version="1.0.0",
    description="Trastornos Neurocognitivos y Demencia en América Latina e Iberoamérica (2000-2025)",
    author="de la Serna, Juan Moisés",
    url="https://github.com/juanmoisesd/trastornos-neurocognitivos-demencia-america-latina-2000-2025",
    packages=find_packages(),
    install_requires=["pandas>=1.3.0","requests>=2.26.0"],
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Topic :: Scientific/Engineering"],
    keywords="zenodo, open-data",
)