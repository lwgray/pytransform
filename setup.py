from setuptools import setup
setup(
    name = 'pytransform',
    packages = ['pytransform'],
    version = '0.2.3',
    entry_points = {
        "console_scripts": ['transform = pytransform.transform:main']
        },
    description = 'Applies transformation to structures and writes new pdb file',
    author = 'Larry Gray',
    author_email = 'lwgray@gmail.com',
    url = 'https://github.com/lwgray/pyTransform',
    download_url = 'https://github.com/lwgray/pyEntrezId/tarball/0.2.3',
    keywords = ['RNA', 'Molecular Structures', 'Transformation', '3d', 'Computational Biology'],
    classifiers = [],
    install_requires=['MDAnalysis==0.8.1']
)
