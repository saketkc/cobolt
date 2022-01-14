import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cobolt", # Replace with your own username
    version="0.0.1",
    author="boyinggong",
    author_email="boyinggong@berkeley.edu",
    description="A package for joint analysis of multimodal single-cell sequencing data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/boyinggong/cobolt",
    project_urls={
        "Bug Tracker": "https://github.com/boyinggong/cobolt/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'scipy',
        'torch',
        'umap-learn',
        'python-igraph',
        'sklearn',
        'xgboost',
        'seaborn',
        'leidenalg',
        'tqdm'
    ],
    #package_dir={"": "cobolt"},
    python_requires=">=3.7",
    packages=["cobolt"],
    zip_safe=False,
    include_package_data=True,
)
