# Ansible Role : NGINX Bad Blocker
![enter image description here](https://whitesmith-website.s3.amazonaws.com/2016/Feb/ansible-1456397742246.png)
![enter image description here](https://raw.githubusercontent.com/mitchellkrogza/nginx-ultimate-bad-bot-blocker/master/.assets/_logo_nginx_bad_bot_blocker.png)

Ansible Role that install and setup [nginx-ultimate-bad-bot-blocker](https://github.com/mitchellkrogza/nginx-ultimate-bad-bot-blocker) on Linux.

## Requirements
None.

## Directory Structure

    ├── ansible-nginx-bad-blocker
        ├── roles
            └── bad-blocker
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
      roles:
        - bad-blocker

 