# Cistercian Numerals Drawer and Reader

Este projeto é uma ferramenta para desenhar e interpretar números cistercienses. Ele inclui dois módulos principais:

- **cisterciense_drawer.py**: Gera imagens de números cistercienses.
- **cisterciense_reader.py**: Lê e interpreta números cistercienses a partir de imagens.

## Estrutura do Projeto

- `cisterciense_drawer.py`: Script para desenhar números cistercienses.
- `cisterciense_reader.py`: Script para leitura de números cistercienses.
- `main.py`: Ponto de entrada principal para executar o programa.
- `Números cistercienses.pdf`: Documento de referência sobre números cistercienses.
- `requirements.txt`: Lista de dependências do projeto.
- `output/`: Pasta onde as saídas geradas pelo programa são armazenadas.

## Pré-requisitos

Certifique-se de ter o Python 3.13 ou superior instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/).

## Instalação

1. Clone este repositório ou baixe os arquivos.
2. Navegue até o diretório do projeto no terminal.
3. Instale as dependências necessárias executando:

   ```bash
   pip install -r requirements.txt
   ```

## Como Usar

### Executar o Programa Principal

Para rodar o programa principal, execute o arquivo `main.py`:

```bash
python main.py
```

### Gerar Números Cistercienses

Para gerar uma imagem de um número cisterciense, use o script `cisterciense_drawer.py`. Por exemplo:

```bash
python cisterciense_drawer.py 4523
```

Isso gerará uma imagem chamada `4523_cisterciense.png` na pasta `output/`.

### Ler Números Cistercienses

Para interpretar um número cisterciense a partir de uma imagem, use o script `cisterciense_reader.py`. Por exemplo:

```bash
python cisterciense_reader.py output/4523_cisterciense.png
```

O programa exibirá o número correspondente no terminal.

## Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.