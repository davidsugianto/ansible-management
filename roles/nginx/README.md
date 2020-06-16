# Ansible Role : NGINX
![enter image description here](https://www.nginx.com/wp-content/uploads/2018/02/ansible-unified-role_featured.jpg)

Ansible Role that installs [NGINX](https://www.nginx.com/) on Linux.

## Requirements
None.

## Directory Structure

    ├── ansible-nginx
        ├── roles
            └── nginx
        ├── hosts
        ├── playbook.yml
        └── README.md

## Example hosts

    # Ansible host config
    # run command: ansible -i hosts -m ping all
    
    [server]
    server_ip
    [server:vars]
    ansible_ssh_port=22
    ansible_ssh_user=root
    ansible_python_interpreter=/usr/bin/python3

## Example Playbook Debian Base

    - hosts: server
      become: yes
      gather_facts: yes
      tags: ansible_os_family == 'Debian'
      remote_user: root
      roles:
        - nginx

 
## Example Playbook Ubuntu Base

    - hosts: server
      become: yes
      gather_facts: yes
      tags: ansible_os_family == 'Ubuntu'
      remote_user: root
      roles:
        - nginx

 
## Example Playbook RedHat Base

    - hosts: server
      become: yes
      gather_facts: yes
      tags: ansible_os_family == 'RedHat'
      remote_user: root
      roles:
        - nginx

 