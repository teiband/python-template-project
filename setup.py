import os
import io
from setuptools import setup, find_packages


def get_data_files(exclude_folders=None):
    """Generates the tuples for the ``data_files`` argument of the ``setup`` function

    The function traverses into the ``share`` folder and adds every file to the list of data files that is not located
    within one of the ``exclude_folders``.

    :param list exclude_folders: Optional list of folder to not include into the data files
    :return: list of data file tuples [(dir1, [file1, file2), ...]
    """
    exclude_folders = exclude_folders or []
    data_files_dir = os.path.join(".", 'share')
    data_files = []
    for path, subdirs, files in os.walk(data_files_dir):
        folder_name = os.path.basename(path)
        if folder_name in exclude_folders:
            subdirs[:] = []
            continue
        data_files.append((path, [os.path.join(path, file) for file in files]))
    return data_files


readme_file_path = os.path.join(".", "README.md")
with open(readme_file_path, "r") as f:
    long_description = f.read()

setup(
    install_requires=[
        # define packages to be installed, e.g. package, or package==1.2.3
    ],
    name="TODO",
    version="TODO", # use semver, e.g. 1.2.3
    description="TODO",
    long_description=long_description,
    url="TODO",
    author="Thomas Eiband",
    author_email="thomas.eiband@dlr.de",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages("src"),
    data_files=get_data_files(exclude_folders=["TODO"]),

    entry_points={
        'console_scripts': [
            'execution = TODO:main'
        ]
    },
    zip_safe=False
)
