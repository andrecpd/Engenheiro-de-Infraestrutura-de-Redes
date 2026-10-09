# LAB-01 — Primeiros passos com Ansible

## Objetivo
Executar coleta de facts em localhost sem modificar configurações de rede.

## Execução na raiz do repositório
```bash
ansible-inventory -i 05-ansible/inventory/lab.yml --list
ansible-playbook -i 05-ansible/inventory/lab.yml 05-ansible/playbooks/collect.yml --syntax-check
ansible-playbook -i 05-ansible/inventory/lab.yml 05-ansible/playbooks/collect.yml
```

## Resultado esperado
O playbook coleta facts de localhost e mostra nome do host, família do sistema operacional e versão do Python.

## Desafio
Adicione uma tarefa que mostre distribuição e versão do sistema. Não colete nem imprima credenciais.

## Critério de conclusão
Inventário válido, syntax-check sem erro, execução bem-sucedida e evidência documentada.
