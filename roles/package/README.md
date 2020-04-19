# Ansible Role : package

![enter image description here](https://i.imgur.com/ti2VR6r.jpg)

Ansible Role that install package dependencies on Linux.

## Requirements

None.

## Directory Structure

    ├── ansible-package
        ├── roles
            └── package
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
      vars:
        deb_package:
          - name: git
          - name: wget
          - name: etc
      roles:
        - package

## Example Playbook RedHat Base

    - hosts: server
      become: yes
      gather_facts: yes
      remote_user: root
      vars:
        redhat_package:
          - name: git
          - name: wget
          - name: etc
      roles:
        - package
