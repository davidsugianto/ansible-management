# Ansible Role : Firewalld
![enter image description here](https://engineering.nordeus.com/content/images/2018/09/ansible-red-cover.jpg)

Ansible Role that installs [firewalld](https://firewalld.org/) on Linux.

## Requirements
None.

## Directory Structure

    ├── ansible-firewalld
        ├── roles
            └── firewalld
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
      vars:
        ansible_python_interpreter: '/usr/bin/python3'
        firewall_service:
          - service: ssh
          - service: http
          - service: https
        firewall_port:
          - port: 8250/tcp
          - port: 9250/tcp
      roles:
        - firewalld

 
## Example Playbook RedHat Base

    - hosts: server_redhat_base
      become: yes
      gather_facts: yes
      tags: ansible_os_family == 'RedHat'
      remote_user: root
      vars:
        firewall_service:
          - service: ssh
          - service: http
          - service: https
        firewall_port:
          - port: 8250/tcp
          - port: 9250/tcp
      roles:
        - firewalld
