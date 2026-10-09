# Arquitetura de referência

Cenário de laboratório: sede, site remoto e workloads em nuvem conectados por roteamento e VPN IPsec.

```text
Site A / HQ --- WAN / Edge --- Site B / Remote
                    |
                 VPN IPsec
                    |
               Cloud VPC/VNet
```

## Princípios
- Segmentar usuários, serviços e gerenciamento.
- Usar endereçamento sumarizável e documentar gateways.
- Definir rotas alternativas, monitoramento e rollback.
- Restringir administração e registrar alterações.

## Checklist
- [ ] Requisitos e fluxos documentados.
- [ ] Plano IPv4/IPv6 e VLANs revisado.
- [ ] Rotas e firewall revisados.
- [ ] Métricas e alertas definidos.
- [ ] Testes de falha e rollback planejados.

Topologia e endereços são ilustrativos; use somente em laboratório.
