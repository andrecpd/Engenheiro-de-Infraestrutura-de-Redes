# Engenheiro de Infraestrutura de Redes

Portfólio prático de **NetOps, automação, redes corporativas, conectividade híbrida e observabilidade**, alinhado a uma atuação de engenharia de infraestrutura.

> **Objetivo:** demonstrar raciocínio técnico, documentação, automação segura e capacidade de troubleshooting por meio de laboratórios reproduzíveis. Os exemplos são de laboratório e não representam configurações de produção.

## Trilhas técnicas

- **Networking:** IPv4/IPv6, VLAN, roteamento, ACL, QoS, redundância e segmentação.
- **Automação:** Ansible, Python, inventário, templates, validação e idempotência.
- **VPN e WAN:** IPsec, túneis entre sites, monitoramento de enlaces e estratégias de failover.
- **Cloud híbrida:** AWS VPC, rotas, DNS/Route 53 e princípios equivalentes em Azure/GCP.
- **NetOps CI/CD:** Git, revisão de mudanças, lint, validação, aprovação e plano de rollback.
- **Observabilidade:** Zabbix, Prometheus, Grafana, logs, métricas e alertas.
- **Linux e containers:** troubleshooting de rede, DNS, rotas, sockets e fundamentos de rede Docker/Kubernetes.

## Estrutura do repositório

| Diretório | Conteúdo |
|---|---|
| `01-arquitetura` | topologias, requisitos, decisões e padrões |
| `02-networking` | endereçamento, VLANs, roteamento, ACL e QoS |
| `03-vpn-hibrida` | VPN IPsec, conectividade entre sites e cloud |
| `04-linux` | comandos e diagnóstico de rede em Linux |
| `05-ansible` | inventário, playbooks, roles e validação |
| `06-python` | scripts de automação e coleta |
| `07-netops-cicd` | pipeline de validação de mudanças |
| `08-cloud` | padrões de conectividade em nuvem |
| `09-observabilidade` | métricas, dashboards e alertas |
| `10-labs` | laboratórios guiados e critérios de aceite |
| `11-troubleshooting` | runbooks de incidentes |
| `12-entrevista` | perguntas técnicas e respostas estruturadas |
| `13-operacao-segura` | change management, backup e rollback |

## Roteiro sugerido

1. Leia a arquitetura e o plano de endereçamento.
2. Execute o LAB-01 em ambiente local ou virtual.
3. Valide os playbooks antes de qualquer alteração.
4. Simule falhas e registre evidências de troubleshooting.
5. Evolua o pipeline para incluir testes, aprovação e rollback documentado.

## Segurança operacional

- Use somente IPs, credenciais e dados fictícios nos exemplos.
- Não publique senhas, tokens, chaves privadas ou configurações sensíveis.
- Faça backup e revisão por pares antes de mudanças reais.
- Use modo de validação/check quando disponível e confirme o plano de rollback.
- Não aplique os exemplos diretamente em redes de produção.

## Como apresentar este portfólio

Para cada laboratório, documente **problema → desenho → implementação → validação → falhas simuladas → resultado → limitações**. Diferencie claramente os exercícios de laboratório da experiência profissional real.

## Próximos passos

Veja [os laboratórios](10-labs/README.md), [Ansible](05-ansible/README.md), [NetOps CI/CD](07-netops-cicd/README.md) e [preparação para entrevista](12-entrevista/README.md).
