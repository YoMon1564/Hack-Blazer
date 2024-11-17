import importlib
print("<DigitalTrailBlazer>")
def check_library_installed(library_name):
    try:
        importlib.import_module(library_name)
        return True
    except ImportError:
        return False
library_to_check = input("library <<")
if check_library_installed(library_to_check):
    print(f"{library_to_check} 已安装。")
else:
    print(f"{library_to_check} 未安装。")