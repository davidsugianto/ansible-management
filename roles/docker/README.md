# Ansible Role : Docker

![enter image description here](https://www.ansible.com/hubfs/2016_Images/Blog_Headers/Ansible-Docker-Blog-2.png)

Ansible Role that installs [Docker](https://www.docker.com/) on Linux.

## Requirements

None.

## Directory Structure

    ├── ansible-docker
        ├── roles
            └── docker
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

    - hosts: server_debian_base
      become: yes
      gather_facts: yes
      tags: ansible_os_family == 'Debian'
      remote_user: root
      roles:
        - docker

## Example Playbook RedHat Base

    - hosts: server_redhat_base
      become: yes
      gather_facts: yes
      tags: ansible_os_family == 'RedHat'
      remote_user: root
      roles:
        - docker

## Ansible Playbook (and  `docker`  Python library) Debian Base

    - hosts: server_debian_base
      become: yes
      gather_facts: yes
      tags: ansible_os_family == 'Debian'
      remote_user: root
      vars:
        pip_package: python3-pip
        pip_install_packages:
          - name: docker
          - name: docker-compose
      roles:
        - pip
        - docker

## Ansible Playbook (and  `docker`  Python library) RedHat Base

    - hosts: server_debian_base
      become: yes
      gather_facts: yes
      tags: ansible_os_family == 'RedHat'
      remote_user: root
      vars:
        pip_package: python-pip
        pip_install_packages:
          - name: docker
          - name: docker-compose
      roles:
        - pip
        - docker
