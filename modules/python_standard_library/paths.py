from pathlib import Path
from time import ctime
import shutil

path = Path('modules/ecommerce')
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")
paths = [file for file in path.iterdir() if file.is_dir()]
#     print(file)
# # print(path.iterdir())
# print(paths)

python_files = [p for p in path.rglob("*.py")] #Recursively searches and allows for patterns. 
# print(python_files)

init_file = Path('modules/ecommerce/__init__.py')
print(ctime(init_file.stat().st_ctime))

# with open("__init__.py", "r") as file: #Gets rid of needing to manually open and closing a file.

source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py"

shutil.copy(source, target)
target.write_text(source.read_text())