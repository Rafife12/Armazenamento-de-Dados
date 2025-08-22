# Associação de Tipos de Dados a Sistemas de Armazenamento

## Descrição
Este projeto tem como objetivo associar diferentes tipos de dados ao sistema de armazenamento mais apropriado, garantindo eficiência e organização.  

O programa recebe como entrada o tipo de dado e retorna o local ideal de armazenamento.

## Tipos de Dados Suportados
- Imagem → Blob Storage
- Transações Bancárias → Banco de Dados Relacional
- Logs de Servidor → Data Lake
- Documentos Word → SharePoint

## Como usar
1. Abra o terminal na pasta do projeto.
2. Execute o comando:
```bash
python main.py
```
3. Digite o tipo de dado exatamente como listado acima.
4. O programa retornará o local ideal de armazenamento.
