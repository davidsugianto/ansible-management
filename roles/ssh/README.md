# Ansible Role : SSH

![enter image description here](https://www.hostinger.co.id/tutorial/wp-content/uploads/sites/11/2017/04/cara-menggunakan-command-ssh.png)

Ansible Role that generate ssh key on Linux.

## Requirements

None.

## Notes

    ssh_pub: ssh key yg sudah di generate di local
    ssh_private: ssh key yg sudah di generate di local
    terus di copy ke ssh/template

## Directory Structure

    ├── ansible-ssh
        ├── roles
            └── ssh
                ├── templates
                └── etc
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
        ssh_pub: id_rsa 
        ssh_private: id_rsa.pub
      roles:
        - ssh
