from setuptools import setup, find_packages
import os

# def package_files(where):
#     paths = []
    
#     for directory in where:
        
#         for (path, directories, filenames) in os.walk(directory):
#             for filename in filenames:
#                 paths.append(os.path.join(path, filename).replace('src/cwlwrapper/', ''))
#     return paths

# extra_files=[]
# # print(extra_files)
# console_scripts = []

# console_scripts.append('{0}={1}.app:entry'.format(find_packages('src')[0].replace('_', '-'),
#                                                   find_packages('src')[0]))
# setup(entry_points={'console_scripts': console_scripts},
#       packages=find_packages(where='src', exclude=['hasard*.sav']),
#       package_dir={'': 'src'},
#       package_data = {'': extra_files})

