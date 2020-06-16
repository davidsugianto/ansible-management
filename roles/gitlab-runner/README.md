
# Ansible Role : Gitlab-runner
![enter image description here](https://about.gitlab.com/images/blogimages/gitlab-ansible-cover.png)

Ansible Role install and configure [Gitlab-runner](https://docs.gitlab.com/runner/)

## Requirements
None.

## Directory Structure

    ├── ansible-letsencrypt
        ├── roles
            └── gitlab-runner
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
	    gitlab_token: 'gitlab_token'  ## gitlab repo token
	    gitlab_runner_name: 'gitlab_runner_name'  ## gitlab runner name
	    gitlab_runner_tags: 'gitlab_runner_tags'  ## gitlab runner tags\
	    gitlab_runner_executor: gitlab_runner_executor  ## gitlab runner executor
	    gitlab_runner_builds_dir: '/home/gitlab-runner/admin_sh/builds'  ## gitlab runner initial repo project
	    gitlab_runner_cache_dir: '/home/gitlab-runner/admin_sh/cache'  ## gitlab runner repo cache
	    gitlab_runner_description: 'gitlab_runner_description'  ## gitlab runner description
	    gitlab_runner_docker_volumes: ## choose docker executor
	       - "/path/apps:/path/builds"  ## docker volume apps
	    gitlab_directory: ## gitlab directory
	       - { dest: '/path/path', mode: '0777'} ## directory  
	       - { dest: '/path/path', mode: '0777'} ## directory
	       - { dest: '/path/path', mode: '0777'} ## directory
      roles:
        - gitlab-runner

 
## Example Playbook RedHat Base

    - hosts: server_redhat_base
      become: yes
      gather_facts: yes
      tags: ansible_os_family == 'RedHat'
      remote_user: root
      vars:
	    gitlab_token: 'gitlab_token'  ## gitlab repo token
	    gitlab_runner_name: 'gitlab_runner_name'  ## gitlab runner name
	    gitlab_runner_tags: 'gitlab_runner_tags'  ## gitlab runner tags\
	    gitlab_runner_executor: gitlab_runner_executor  ## gitlab runner executor
	    gitlab_runner_builds_dir: '/home/gitlab-runner/admin_sh/builds'  ## gitlab runner initial repo project
	    gitlab_runner_cache_dir: '/home/gitlab-runner/admin_sh/cache'  ## gitlab runner repo cache
	    gitlab_runner_description: 'gitlab_runner_description'  ## gitlab runner description
	    gitlab_runner_docker_volumes: ## choose docker executor
	       - "/path/apps:/path/builds"  ## docker volume apps
	    gitlab_directory: ## gitlab directory
           - { dest: '/path/path', mode: '0777'} ## directory  
           - { dest: '/path/path', mode: '0777'} ## directory
           - { dest: '/path/path', mode: '0777'} ## directory
      roles:
        - gitlab-runner
      roles:
        - letsencrypt
     
