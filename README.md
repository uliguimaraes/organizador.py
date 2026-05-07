# Organizador de Arquivos em Python

> Um assistente de pastas que transforma uma área de downloads bagunçada em uma estrutura organizada por tipo de arquivo.

## Visão geral

O **organizador.py** é um script em Python que percorre um diretório-alvo, identifica a extensão de cada arquivo e move automaticamente os itens para pastas como `Imagens`, `Documentos` e `Videos`. Ele usa módulos da biblioteca padrão, como `os` e `shutil`, para navegar pelo sistema de arquivos e mover arquivos com segurança.[1] [2]

| Categoria | Extensões reconhecidas |
|---|---|
| Imagens | `.jpg`, `.jpeg`, `.png`, `.gif` |
| Documentos | `.pdf`, `.docx`, `.txt`, `.xlsx` |
| Vídeos | `.mp4`, `.mov`, `.avi` |

## Como funciona

O script verifica se o diretório configurado existe, ignora subpastas e analisa somente arquivos. Quando encontra uma extensão mapeada, cria a pasta de destino, caso ela ainda não exista, e move o arquivo para a categoria correspondente.

```text
Downloads
   ├── foto.png      → Imagens
   ├── contrato.pdf  → Documentos
   └── video.mp4     → Videos
```

## Antes de executar

Abra o arquivo `organizador.py` e ajuste a constante `DIRETORIO_ALVO` para o caminho da pasta que você deseja organizar.

```python
DIRETORIO_ALVO = r"C:\Users\SeuUsuario\Downloads"
```

## Como executar

```bash
git clone https://github.com/uliguimaraes/organizador.py.git
cd organizador.py
python organizador.py
```

## Ideias para evolução

O projeto pode receber novas categorias, modo de simulação antes de mover os arquivos, logs em arquivo `.txt`, suporte a argumentos de linha de comando e tratamento para nomes duplicados.

## Referências

[1]: https://docs.python.org/3/library/os.html "Python os module"
[2]: https://docs.python.org/3/library/shutil.html "Python shutil module"
