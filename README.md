# Projeto Prático - Cadastro de Clientes

## Descrição  
Este projeto é uma aplicação simples de cadastro de clientes, desenvolvida utilizando o **Streamlit**. A aplicação permite o cadastro de clientes, onde são armazenadas informações como o nome, data de nascimento e tipo de cliente em um arquivo CSV.

## Tecnologias Utilizadas  
- **Streamlit**: Framework para criação de aplicações web interativas em Python.  
- **Pandas**: Biblioteca para manipulação de dados, embora aqui seja usada apenas para leitura e escrita simples no CSV.  
- **Python**: Linguagem de programação utilizada no projeto.

## Instalação

### Pré-requisitos  
Antes de começar, certifique-se de ter os seguintes itens instalados:
- **Python 3.8+**: Certifique-se de que a versão do Python em seu sistema seja 3.8 ou superior.
- **Poetry** (opcional): Para gerenciar dependências, utilize o Poetry. Caso não tenha, instale o Poetry através deste link: https://python-poetry.org/docs/#installation.

### Passo 1: Clonar o Repositório  
Primeiro, clone o repositório para o seu ambiente local. Execute os seguintes comandos no seu terminal:

```
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### Passo 2: Instalar as Dependências  
Depois de clonar o repositório, instale as dependências do projeto. Se você está usando o **Poetry** para gerenciar as dependências, use o seguinte comando:

```
poetry install
```

Se não estiver usando o Poetry, você pode instalar as dependências manualmente com o `pip`, mas é recomendado usar o Poetry para manter a consistência do ambiente.

### Passo 3: Ativar o Ambiente Virtual  
Agora, ative o ambiente virtual. Se você estiver usando o **Poetry**, basta executar:

```
poetry shell
```

Isso ativará o ambiente virtual do Poetry. Se você estiver utilizando um ambiente virtual gerenciado pelo **venv** ou outro sistema, ative-o de acordo com o método adequado.

### Passo 4: Executar a Aplicação  
Agora, você pode executar a aplicação Streamlit com o seguinte comando:

```
streamlit run Cadastro.py
```

Abra o navegador e vá para a URL fornecida pelo Streamlit (geralmente **http://localhost:8501**).

## Como Usar

1. Preencha os campos no formulário de cadastro para adicionar um cliente. As informações serão salvas no arquivo **clientes.csv**.  
2. Após o cadastro, você pode verificar o arquivo **clientes.csv** para ver os dados registrados.

## Testes  
Este projeto não possui testes automatizados implementados. No entanto, você pode testar a aplicação manualmente ao preencher o formulário de cadastro e verificar se os dados são salvos corretamente no arquivo CSV.

## Contribuição

1. Faça um **fork** deste repositório.
2. Crie uma **branch** para suas alterações:
   ```
   git checkout -b minha-alteracao
   ```
3. **Commit** suas mudanças:
   ```
   git commit -am 'Adicionando nova funcionalidade'
   ```
4. **Push** para a sua branch:
   ```
   git push origin minha-alteracao
   ```
5. Envie uma **Pull Request** para este repositório.
