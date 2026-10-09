# NetOps CI/CD

## Fluxo recomendado
1. Abrir branch para a mudança.
2. Revisar diff por pares.
3. Executar lint e testes de sintaxe.
4. Validar templates, inventário e variáveis.
5. Exigir aprovação antes de qualquer aplicação.
6. Aplicar em laboratório/canário e verificar estado.
7. Executar rollback documentado se o aceite falhar.

O workflow inicial deste repositório faz validações estáticas. Ele não acessa equipamentos nem aplica configurações.
