import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_file(host):
    f = host.file('/usr/bin/docker')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0755'


def test_docker_daemon(host):
    p = host.process.get(user="root", comm="docker")
    assert p


def test_docker_socket(host):
    socket = host.socket('unix:///var/run/docker.sock')
    assert socket.is_listening


def test_docker_port(host):
    socket = host.socket("tcp://0.0.0.0:2375")
    assert socket.is_listening
