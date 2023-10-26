import shutil
import tempfile
import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)
print(tmp_file)
with open(tmp_file.name) as file:
    file_contents = file.read
    print(file_contents)
    pass

