import sys
import os

class VirtualEnvError(RuntimeError):
    pass

def check_current_env(env_name: str = "gil"):
    prefix = sys.prefix
    if env_name not in str(prefix):
        raise VirtualEnvError("Error: The script must be run inside a virtual environment!")

def create_requirements_file(required_libraries: str="beautifulsoup4\npytest\n", file_pash: str="requirements.txt"):
    with open(file_pash, "w") as stream:
        stream.write(required_libraries)

def install_libraries(file_path: str="requirements.txt"):
    result = os.system(f"pip install -r {file_path}")
    if result != 0:
        raise RuntimeError("Error: Libraries are not installed")

def update_requirements_file(file_for_write: str="requirements.txt"):
    libraries = os.popen("pip freeze").read()
    print(libraries)
    with open(file_for_write, "w") as stream:
        stream.write(libraries)


if __name__ == '__main__': 
    """Запуск по умолчанию (по заданию)"""
    check_current_env()
    create_requirements_file()
    install_libraries()
    update_requirements_file()