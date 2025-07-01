# FabricaAD_backend
Avaliação de Desempenho de Colaboradores.

## Instruções de instalação e execução

O projeto usa [pdm](https://pdm-project.org/en/latest/) como gerenciador de pacotes, dependências e ambientes virtuais para Python.


### Instalação pdm:

Verifique se o pdm está instalado rodando o seguinte comando no terminal:

```bash
pdm -V
```

Se o pdm não estiver instalado o terminal retornará algo como:

```bash
command not found: pdm
```

Neste caso, instale a versão mais recente:

```bash
curl -sSLv https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python3 -
```

> IMPORTANTE: Após a instalação, feche o terminal (Ctrl + D) e abra um novo terminal (Ctrl + Alt + T)

Execute:

```bash
pdm -V
```

> IMPORTANTE: Se retornar algo como:

```bash
command not found: pdm
```

Adicione o executável ao seu PATH.

> NOTA: Caso tenha dificuldades com a configuração do pdm, consulte: [Instalação e configuração do PDM](https://github.com/marrcandre/django-drf-tutorial?tab=readme-ov-file#a3-instala%C3%A7%C3%A3o-e-configura%C3%A7%C3%A3o-do-pdm).

### Instruções de execução:
Instale as dependências com o seguinte comando:

```bash
pdm install
```

Para executar o projeto digite no terminal:

```bash
pdm run dev
```
