# Runbooks de troubleshooting

## Sem conectividade entre redes
1. Confirmar interfaces, erros e estado físico.
2. Verificar IP/máscara, VLAN e gateway.
3. Consultar rotas nos dois sentidos.
4. Verificar ACL/firewall e logs.
5. Testar caminho com traceroute/tracepath.
6. Verificar MTU e portas da aplicação.
7. Comparar antes/depois e registrar causa-raiz.

## VPN estabelecida, tráfego não passa
- Conferir seletores e prefixos locais/remotos.
- Verificar rota de retorno e regras de firewall.
- Consultar contadores das SAs.
- Testar MTU/MSS e NAT.
- Capturar tráfego apenas com autorização.

## Lentidão intermitente
Correlacione latência, perda, jitter, utilização, erros, descartes, filas e mudanças recentes. Diferencie rede, DNS e aplicação.

## Registro de incidente
Data/hora · impacto · escopo · sintomas · hipótese · evidências · mitigação · causa-raiz · prevenção.
