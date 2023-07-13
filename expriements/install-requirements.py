import os
import subprocess


def create_virtual_environment():
    # Create a virtual environment directory
    subprocess.run(['python', '-m', 'venv', 'env'])
    print("Virtual environment 'env' created.")


def activate_virtual_environment():
    # Activate the virtual environment
    if os.name == 'nt':
        activate_script = 'env\\Scripts\\activate.bat'
    else:
        activate_script = 'env/bin/activate'

    subprocess.run([activate_script], shell=True)
    print("Virtual environment activated.")


def install_requirements():
    # Install packages from requirements.txt
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
    print("Packages installed.")


def main():
    # Create and activate the virtual environment
    create_virtual_environment()
    activate_virtual_environment()

    # Install the packages from requirements.txt
    install_requirements()


if __name__ == '__main__':
    main()
