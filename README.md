# nestSX
Deploy and configure a simple nested NSX lab over a single ESXi host managed by a(n infra) vCenter

from an ubuntu distribution, here are the required components:

sudo apt install python3-pip

sudo apt install git

sudo apt install python3-pyvmomi

sudo apt install software-properties-common

sudo apt-add-repository ppa:ansible/ansible // not necessarily the best option

sudo apt update

sudo apt install ansible

sudo ansible-galaxy collection install git+https://github.com/vmware/ansible-for-nsxt
