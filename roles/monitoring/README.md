# Ansible Role : Monitoring

![enter image description here](https://www.eginnovations.com/blog-amp/wp-content/uploads/2019/08/universal-management-pack-scom-1024x768.jpg)

Ansible Role that Setup monitoring apps on server.

## Requirements

None.

## Directory Structure

    ├── ansible-monitoring
        ├── roles
            └── monitoring
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

      hosts: ubuntu
      become: yes
      gather_facts: yes
      remote_user: root
      vars:
        docker_app_name: docker-monitoring-tig
        docker_path: /home/docker-monitoring-tig
        docker_repo: git@gitlab.com:picasso-code/docker-monitoring-tig.git
        docker_logs: /home/docker-monitoring-tig/logs
      roles:
        - monitoring
