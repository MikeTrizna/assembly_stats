import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
    'numpy'
]

setuptools.setup(
    name="assembly_stats",
    version="0.1.4",
    author="Mike Trizna",
    author_email="triznam@si.edu",
    description="Calculates both scaffold and contig statistics (N50, L50, etc.) from a scaffold FASTA file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MikeTrizna/assembly_stats",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'assembly_stats=assembly_stats.cli:cli'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
         # Pick your license as you wish
        'License :: OSI Approved :: MIT License',
    ],
)