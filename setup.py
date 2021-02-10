from setuptools import setup, find_packages
#sudo apt install libtiff-dev libqt4-dev

INSTALL_REQUIREMENTS = [
    #'tensorflow==2.3.1',
    #'scikit-build==0.11.1',
    #'opencv-python',

    'albumentations==0.4.6',
    'Flask==1.1.2',
    'pydicom==2.0.0',
    'numpy==1.17.0',
    #'pyparsing',
    #'scikit_build',
    #'efficientnet==1.1.1',
    'boto3==1.16.9',
    'pandas==1.0.1',
    'SimpleITK==1.2.0',
    
    #'Pillow==7.1.2',
    #'Keras==2.2.4',
    #'scikit-image==0.16.1',
    #'dicompyler-core==0.5.5',
    #'keras-retinanet==0.5.1',
    'Werkzeug==1.0.1',
    'python-logstash==0.4.6',
    'imantics==0.1.12',
]


setup(
    name="py_package",
    description="dummy package",
    long_description="Deneme",
    long_description_content_type="text/markdown",
    author="m",
    license="MIT",
    url="https://github.com/mertyergin/pypackage",
    python_requires=">=3.7",
    install_requires=INSTALL_REQUIREMENTS,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
