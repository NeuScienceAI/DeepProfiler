import setuptools


setuptools.setup(
    name="deep-profiler",
    version="0.1.0",
    author="Juan Caicedo",
    author_email="jcaicedo@gmail.com",
    description=("Tools for representation learning in high throughput image collections"),
    license="BSD",
    keywords="",
    url="https://github.com/jccaicedo/DeepProfiler",
    packages=["deepprofiler"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License"
    ],
    install_requires=[
        "click>=6.7",
        "comet_ml>=1.0",
        "gpyopt>=1.2"
        "keras>=2.2",
        "keras_resnet>=0.1.0",
        "numpy>=1.13",
        "pandas>=0.20.0",
        "scikit-image>=0.13.0",
        "scikit-learn>=0.19.0",
        "scipy>=0.19.0",
        "tensorflow>=1.8",
    ],
    setup_requires=["pytest-runner"],
    tests_requires=[
        "pytest",
        "pytest-cov",
        "codecov"
    ]
)
