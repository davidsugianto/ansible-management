
# Ansible Role : Pip

![enter image description here](https://miro.medium.com/max/2632/1*8Zh-mzLnVMDsbvXdKsU4lw.png)

Ansible Role that installs [python-pip package](https://pypi.org/) on Linux.

## Requirements
None.

## Directory Structure

    ├── ansible-pip
        ├── roles
            └── pip
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
    ansible_python_interpreter=/usr/bin/python


## Example Playbook Debian Base

    - hosts: server_debian_base
      become: yes
      gather_facts: yes
      tags: ansible_os_family == 'Debian'
      remote_user: root
      vars:
        pip_package: python3-pip
        pip_install_packages:
          - name: docker
          - name: awscli
      roles:
        - pip

 
## Example Playbook RedHat Base

    - hosts: server_redhat_base
      become: yes
      gather_facts: yes
      tags: ansible_os_family == 'RedHat'
      remote_user: root
      vars:
        pip_package: python-pip
        pip_install_packages:
          - name: docker
          - name: awscli
      roles:
        - pip

 