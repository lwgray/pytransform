from setuptools import setup
setup(
    name = 'pytransform',
    packages = ['pytransform'],
    version = '0.1.0',
    entry_points = {
        "console_scripts": ['pytransform = pytransform.pytransform:main']
        },
    description = 'Applies transformation to structures and writes new pdb file',
    author = 'Larry Gray',
    author_email = 'lwgray@gmail.com',
    url = 'https://github.com/lwgray/pyTransform',
    download_url = 'https://github.com/lwgray/pyEntrezId/tarball/0.1.0',
    keywords = ['RNA', 'Molecular Structures', 'Transformation', '3d', 'Computational Biology'],
    classifiers = [],
    install_requires=['biopython==1.66', 'cffi==1.5.0', 'cryptography==1.2.1', 'decorator==4.0.9',
    'ecdsa==0.13', 'enum34==1.1.2', 'fpconst==0.7.2', 'GridDataFormats==0.3.2', 'MDAnalysis==0.13.0',
    'networkx==1.11', 'numpy==1.10.4', 'paramiko==1.16.0', 'ply==3.8', 'pycparser==2.14',
    'pycrypto==2.6.1', 'pyOpenSSL==0.15.1', 'rsa==3.3', 'six==1.10.0', 'stevedore==1.10.0',
    'virtualenv==14.0.6', 'virtualenv-clone==0.2.6', 'VirtualEnvOnDemand==4.1.0',
    'virtualenvwrapper==4.7.1', 'wheel==0.29.0']
)
