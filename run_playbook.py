import subprocess
import os

# Config
config_path = os.path.join("general", "ansible.cfg")
playbook_path = os.path.join("general", "node.yaml")
inventory_path = os.path.join("general", "inventory.yaml")
target_group = "master"  # or "master", or passed from CLI args

# Environment
env = os.environ.copy()
env["ANSIBLE_CONFIG"] = config_path

# Run Ansible Playbook with inventory and limit
process = subprocess.Popen(
    [
        "ansible-playbook",
        "-i", inventory_path,
        "-l", target_group,
        playbook_path
    ],
    env=env
)

process.communicate()
print("Return Code:", process.returncode)