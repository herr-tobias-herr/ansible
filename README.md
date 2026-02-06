Ansible tutorial

ssh-copy-id q@192.168.1.2

execute playbook with: ansible-playbook --ask-become-pass playbook.yaml

commands
scp /file/to/send q@192.168.1.2:/where/to/put

OpenSSH
ssh-ed25519
ssh-rsa         Rivest-Shamir-Adleman

local                                               pi
ssh-keygen -t ed25519 -C „ansible“
ssh-copy-id -i ~/.ssh/ansible.pub q@192.168.1.1      -> id_e.pub 
ssh -i ~/.ssh/ansible q@192.168.1.1

ansible all --key-file ~/.ssh/ansible -i inventory -m ping
ansible all -m ping #with ansible.cfg
ansible all --list-hosts
ansible all -m gather_facts --limit q@192.168.1.1 | grep ansible_distribution
ansible all -m apt -a update_cache=true --become --ask-become-pass
ansible all -m apt -a name=vim-nox --become --ask-become-pass
ansible all -m apt -a "upgrade=dist" --become --ask-become-pass