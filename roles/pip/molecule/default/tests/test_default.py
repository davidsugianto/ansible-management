import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


# def test_python_installed(host):
#     python = host.package("pip")
#     assert python.is_installed

# def test_pip_installed(host):
#     pip = host.package("pip")
#     assert pip.is_installed

# def test_numpy_installed(host):
#     numpy = host.pip("numpy")
#     assert numpy.is_installed
