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
        docker_app_name: docker-nuxt
        docker_path: /home/docker-nuxt
        docker_repo: https://github.com/davidsugianto/nuxtjs-pm2.git
        docker_logs: /home/docker-nuxt/logs
        env_source: 
          - {src: '.env-picasso.j2', dest: '/home/docker-nuxt/.env'}
        apps_path: 
          - path: /home/docker-nuxt/public-html/nuxt-staging
          - path: /home/docker-nuxt/public-html/nuxt-production
        apps_repo: 
          - { repo: 'https://github.com/davidsugianto/argocd-app-demo.git', dest: '/home/docker-nuxt/public-html/nuxt-staging'}
          - { repo: 'https://github.com/davidsugianto/argocd-app-demo.git', dest: '/home/docker-nuxt/public-html/nuxt-production'}
        package_json:
          - {src: 'package-nuxt.json.j2', dest: '/home/docker-nuxt/public-html/nuxt-staging/package.json'}
          - {src: 'package-nuxt.json.j2', dest: '/home/docker-nuxt/public-html/nuxt-production/package.json'}
      roles:
        - nuxt-setup-project
