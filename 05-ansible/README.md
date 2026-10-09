# Ansible para NetOps

Este módulo começa com coleta de facts em localhost, sem modificar a rede.

## Instalação em ambiente virtual
```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install ansible-core
ansible --version
```

## Validar e executar
```bash
ansible-inventory -i 05-ansible/inventory/lab.yml --list
ansible-playbook -i 05-ansible/inventory/lab.yml 05-ansible/playbooks/collect.yml --syntax-check
ansible-playbook -i 05-ansible/inventory/lab.yml 05-ansible/playbooks/collect.yml --check --diff
```

Para equipamentos de rede, confirme suporte de conexão/módulos do fabricante, use Ansible Vault para segredos e teste primeiro em equipamento virtual.
