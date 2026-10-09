# Networking

## Plano de endereçamento de laboratório

| Segmento | Rede | Uso |
|---|---|---|
| VLAN 10 | 10.10.10.0/24 | Usuários Site A |
| VLAN 20 | 10.10.20.0/24 | Usuários Site B |
| VLAN 30 | 10.10.30.0/24 | Gerenciamento |
| Loopbacks | 10.255.0.0/24 | Roteadores de teste |
| Ponto a ponto | 10.0.0.0/30 | Enlace de teste |

## Troubleshooting por camadas
1. Interface física, estado, erros e descartes.
2. VLAN access/trunk e tabela MAC.
3. Endereço, máscara, gateway e ARP/ND.
4. Rotas, próximo salto e rota de retorno.
5. ACL/firewall, DNS, MTU e portas de aplicação.

## Linux
```bash
ip -br address
ip route
ip neigh
ping -c 4 10.10.10.1
tracepath 10.10.20.10
ss -tulpn
resolvectl status
```

Não aplique comandos de alteração em produção sem autorização e plano de mudança.
