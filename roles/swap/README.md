# Ansible Role : Swap
![enter image description here](https://cumulusnetworks.com/blog/wp-content/uploads/nclu-ansible-1.png)

Ansible Role that create Swap on Linux.

## Requirements
None.

## Directory Structure

    ├── ansible-swap
        ├── roles
            └── swap
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

## Example Playbook 

    - hosts: server
      become: yes
      gather_facts: yes
      remote_user: root
      vars:
        swap_file_size_mb: '2048'
      roles:
        - swap

 