import os
import re
import shutil
import subprocess
import datetime
import pytz
from tabulate import tabulate


def create_directory(domain):
    # Create the full path for the domain directory
    domain_dir = os.path.join('/var/www', domain)

    # Check if the domain directory already exists
    if not os.path.exists(domain_dir):
        # Create the domain directory
        os.makedirs(domain_dir)
        print(f"The directory for domain '{domain}' has been created.")
    else:
        print(f"The directory for domain '{domain}' already exists.")

    # Add a default index file to the domain directory
    index_file_path = os.path.join(domain_dir, 'index.html')
    with open(index_file_path, 'w') as index_file:
        index_file.write('<html><body><h1>Welcome to ' + domain + '</h1></body></html>')
    print(f"The default index file has been added to the domain directory.")


def create_vhost(domain, admin_email, php_version):
    # Add the ".local" suffix to the domain name if not already present
    domain_with_suffix = domain + ".local" if not domain.endswith(".local") else domain

    # Create a new virtual host configuration file
    vhost_template = f"""
    <VirtualHost *:80>
        ServerAdmin {admin_email}
        ServerName {domain_with_suffix}
        ServerAlias www.{domain_with_suffix}
        DocumentRoot /var/www/{domain}

        <Directory /var/www/{domain}>
            Options Indexes FollowSymLinks MultiViews
            AllowOverride All
            Require all granted
            Allow from all
        </Directory>

        ErrorLog ${{APACHE_LOG_DIR}}/{domain}_error.log
        CustomLog ${{APACHE_LOG_DIR}}/{domain}_access.log combined

        <IfModule mod_deflate.c>
            AddOutputFilterByType DEFLATE text/html text/plain text/xml text/css application/javascript
        </IfModule>

        <IfModule mod_php{php_version}.c>
            php_admin_flag engine on
        </IfModule>
    </VirtualHost>
    """

    # Save the virtual host configuration file
    vhost_filename = f"/etc/apache2/sites-available/{domain_with_suffix}.conf"
    with open(vhost_filename, 'w') as vhost_file:
        vhost_file.write(vhost_template)

    # Enable the virtual host
    subprocess.run(['a2ensite', domain_with_suffix])

    # Enable mod_deflate (gzip) module
    subprocess.run(['a2enmod', 'deflate'])

    # Reload Apache to apply the changes
    subprocess.run(['systemctl', 'reload', 'apache2'])


def update_hosts_file(domain, new_domain=None):
    # Add the ".local" suffix to the domain name if not already present
    domain_with_suffix = domain + ".local" if not domain.endswith(".local") else domain

    # Update the hosts file
    hosts_file = '/etc/hosts'
    with open(hosts_file, 'r') as hosts:
        hosts_content = hosts.read()
    if new_domain:
        new_domain_with_suffix = new_domain + ".local"
        hosts_content = hosts_content.replace(f"127.0.0.1 {domain_with_suffix}", f"127.0.0.1 {new_domain_with_suffix}")
        print(f"The domain name has been updated to '{new_domain}'.")
    else:
        if f"127.0.0.1 {domain_with_suffix}" not in hosts_content:
            hosts_content += f"\n127.0.0.1 {domain_with_suffix}"
            print(f"The hosts file has been updated with the domain '{domain_with_suffix}'.")
        else:
            print(f"The domain '{domain_with_suffix}' already exists in the hosts file.")
    with open(hosts_file, 'w') as hosts:
        hosts.write(hosts_content)


