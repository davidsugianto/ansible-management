# Ansible Role : EPEL Repo
![enter image description here](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLSZP7uzznzopAPPQL1nt5xMHhB-yNCyfNlnZGmCX-6xDmyscU3A&s)

Ansible Role that installs [EPEL-Repo](https://fedoraproject.org/wiki/EPEL) on Linux.

## Requirements
None.

## Directory Structure

    ├── ansible-repo-epel
        ├── roles
            └── repo-epel
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
        ansible_python_interpreter=/usr/bin/python2.7

## Example Playbook

    - hosts: server
      become: yes
      gather_facts: yes
      remote_user: root
      roles:
        - repo-epel

 