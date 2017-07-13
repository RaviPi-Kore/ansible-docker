igrybkov.docker
=========

Install Docker and its dependencies:
- Packages required to execute docker commands by Ansible
- Docker-compose

Requirements
------------

Any Ubuntu system.

Role Variables
--------------

`docker_apt_key_url` &mdash; url of the repository key

`docker_apt_key_sig` &mdash; apt repository key signature

`docker_apt_repository` &mdash; url of the apt repository with docker packages

`docker_compose_version` &mdash; version of docker-compose to be installed. Can be latest, blank or contain specific version.

`docker_group` &mdash; name of the group used by docker

`docker_users` &mdash; users who will be added to docker group

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: all
      roles:
         - { role: igrybkov.docker, docker_compose_version: "1.8.1" }

License
-------

MIT License