def update_domain(domain):
    # Get the updated domain name, root path, and admin email from the user
    new_domain = input("Enter the new domain name (leave blank to keep the current domain name): ")
    new_root_path = input("Enter the new root path (leave blank to keep the current root path): ")
    new_admin_email = input("Enter the new admin email (leave blank to keep the current admin email): ")
    new_php_version = input("Enter the new PHP version (e.g., 7.4): ")

    # Check if any update options are provided
    update_domain_name = new_domain != ""
    update_root_path = new_root_path != ""
    update_admin_email = new_admin_email != ""
    update_php_version = new_php_version != ""

    # Add the ".local" suffix to the domain name if not already present
    domain_with_suffix = domain + ".local" if not domain.endswith(".local") else domain

    # Add the ".local" suffix to the new domain name if provided and not already present
    new_domain_with_suffix = new_domain + ".local" if new_domain and not new_domain.endswith(".local") else new_domain

    # Rename the domain directory if updating the domain name
    if update_domain_name:
        base_dir = '/var/www'
        old_dir = os.path.join(base_dir, domain)
        new_dir = os.path.join(base_dir, new_domain)
        os.rename(old_dir, new_dir)
        print(f"The directory for domain '{domain}' has been renamed to '{new_domain}'.")

    # Update the virtual host configuration file
    if update_domain_name or update_root_path or update_admin_email or update_php_version:
        vhost_filename = f"/etc/apache2/sites-available/{domain_with_suffix}.conf"
        if os.path.exists(vhost_filename):
            with open(vhost_filename, 'r') as vhost_file:
                vhost_content = vhost_file.read()

            if update_root_path:
                vhost_content = vhost_content.replace(f"/var/www/{domain}", new_root_path)

            if update_admin_email:
                vhost_content = re.sub(r'ServerAdmin\s+(.+)', f'ServerAdmin {new_admin_email}', vhost_content)

            if update_php_version:
                vhost_content = re.sub(r'mod_php([0-9.]+)\.c', f'mod_php{new_php_version}.c', vhost_content)

            with open(vhost_filename, 'w') as vhost_file:
                vhost_file.write(vhost_content)
            print(f"The virtual host configuration file has been updated for domain '{domain}'.")
        else:
            print(f"Virtual host configuration file not found for domain '{domain}'. Skipping update.")

    # Perform the necessary updates in the hosts file
    if update_domain_name:
        update_hosts_file(domain, new_domain)


def delete_domain(domain):
    # Add the ".local" suffix to the domain name if not already present
    domain_with_suffix = domain + ".local" if not domain.endswith(".local") else domain

    # Remove the virtual host configuration file
    vhost_filename = f"/etc/apache2/sites-available/{domain_with_suffix}.conf"
    if os.path.exists(vhost_filename):
        os.remove(vhost_filename)
        print(f"The virtual host configuration file for domain '{domain_with_suffix}' has been deleted.")

    # Check if the domain vhost file is added with the suffix
    vhost_filename_without_suffix = f"/etc/apache2/sites-available/{domain}.conf"
    if os.path.exists(vhost_filename_without_suffix):
        os.remove(vhost_filename_without_suffix)
        print(f"The virtual host configuration file for domain '{domain}' has been deleted.")

    # Disable the virtual host
    subprocess.run(['a2dissite', domain_with_suffix])

    # Remove the domain directory if it exists
    domain_dir = os.path.join('/var/www', domain_with_suffix)
    if os.path.exists(domain_dir):
        shutil.rmtree(domain_dir)
        print(f"The directory for domain '{domain_with_suffix}' has been deleted.")
    elif os.path.exists(os.path.join('/var/www', domain)):
        shutil.rmtree(os.path.join('/var/www', domain))
        print(f"The directory for domain '{domain}' has been deleted.")
    else:
        print(f"The directory for domain '{domain_with_suffix}' doesn't exist. Skipping deletion.")

    # Update the hosts file
    hosts_file = '/etc/hosts'
    with open(hosts_file, 'r') as hosts:
        hosts_content = hosts.read()
    hosts_content = re.sub(rf"(127\.0\.0\.1\s+){domain_with_suffix}", '', hosts_content)
    with open(hosts_file, 'w') as hosts:
        hosts.write(hosts_content)
    print(f"The domain '{domain_with_suffix}' has been removed from the hosts file.")

    # Reload Apache to apply the changes
    subprocess.run(['systemctl', 'reload', 'apache2'])


def get_installed_date(domain):
    # Add the ".local" suffix to the domain name if not already present
    domain_with_suffix = domain + ".local" if not domain.endswith(".local") else domain

    # Check if the domain directory exists with the suffix
    domain_dir_with_suffix = os.path.join('/var/www', domain_with_suffix)
    if os.path.exists(domain_dir_with_suffix):
        installed_timestamp = os.path.getctime(domain_dir_with_suffix)
        installed_date = datetime.datetime.fromtimestamp(installed_timestamp, pytz.timezone('UTC')).astimezone()
        return installed_date.strftime('%Y-%m-%d %H:%M:%S')

    # Check if the domain directory exists without the suffix
    domain_dir_without_suffix = os.path.join('/var/www', domain)
    if os.path.exists(domain_dir_without_suffix):
        installed_timestamp = os.path.getctime(domain_dir_without_suffix)
        installed_date = datetime.datetime.fromtimestamp(installed_timestamp, pytz.timezone('UTC')).astimezone()
        return installed_date.strftime('%Y-%m-%d %H:%M:%S')

    return ""


