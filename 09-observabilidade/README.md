# Observabilidade de rede

## Sinais fundamentais
- Disponibilidade de interfaces, peers e túneis.
- Latência, jitter e perda de pacotes.
- Utilização, descartes e erros de interface.
- CPU, memória e temperatura quando disponíveis.
- Estado BGP/OSPF e mudanças de adjacência.
- DNS, DHCP e serviços críticos.

## Boas práticas de alertas
Todo alerta deve ter severidade, condição, duração, serviço impactado, runbook, equipe responsável e critério de recuperação. Evite alertas ruidosos sem contexto.

Defina SLOs conforme requisitos do serviço e capacidade real de medição; não use números arbitrários como compromisso contratual.
