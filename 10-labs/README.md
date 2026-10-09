# Laboratórios

Execute em EVE-NG, GNS3, containers ou VMs de teste. Adapte comandos e módulos às imagens disponíveis.

## LAB-01 — Inventário e coleta com Ansible
1. Instale Ansible Core em ambiente isolado.
2. Valide o inventário `05-ansible/inventory/lab.yml`.
3. Execute o syntax-check e o playbook.
4. Registre a saída e observações.

**Aceite:** inventário válido, playbook sem erro e facts do host exibidos.

## LAB-02 — Plano de endereçamento
Execute `python 06-python/validate_prefixes.py`, identifique a sobreposição intencional e corrija a lista.

**Aceite:** a sobreposição é detectada inicialmente e deixa de aparecer após a correção.

## LAB-03 — VPN IPsec entre sites
Desenhe e valide um túnel em simulador. Documente rotas, estado das SAs, conectividade, falha e recuperação. Não inclua segredos.

## LAB-04 — Pipeline NetOps
Abra um pull request e confira o workflow GitHub Actions. O pipeline valida código, mas não aplica mudanças em equipamentos.

## LAB-05 — Troubleshooting
Simule falha de rota, DNS, MTU ou porta. Registre sintoma, hipótese, comandos, causa-raiz, correção e prevenção.

## Modelo de relatório
Cenário e objetivo · topologia e versões · pré-requisitos · procedimento · saída esperada · testes negativos · evidências · limitações · rollback.