def show_installed_domains():
    # Read the hosts file
    hosts_file = '/etc/hosts'
    with open(hosts_file, 'r') as hosts:
        hosts_content = hosts.read()

    # Get the list of domains from the hosts file
    domain_names = list(set(re.findall(r"127\.0\.0\.1\s+(.+)\.local", hosts_content)))

    if domain_names:
        # Create a table with the domain details
        table_data = []
        for i, domain in enumerate(domain_names, start=1):
            vhost_filename = f"/etc/apache2/sites-available/{domain}.conf"
            admin_email = ""
            php_version = "system"
            installed_date = get_installed_date(domain)
            installed_path = ""
            if os.path.exists(vhost_filename):
                with open(vhost_filename, 'r') as vhost_file:
                    vhost_content = vhost_file.read()

                admin_email_match = re.search(r'ServerAdmin\s+(.+)', vhost_content)
                admin_email = admin_email_match.group(1) if admin_email_match else ""

                php_version_match = re.search(r'mod_php([0-9.]+)\.c', vhost_content)
                php_version = php_version_match.group(1) if php_version_match else "system"

            domain_dir_with_suffix = os.path.join('/var/www', domain + ".local")
            domain_dir_without_suffix = os.path.join('/var/www', domain)
            if os.path.exists(domain_dir_with_suffix):
                installed_path = os.path.abspath(domain_dir_with_suffix)
            elif os.path.exists(domain_dir_without_suffix):
                installed_path = os.path.abspath(domain_dir_without_suffix)

            table_data.append([i, domain, installed_path, admin_email, php_version, installed_date])

        # Print the table
        headers = ["Serial", "Domain Name", "Installed Path", "Admin Email", "PHP Version", "Installed Date"]
        print(tabulate(table_data, headers=headers, tablefmt="pretty"))
    else:
        print("No domains installed.")


def install_wordpress(domain):
    # Change to the domain directory
    os.chdir(f"/var/www/{domain}")

    # Run the WP-CLI command to download and install WordPress
    subprocess.run(['wp', 'core', 'download', '--allow-root'])

    # Delete the index.html file
    index_file = os.path.join('/var/www', domain, 'index.html')
    if os.path.exists(index_file):
        os.remove(index_file)
        print("The default index.html file has been deleted.")

    print(f"WordPress has been installed for domain '{domain}'.")


def install_laravel(domain, use_suffix=True):
    # Change to the domain directory
    os.chdir(f"/var/www/{domain}")

    # Run the Composer command to create a new Laravel project
    subprocess.run(['composer', 'create-project', '--prefer-dist', 'laravel/laravel', '.'])

    # Delete the index.html file
    index_file = os.path.join('/var/www', domain, 'index.html')
    if os.path.exists(index_file):
        os.remove(index_file)
        print("The default index.html file has been deleted.")

    print(f"Laravel has been installed for domain '{domain}'.")


def install_django(domain):
    # Change to the domain directory
    os.chdir(f"/var/www/{domain}")

    # Create a Python virtual environment
    subprocess.run(['python3', '-m', 'venv', 'env'])
    activate_script = os.path.join('env', 'bin', 'activate')
    subprocess.run(['source', activate_script], shell=True)

    # Run the pip command to install Django
    subprocess.run(['pip', 'install', 'Django'])

    # Delete the index.html file
    index_file = os.path.join('/var/www', domain, 'public', 'index.html')
    if os.path.exists(index_file):
        os.remove(index_file)
        print("The default index.html file has been deleted.")

    print(f"Django has been installed for domain '{domain}'.")


def install_applications(domain):
    install_option = input("Choose an installation option: (1) WordPress, (2) Laravel, (3) Django, (4) Skip: ")
    if install_option == "1":
        install_wordpress(domain)
    elif install_option == "2":
        install_laravel(domain)
    elif install_option == "3":
        install_django(domain)
    elif install_option == "4":
        pass
    else:
        print("Invalid installation option. Skipping installation.")


def main():
    # Get the action from the user
    action = input(
        "Choose an action: (1) Install Apps, (2) Create, (3) Update, (4) Delete, (5) Show Installed Domains: ")

    if action == "1":
        domain = input("Enter the domain name to install application: ")
        install_applications(domain)
    elif action == "2":
        domain = input("Enter the domain name: ")
        admin_email = input("Enter the admin email: ")
        php_version = input("Enter the PHP version (e.g., 7.4): ")
        create_directory(domain)
        create_vhost(domain, admin_email, php_version)
        update_hosts_file(domain)
        install_applications(domain)
    elif action == "3":
        domain = input("Enter the domain name to update: ")
        update_domain(domain)
    elif action == "4":
        domain = input("Enter the domain name to delete: ")
        delete_domain(domain)
    elif action == "5":
        show_installed_domains()
    else:
        print("Invalid action. Please choose a valid action.")


if __name__ == '__main__':
    main()
