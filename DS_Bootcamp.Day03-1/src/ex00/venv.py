import os

if __name__ == '__main__':
    current_venv = os.environ.get('VIRTUAL_ENV')
    print(f"Your current virtual env is {current_venv}")