# Ansible Role : Database

![enter image description here](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9bimIb5sgifwM8GIrOHaT4KTQsQQLe2C-1-NPRg5s2tgkEhi0&s)

Ansible Role that Setup Database on server.

## Requirements

None.

## Directory Structure

    ├── ansible-database
        ├── roles
            └── database
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

    - hosts: ubuntu
      become: yes
      gather_facts: yes
      remote_user: root
      vars:
        docker_app_name: docker-postgresql
        docker_path: /home/docker-postgresql
        docker_repo: git@gitlab.com:picasso-code/docker-postgresql.git
        docker_logs: /home/docker-postgresql/logs
        env_source:
          - { src: '.env.j2', dest: '/home/docker-postgresql' }
      roles:
        - database
