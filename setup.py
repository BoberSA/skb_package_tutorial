import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().split()

setuptools.setup(
    name='sbober_fractals',
    version='0.0.1',
    author="Bober S.A.",
    author_email="stas.bober@gmail.com",
    description="Classes for jit-compiled fractal sets calculation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BoberSA/skb_package_tutorial",
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    python_requires='>=3.8, <=3.9'
    )
