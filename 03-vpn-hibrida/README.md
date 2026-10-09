# VPN e conectividade híbrida

## Checklist de VPN IPsec
- [ ] Redes locais/remotas sem sobreposição.
- [ ] Endpoints e parâmetros IKE/IPsec documentados.
- [ ] Segredos guardados fora do Git.
- [ ] ACLs limitadas aos prefixos necessários.
- [ ] Negociação IKE e SAs validadas.
- [ ] Rotas de ida e volta verificadas.
- [ ] MTU/MSS e NAT-T testados.
- [ ] Queda e recuperação do túnel simuladas.

## Diagnóstico
1. Alcance do peer e UDP 500/4500.
2. Compatibilidade de IKE, criptografia, integridade, DH/PFS e lifetimes.
3. Seletores/proxy IDs e rotas de retorno.
4. NAT, ACL e MTU.
5. Estado das SAs, contadores e logs.

Use somente endpoints e segredos fictícios em laboratórios.
