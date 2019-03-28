import zipimport
import zipfile

pyfile = 'zip_test.py'
zfile = 'zip_test.zip'


def zip_file() -> None:
    with zipfile.ZipFile(zfile, 'w') as zf:
        zf.writestr(pyfile, code)

# --- step1 ---


code = '''
def func():
    return 1
'''

zip_file()

importer = zipimport.zipimporter('zip_test.zip')

module = importer.load_module('zip_test')
print(module.func())


# --- step2 ---

code = '''
def func():
    return 2
'''

zip_file()

importer = zipimport.zipimporter('zip_test.zip')

module = importer.load_module('zip_test')
print(module.func())
