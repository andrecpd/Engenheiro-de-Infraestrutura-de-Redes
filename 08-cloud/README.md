# Cloud e conectividade híbrida

## AWS VPC: pontos de verificação
- CIDRs sem sobreposição com on-premises e outras VPCs.
- Subnets públicas/privadas e tabelas de rotas explícitas.
- Security Groups e NACLs com menor privilégio.
- Route 53: hosted zones, registros e resolução híbrida.
- VPN Site-to-Site ou link dedicado conforme requisitos.
- Logs, métricas e alarmes de conectividade.

## Azure e GCP
Mapeie os mesmos conceitos: redes virtuais, subnets, rotas, firewalls, VPN/links dedicados, DNS e telemetria. Documente diferenças de produto e limites por provedor.

## Antes da mudança
- [ ] CIDRs e rotas de ida/volta revisados.
- [ ] Segurança revisada por fluxo.
- [ ] Impacto, janela, validação e rollback definidos.
- [ ] Custos recorrentes avaliados.
