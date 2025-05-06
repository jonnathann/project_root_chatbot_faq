# 📊 Análise Exploratória

Este documento apresenta um resumo da análise exploratória realizada sobre o conjunto de dados utilizado para treinar modelos de Machine Learning voltados à construção de um chatbot de perguntas e respostas.

## ✅ Informações Gerais

- **Número total de observações**: 10.000
- **Número de colunas**: 3
  - `pergunta` (texto)
  - `categoria` (classe da pergunta)
  - `resposta` (texto)
- **Número de categorias distintas**: 9

## 🔍 Verificações Realizadas

- ✅ Verificação da **dimensão** do dataset  
- ✅ Verificação da **existência de valores nulos**  
- ✅ Cálculo da **quantidade média de caracteres** por coluna (`pergunta`, `categoria`, `resposta`)  
- ✅ Verificação da **distribuição das categorias**  
- ✅ Análise do **balanceamento das classes**  

## 📈 Distribuição das Categorias

O gráfico gerado mostra a quantidade de exemplos por classe, evidenciando uma distribuição relativamente balanceada entre as 9 categorias. Nenhuma categoria apresentou desbalanceamento severo.

## 🧹 Limpeza e Preparação

- Não foram encontrados valores ausentes nas colunas.
- Os textos estão normalizados (sem necessidade de tratamento adicional nesta fase).

---

Esta análise é o primeiro passo do projeto, ajudando a entender a estrutura dos dados antes de aplicarmos os algoritmos de aprendizado supervisionado.
