from setuptools import setup
setup(
    name = 'pytransform',
    packages = ['pytransform'],
    version = '0.1.1',
    entry_points = {
        "console_scripts": ['pytransform = pytransform.pytransform:main']
        },
    description = 'Applies transformation to structures and writes new pdb file',
    author = 'Larry Gray',
    author_email = 'lwgray@gmail.com',
    url = 'https://github.com/lwgray/pyTransform',
    download_url = 'https://github.com/lwgray/pyEntrezId/tarball/0.1.1',
    keywords = ['RNA', 'Molecular Structures', 'Transformation', '3d', 'Computational Biology'],
    classifiers = [],
    install_requires=['numpy==1.10.4', 'MDAnalysis==0.13.0']
)
