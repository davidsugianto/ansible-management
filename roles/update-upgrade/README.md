# Ansible Role : Updates Upgrades
![enter image description here](https://cumulusnetworks.com/blog/wp-content/uploads/nclu-ansible-1.png)

Ansible Role that update and upgrade package on Linux.

## Requirements
None.

## Directory Structure

    ├── ansible-updates-upgrades
        ├── roles
            └── update-upgrade
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
      remote_user: root
      tags: ansible_os_family == 'Debian'
      roles:
        - update-upgrade

 
 ## Example Playbook RedHat Base

    - hosts: server
      become: yes
      gather_facts: yes
      remote_user: root
      tags: ansible_os_family == 'RedHat'
      roles:
        - update-upgrade

 