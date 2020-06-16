import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


# def test_hosts_file(host):
#     f = host.file('/etc/hosts')

#     assert f.exists
#     assert f.user == 'root'
#     assert f.group == 'root'

# def test_selinux_port_running_and_enabled(host):
#     centos = host.ports("80")
#     assert centos.is_running
#     assert centos.is_enabled
