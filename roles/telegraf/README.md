# Ansible Role : Telegraf

![enter image description here](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs_XIbM1Q5QMoI0pSJTJm6gTokDtKB0xWKfaGlECgm1rezPjwy&s)

Ansible Role that install and configure telegraf metrics agent on Linux.

## Requirements

None.

## Directory Structure

    ├── ansible-telegraf
        ├── roles
            └── telegraf
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
        telegraf_agent: telegraf.conf
      roles:
        - telegraf

## Example Playbook RedHat Base

    - hosts: server
      become: yes
      gather_facts: yes
      remote_user: root
      vars:
        telegraf_agent: telegraf.conf
      roles:
        - telegraf
