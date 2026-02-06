# Ansible Tutorial

This repository demonstrates basic usage of **Ansible** with SSH key authentication to manage remote hosts without entering passwords each time.

---

## **1. SSH Key Setup**

To allow Ansible to connect to remote hosts securely, create an SSH key and copy it to the remote host.

### Generate a new SSH key

```bash
# Generate an ED25519 key for Ansible
ssh-keygen -t ed25519 -C "ansible"
```

* Default location: `~/.ssh/id_ed25519` (you can name it `ansible` if you want: `~/.ssh/ansible`)

### Copy the key to the remote host

```bash
ssh-copy-id -i ~/.ssh/ansible.pub q@192.168.1.1
```

* This adds your public key to the remote host's `~/.ssh/authorized_keys`
* Test access:

```bash
ssh -i ~/.ssh/ansible q@192.168.1.1
```

Now you can connect **without a password**, which is required for Ansible automation.

---

## **2. Basic SSH Commands**

```bash
# Securely copy a file to a remote host
scp /path/to/local/file q@192.168.1.2:/remote/path

# Connect to a remote host
ssh q@192.168.1.1
```

Supported key types:

* `ssh-ed25519`
* `ssh-rsa` (Rivest-Shamir-Adleman)

---

## **3. Configure Ansible for Remote Hosts**

Once your SSH key is on the remote host, test connection using Ansible:

```bash
# Using a specific key file
ansible all --key-file ~/.ssh/ansible -i inventory -m ping

# If configured in ansible.cfg
ansible all -m ping
```

Other useful commands:

```bash
# List all hosts
ansible all --list-hosts

# Gather facts from a specific host
ansible all -m gather_facts --limit q@192.168.1.1 | grep ansible_distribution

# Update package cache on all hosts (requires become)
ansible all -m apt -a update_cache=true --become --ask-become-pass

# Install a package
ansible all -m apt -a "name=vim-nox" --become --ask-become-pass

# Upgrade system packages
ansible all -m apt -a "upgrade=dist" --become --ask-become-pass
```

---

## **4. Running Playbooks**

### Using Python script

```bash
python3 ./run_playbook.py
```

### Using native Ansible command

```bash
ansible-playbook --ask-become-pass playbook.yaml
```

---

## **5. Notes**

* Ensure your `inventory` file contains the target hosts.
* `ansible.cfg` can simplify commands by setting default SSH key and user.
* Using SSH keys allows passwordless access, which is essential for automated playbooks.

---

This setup allows you to manage remote hosts via Ansible efficiently and securely.
