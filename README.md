# Visualização de Dados: Análise do Desempenho Escolar dos Alunos

**Autores:** Beatriz Martins e Laura Barreto  
**Unidade Curricular:** Visualização de Dados (Licenciatura em Engenharia e Ciência de Dados - Universidade de Coimbra)

## Resumo do Projeto
Este projeto tem como objetivo explorar e compreender as relações entre fatores socioeconómicos, comportamentais e escolares que influenciam o sucesso académico de alunos portugueses nas disciplinas de **Matemática** e **Português**. 

Através da criação de visualizações de dados originais, interativas e bem fundamentadas em boas práticas de design, procurámos responder a várias questões analíticas e extrair padrões que muitas vezes passam despercebidos numa análise de dados tabular tradicional.

---

## Principais Descobertas e Visualizações
O código desenvolvido analisa e gera gráficos que suportam as seguintes conclusões-chave:

1. **Relações de Correlação (Heatmap e Regressão Linear):**
   * Verificámos o peso de várias features (ex: tempo de estudo, apoio familiar, saúde) na nota final (G3). Fatores como o tempo de estudo e apoio educativo têm correlações positivas, enquanto as saídas e reprovações passadas afetam negativamente as notas.
2. **Faltas vs. Vida Pessoal (Barras Empilhadas):**
   * Alunos com um elevado número de faltas (mais de 10) tendem a estar envolvidos em relações amorosas (*romantic*) e a apresentar uma maior frequência de saídas com amigos (*goout*).
3. **Impacto das Explicações e Internet (Sunburst interativo):**
   * Analisámos como ter aulas de apoio (explicações) e acesso à Internet afeta a nota de Matemática. Alunos com ambos os recursos tendem a alcançar resultados ligeiramente mais sólidos.
4. **Profissão dos Pais (Funnel Chart):**
   * Verificámos se filhos de professores têm melhores resultados académicos. Existe uma ligeira vantagem, mas não é o fator mais determinante para o sucesso.
5. **Tempo de Estudo, Tempo Livre e Reprovações (Gráfico de Bolhas/Wedges Customizado):**
   * Alunos que dedicam mais tempo ao estudo apresentam, naturalmente, uma menor taxa de reprovações e reportam ter menos tempo livre para outras atividades.
6. **Comparação Matemática vs. Português (Gráfico de Barras Divergentes):**
   * Confirmámos que a distribuição de notas em Português é geralmente superior (mais razoável e centralizada) do que em Matemática, disciplina onde se nota uma maior dificuldade geral.
7. **Idade e Distância da Escola (Boxplot e Scatter):**
   * Alunos mais velhos ou que demoram mais tempo no percurso casa-escola (> 1 hora) tendem a obter notas intermédias a baixas.
8. **Atividades Extracurriculares por Género (Donut Charts):**
   * O envolvimento em atividades extracurriculares mostrou ter uma influência mais positiva no desempenho escolar das raparigas, contrastando com o impacto neutro/negativo nos rapazes.

---

## Estrutura de Ficheiros

* **Código e Visualizações:** O ficheiro principal de Python contém o pré-processamento (limpeza de dados, uso de `LabelEncoder`) e o código para geração dos vários gráficos estáticos e interativos.
* **Dados (`.csv`):**
  * `student_data.csv` e `mat2.csv`: Dados demográficos e escolares relativos à disciplina de Matemática.
  * `por2.csv`: Dados relativos à disciplina de Português.
* **Documentação (`.pdf`):** Relatório detalhado com a justificação de design escolhido para as visualizações, tratamento de limitações de dados e reflexão sobre os resultados.

---

## Como Executar

1. **Pré-requisitos:** Ter o Python instalado juntamente com as bibliotecas necessárias. Pode instalá-las correndo:
   ```bash
   pip install pandas numpy matplotlib seaborn plotly scikit-learn
