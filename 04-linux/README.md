# Linux para infraestrutura de redes

## Coleta inicial
```bash
hostnamectl
ip -br link
ip -br address
ip route
ip rule
ip neigh
ss -s
ss -tulpn
resolvectl status
```

## Perguntas de diagnóstico
- A interface está UP e sem erros?
- Endereço, gateway e rota default estão corretos?
- O próximo salto resolve por ARP/ND?
- DNS resolve o nome esperado?
- A aplicação escuta na porta correta?
- Há bloqueio de firewall ou ACL?
- O MTU é consistente no caminho?

Registre horário, host, comando, evidência, hipótese e resultado. Remova dados sensíveis antes de publicar.
