# Ansible Role : Setup Nuxt Project

![enter image description here](https://miro.medium.com/max/798/1*EWDEUt0fqsmRgpYGFOOMew.png)

Ansible Role that setup nuxt project on Linux.

## Requirements

None.

## Directory Structure

    ├── ansible-nuxt-setup
        ├── roles
            └── nuxt-setup-project
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
        docker_app_name: docker-frontend-hotel
        docker_path: /home/docker-frontend-hotel
        docker_repo: git@gitlab.com:picasso-code/docker-frontend-hotel.git
        docker_logs: /home/docker-frontend-hotel/logs
        env_source: 
          - {src: '.env-picasso.j2', dest: '/home/docker-frontend-hotel/.env'}
        apps_path: 
          - path: /home/docker-frontend-hotel/public-html/hotel-staging
          - path: /home/docker-frontend-hotel/public-html/hotel-production
          - path: /home/docker-frontend-hotel/public-html/member-staging
          - path: /home/docker-frontend-hotel/public-html/member-production
        apps_repo: 
          - { repo: 'git@gitlab.com:picasso-code/hotel-landing.git', dest: '/home/docker-frontend-hotel/public-html/hotel-staging'}
          - { repo: 'git@gitlab.com:picasso-code/hotel-landing.git', dest: '/home/docker-frontend-hotel/public-html/hotel-production'}
        package_json:
          - {src: 'package-member.json.j2', dest: '/home/docker-frontend-hotel/public-html/member-staging/package.json'}
          - {src: 'package-hotel.json.j2', dest: '/home/docker-frontend-hotel/public-html/hotel-staging/package.json'}
      roles:
        - nuxt-setup-project
