## --- IMPORT DAS BIBLIOTECAS NECESSÁRIAS --- ##
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import matplotlib.patches as mpatches
from sklearn.linear_model import LinearRegression

## --- LEITURA DOS CSV's COM OS DADOS --- ##
# Leitura dos dados do dataset student_data
df_student_data = pd.read_csv ('student_data.csv', delimiter = ',')

# Leitura dos dados do dataset da disciplina de Português
df_pt = pd.read_csv ('por2.csv', delimiter = ",")

# Leitura dos dados do dataset da disciplina de Matemática
df_mat = pd.read_csv ('mat2.csv', delimiter = ",")

# Juntar os dados do df_mat e df_por
df_todos = pd.concat ([df_pt, df_mat], ignore_index = True)

# Verificar valores em falta em cada df
valores_falta_pt = df_pt.isnull().sum()
print (valores_falta_pt)
print ()

valores_falta_mat = df_mat.isnull().sum()
print (valores_falta_mat)
print ()

# Copiar os dataframes para depois passar para numéricos
df_mat_le = df_mat.copy ()
df_pt_le = df_pt.copy ()
df_todos_le = df_todos.copy()
df_students_le = df_student_data.copy()

# Remover coluna "ID" de dados_mat
df_mat_sem_id = df_mat.drop(columns = "ID")

# Comparar se todos os elementos dos dois dataframes são iguais 
if df_mat_sem_id.equals(df_student_data):
    print("Iguais")
else:
    print("Não são iguais")

# Resultado: são iguais, logo usamos apenas mat2.csv
                
# Converter todas para numéricas com LabelEncoder
cols = ['sex', 'address', 'famsize', 'Mjob', 'Fjob', 'reason', 
        'guardian', 'schoolsup', 'famsup', 'paid', 'activities',
        'nursery', 'higher', 'internet', 'romantic', 'Pstatus']

dfs = [df_mat_le, df_pt_le, df_todos_le]

# Para cada feature nos dataframes, usar o LabelEncoder para mudar para numérica
for coluna in cols:
    for df in dfs: 
        le = LabelEncoder()
        df[coluna] = le.fit_transform(df[coluna])

# Mapear as variáveis
variaveis = {
    "sex": "sexo",
    "age": "idade",
    "address": "morada",
    "famsize": "tam_família",
    "Pstatus": "pais_casados",
    "Medu": "escolaridade_mãe",
    "Fedu": "escolaridade_pai",
    "Mjob": "trabalho_mãe",
    "Fjob": "trabalho_pai",
    "reason": "escolha_escola",
    "guardian": "enc_educação",
    "traveltime": "tempo_casa_escola",
    "studytime": "tempo_estudo",
    "failures": "n_reprovações",
    "schoolsup": "apoio_escola",
    "famsup": "apoio_família",
    "paid": "explicações",
    "activities": "atividades_extra",
    "nursery": "frequentou_creche",
    "higher": "ensino_superior",
    "internet": "tem_internet",
    "romantic": "namora",
    "famrel": "relação_familiar",
    "freetime": "tempo_livre",
    "goout": "freq_saídas",
    "Dalc": "álcool_semana",
    "Walc": "álcool_f.semana",
    "health": "saúde",
    "absences": "faltas",
    "G1": "nota_Período_1",
    "G2": "nota_Período_2",
    "G3": "nota_Período_3"
} 

df_vars = df_todos_le.rename(columns = variaveis)


## -- HEATMAP DAS CORRELAÇÕES ENTRE VARIÁVEIS -- ##
corr_todos = df_vars.corr(numeric_only = True)
plt.figure(figsize = (12,6)) 
sns.heatmap(
    corr_todos,
    annot = True, # Mostra os valores numéricos
    fmt = ".1f", # Arredonda para 2 casas decimais
    cmap = "coolwarm",
    square = True,
    annot_kws = {"size": 6}, # Tamanho da fonte dos números
    yticklabels = True

)
plt.xticks(rotation = 50, ha = "right", fontsize = 8)
plt.yticks(rotation = 0, ha = "right", fontsize = 8)
plt.title("Relações entre os Vários Fatores de Desempenho Escolar", fontsize = 18, fontweight = "bold", 
          pad = 15, fontname = "Tahoma", color = "#252B9F")
plt.show()


## -- GRÁFICO DE BARRAS - CORRELAÇÕES COM G3 -- ##
# Ordenar correlações com G3
corr_with_G3 = corr_todos["nota_Período_3"].drop("nota_Período_3").sort_values(ascending = False)

# Separar índices de barras positivas e negativas
negativas = sum(corr_with_G3 < 0) 

# Criar figura
plt.figure(figsize = (12,6))
plt.bar(corr_with_G3.index, corr_with_G3.values, color = "#E7CEFFFF", 
        edgecolor = "black", linewidth = 0.5,  zorder = 2)

# Linha preta em y = 0
plt.axhline(0, color = 'black', linewidth = 0.8, linestyle = '-', zorder = 3)

# Linha vertical separando positivas e negativas
plt.axvline(x = negativas - 0.5, color = '#9F9F9F', linewidth = 1.2, zorder = 4)

# Grelha suave atrás das barras
plt.grid(True, axis = 'y', linestyle = '--', alpha = 0.7, zorder = 0)
plt.title("Fatores que influenciam a Nota Final (G3)", fontsize = 20, pad = 15, 
          fontweight = "bold", fontname = "Tahoma", color = "#966FC1")

plt.text(
    x = 3,      
    y = 0.55,       
    s = "Fatores com relação positiva\n         com a nota final",
    fontsize = 14,
    fontweight = 'bold',
    color = "#005AA4", 
    fontname = "Tahoma",
    bbox = dict(
        facecolor = "#FFFFFF", 
        edgecolor = "#000000", 
        boxstyle = "round,pad=0.5" 
    )

)

plt.text(
    x = 19,      
    y = -0.45,       
    s = "Fatores com relação negativa\n         com a nota final",
    fontsize = 14,
    fontweight = 'bold',
    color = '#005AA4', 
    fontname = "Tahoma",
    bbox = dict(
        facecolor = "#FFFFFF", 
        edgecolor = "#000000", 
        boxstyle = "round,pad=0.5" 
    )

)

plt.ylabel("Peso da Relação", fontsize = 14)
plt.xticks(rotation = 45, ha = 'right', fontsize = 12)
plt.yticks(fontsize = 12)
plt.ylim (-1,1)
plt.tight_layout()
plt.show()


## -- REGRESSÃO LINEAR PARA VER BETAS MAIORES NUMA PIRAMIDE -- ##
# Selecionar apenas as colunas numéricas (já codificadas) e remover G1 e G2 
df_model = df_vars.drop(columns = ['nota_Período_1', 'nota_Período_2'])

# Separar variáveis independentes e dependente
X = df_model.drop(columns = ['nota_Período_3'])
X_numeric = X.select_dtypes(include = [np.number])
y = df_model['nota_Período_3']

# Ajustar regressão linear
reg = LinearRegression()
reg.fit(X_numeric, y)

# Extrair betas e variáveis
betas = pd.Series(reg.coef_, index = X_numeric.columns)

# Top 11 betas em módulo
top_betas = betas.abs().sort_values(ascending = False).head(11)
top_betas = betas.reindex(top_betas.index) # Manter sinais originais

# Gráfico em Pirâmide 
plt.figure(figsize = (8,6))
bars = plt.barh(top_betas.index, top_betas.values, color = '#E7CEFFFF', edgecolor = "black", linewidth = 0.3, zorder = 3)
plt.xlabel("Peso do Fator", fontsize = 14)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.grid(linestyle = "--", zorder = 0)
plt.axvline(0, color = "#9F9F9F", linewidth = 1.4, zorder = 3)
plt.title("Fatores que influenciam a Nota Final G3 (Regressão Linear)", fontsize = 20, pad = 15, 
          fontweight = "bold", fontname = "Tahoma", color = "#966FC1")

for bar in bars:
    width = bar.get_width()
    y = bar.get_y() + bar.get_height()/2

    plt.text(
        width/2, # Posição horizontal: meio da barra
        y,
        f'{width:.2f}',
        ha = 'center',           
        va = 'center',
        color = 'black',         
        fontsize = 11,
        fontweight = 'bold'
    )

ax = plt.gca()
ax_height = ax.get_ylim()[0] # Limite inferior
plt.text(
    x = -1.75,
    y = 7, # Metade do eixo    
    s = "     A Regressão Linear calcula os\n       pesos de cada fator. Quanto\n   maior o peso em módulo, maior a\n    influência do fator na nota final.",
    fontsize = 12,
    fontweight = 'bold',
    color = "#005AA4", 
    fontname = "Tahoma",
    bbox = dict(
        facecolor = "#FFFFFF", 
        edgecolor = "#000000", 
        boxstyle = "round,pad=0.5" 
    )

)

# Inverter eixo y para pirâmide (maior impacto no topo)
plt.gca().invert_yaxis()
plt.show()


## -- RELAÇÃO ENTRE O NÚMERO DE FALTAS, RELAÇÕES ROMÂNTICAS E SAÍDAS COM AMIGOS -- ##
# Criar bins
bins = [10, 20, 76] 

# Definir labels
faltas = ["10 a 20 faltas", "20 a 75 faltas"] 

# Dividimos as faltas por classes
faltas_categorias = pd.cut(df_todos_le['absences'], bins = bins, labels = faltas, include_lowest = True)

# Selecionar apenas os alunos com mais de 10 faltas
alunos_faltas = df_todos_le[(df_todos_le['absences'] >= 10)]

# Função para contar valores em classes específicas
def contar_classes(df, var):
    categorias = ["10 a 20 faltas", "20 a 75 faltas"]
    
    if len(df[var].unique()) == 2:
        classe_0 = df[var].eq(0).groupby(faltas_categorias, observed = False).sum().reindex(categorias, fill_value = 0)
        classe_1 = df[var].eq(1).groupby(faltas_categorias, observed = False).sum().reindex(categorias, fill_value = 0)
        return classe_0, classe_1
    
    elif len(df[var].unique()) > 3:
        classe_1 = df[var].eq(1).groupby(faltas_categorias, observed = False).sum().reindex(categorias, fill_value = 0)
        classe_2 = df[var].eq(2).groupby(faltas_categorias, observed = False).sum().reindex(categorias, fill_value = 0)
        classe_3 = df[var].eq(3).groupby(faltas_categorias, observed = False).sum().reindex(categorias, fill_value = 0)
        classe_4 = df[var].eq(4).groupby(faltas_categorias, observed = False).sum().reindex(categorias, fill_value = 0)
        classe_5 = df[var].eq(5).groupby(faltas_categorias, observed = False).sum().reindex(categorias, fill_value = 0)
        return classe_1, classe_2, classe_3, classe_4, classe_5

# Função para empilhar barras
def label_barras_empilhadas(ax, x_positions, listas_valores, nomes):

    for xs, valores, nome in zip(x_positions, listas_valores, nomes):
        soma = np.sum(valores, axis = 0)

        for x, y in zip(xs, soma):
            ax.text(x, y + 1.5, nome, ha = "center", va = "bottom", fontsize = 11)

# Contagens por classes
romantic_0, romantic_1 = contar_classes(alunos_faltas, 'romantic')
goout_1, goout_2, goout_3, goout_4, goout_5 = contar_classes(alunos_faltas, 'goout')

# Eixo X
x = np.arange(len(faltas))
largura = 0.25

fig, ax = plt.subplots(figsize = (12,7))

# Romantic empilhado
ax.bar(x - largura/2, romantic_0, width = largura, color = "#FFC8EA", label = "Not Romantic", zorder = 2, edgecolor = "#000000", linewidth = 0.3)
ax.bar(x - largura/2, romantic_1, width = largura, bottom = romantic_0, color = "#FE97D6", label = "Romantic", zorder = 2, edgecolor = "#000000", linewidth = 0.3)

# GoOut empilhado
ax.bar(x + largura/2, goout_1, width = largura, color = "#E1D9FD", label = "Quase nunca sai", zorder = 2, edgecolor = "#000000", linewidth = 0.3)
ax.bar(x + largura/2, goout_2, width = largura, bottom = goout_1, color = "#D4C9FE", label = "Sai Pouco", zorder = 2, edgecolor = "#000000", linewidth = 0.3)
ax.bar(x + largura/2, goout_3, width = largura, bottom = goout_1 + goout_2, color = "#C6B8FB", label = "Sai às Vezes", zorder = 2, edgecolor = "#000000", linewidth = 0.3)
ax.bar(x + largura/2, goout_4, width = largura, bottom = goout_1 + goout_2 + goout_3, color = "#BDACFB", label = "Sai Frequentemente", zorder = 2, edgecolor = "#000000", linewidth = 0.3)
ax.bar(x + largura/2, goout_5, width = largura, bottom = goout_1 + goout_2 + goout_3 + goout_4, color = "#B39FFC", label = "Sai Muito", zorder = 2, edgecolor = "#000000", linewidth = 0.3)

# Alturas totais das barras para cada variável
romantic_total = romantic_0 + romantic_1
age_total = goout_1 + goout_2 + goout_3 + goout_4 + goout_5

# Posições x de cada barra
x_romantic = x - largura/2
x_age = x + largura/2

# Criar rótulos
label_barras_empilhadas(ax, x_positions = [x_romantic, x_age],
                        listas_valores = [[romantic_0, romantic_1],[goout_1, goout_2, goout_3, goout_4, goout_5]],
                        nomes = ["Namoro", "Saídas"]
)

plt.xlabel ('Intervalos de faltas', fontsize = 16)
plt.ylabel ('Número de alunos', fontsize = 16)
ax.set_xticks(x)
ax.set_xticklabels(faltas, fontsize = 14)
plt.title ('Influência que as Relações Amorosas e a Frequência de Saídas dos Alunos têm na Quantidade de Faltas', fontsize = 18.5, 
           fontweight = "bold", pad = 15, fontname = "Tahoma", color = "#966FC1", loc = "center")

# Definir legenda
leg = plt.legend(loc = 'upper right', title = "Legenda:", fontsize = 10)
leg.get_title().set_fontweight('bold')
plt.tight_layout()

# Meter a grelha por trás do gráfico
plt.grid(zorder = 0)
plt.show()


## --- SUNBURST - INFLUÊNCIA DAS EXPLICAÇÕES NO DESEMPENHO DO ALUNO EM MATEMÁTICA --- ##
# Criar nova coluna 'explicações' no df_mat
df_mat['explicações'] = df_mat.apply(lambda row: 'Com Explicações' if (row['paid'] == 'yes') else 'Sem Explicações',
    axis = 1
)
# Criar bins
bins = [0,5,10,14,18,21]

# Criar labels
labels = ["0 a 4 - Mt. Insuf.", "5 a 9 - Insuf.", "10 a 13 - Suf.", "14 a 17 - Bom", "18 a 20 - Mt. Bom"]

# Ordem em que as notas aparecem
ordem_notas = {
    "0 a 4 - Mt. Insuf.": 0,
    "5 a 9 - Insuf.": 1,
    "10 a 13 - Suf.": 2,
    "14 a 17 - Bom": 3,
    "18 a 20 - Mt. Bom": 4
}

# Dividir as notas por bins
df_mat['nota_cat'] = pd.cut(df_mat['G3'], bins = bins, labels = labels, include_lowest = True).astype(str).str.strip()
# Mapear os alunos com e sem internet
df_mat['internet_cat'] = df_mat['internet'].map({'no':'Sem Internet', 'yes':'Com Internet'})
# Colocar as notas por ordem
df_mat["nota_order"] = df_mat["nota_cat"].map(ordem_notas)

# Coluna só com rótulos resumidos para mostrar dentro das fatias
df_mat['nota_label_curta'] = df_mat['nota_cat'].replace({
    "0 a 4 - Mt. Insuf.": "Mt. Insuf.",
    "5 a 9 - Insuf.": "Insuf.",
    "10 a 13 - Suf.": "Suf.",
    "14 a 17 - Bom": "Bom",
    "18 a 20 - Mt. Bom": "Mt. Bom"
})

# Criar Sunburst para cada grupo (apenas para gerar GO traces)
df_com = df_mat[df_mat['explicações'] == "Com Explicações"]
df_sem = df_mat[df_mat['explicações'] == "Sem Explicações"]

# Criar coluna count para calcular percentagens
df_com["count"] = 1
df_sem["count"] = 1

# Cores para cada nota
nota_colors = {
        "0 a 4 - Mt. Insuf.": "#FE7272",
        "5 a 9 - Insuf.": "#FEA7A7",
        "10 a 13 - Suf.": "#FFF29F",
        "14 a 17 - Bom": "#CEE9FF",
        "18 a 20 - Mt. Bom": "#81C6FF"
}

# Cores para as pessoas que têm Internet e não têm
internet_colors = {
    "Com Internet": "#F0DFFF",
    "Sem Internet": "#D3A5FE"
}

#  Função para criar sunburst mantendo ordem 
def criar_sunburst(df):
    # Sort por nota_order antes para manter a ordem correta
    df_sorted = df.sort_values('nota_order')
    print(len(df_sorted))
    return px.sunburst(
        df_sorted,
        path = ['nota_cat','internet_cat'],
        color = 'nota_cat',
        color_discrete_map = nota_colors,
        maxdepth = 2,
        hover_data = ['count'],                  
        custom_data = ['nota_label_curta'] # Passa rótulo curto para usar no texttemplate
    )

# Criar Sunbursts 
fig_com_px = criar_sunburst(df_com)
fig_sem_px = criar_sunburst(df_sem)

# Subplots 
fig = make_subplots(
    rows = 1, cols = 2, specs = [[{'type':'domain'}, {'type':'domain'}]],
    subplot_titles = ['181 Alunos com explicações', '214 Alunos sem explicações']
)
# Atualizar o layout
for i, ann in enumerate(fig['layout']['annotations']):
    ann['font'] = dict(family = "Tahoma", size = 20, color = "#000000", weight = 'bold') # Fonte, cor e tamanho
    ann['text'] = f"<b>{ann['text']}</b>" # Negrito
    ann['y'] -= 0.02

# Adicionar os traces aos sunbursts
for trace in fig_com_px.data:
    fig.add_trace(trace, row = 1, col = 1)
for trace in fig_sem_px.data:
    fig.add_trace(trace, row = 1, col = 2)

# Corrigir cores da camada externa (internet) 
for tr in fig.data:
    if tr.type == 'sunburst':
        new_colors = []
        for label, parent in zip(tr.labels, tr.parents):
            if label in internet_colors:
                new_colors.append(internet_colors[label])
            elif label in nota_colors:
                new_colors.append(nota_colors[label])
        tr.marker.colors = new_colors

        tr.marker.line = dict(color = 'black', width = 0.3)  # Contorno preto, 1px de largura

# Impedir reordenação automática 
fig.update_traces(sort = False)

# Criar legendas para notas (interior) 
nota_legend = [go.Scatter(
    x = [None], y = [None],
    mode = 'markers',
    marker = dict(size = 15, color = color, line = dict(color = 'black', width = 1)),
    legendgroup = 'Notas',
    showlegend = True,
    name = nome
) for nome, color in nota_colors.items()]

# Criar legendas para internet (exterior) 
internet_legend = [go.Scatter(
    x = [None], y = [None],
    mode = 'markers',
    marker = dict(size = 15, color = color, line = dict(color = 'black', width = 1)),
    legendgroup = 'Internet',
    showlegend = True,
    name = nome
) for nome, color in internet_colors.items()]

# Adicionar todas as legendas à figura 
for trace in nota_legend + internet_legend:
    fig.add_trace(trace)

# Mostrar percentagem da camada interna (notas) diretamente nas fatias
for tr in fig.data:
    if tr.type == 'sunburst':
        # Criar lista de texttemplate apenas para camada interna
        texts = []
        for label, parent, custom in zip(tr.labels, tr.parents, tr.customdata):
            if parent == "":  # Camada interna (notas)
                texts.append(f"{custom[0]}<br>%{{percentParent:.1%}}")  # Rótulo curto + %
            else:             # Camada externa (internet)
                texts.append(f"{label}")
        tr.texttemplate = texts


fig.add_annotation(
    x = 0.01, # Horizontal relativa ao gráfico
    y = 0.000000005, # Vertical relativa ao gráfico
    text = "<b>181 Alunos</b>",
    showarrow = False,
    font = dict(size = 16, color = "black", family = "Tahoma"),
    align = "center",
    bordercolor = "black",
    borderwidth = 1,
    borderpad = 4,
    bgcolor = "white",
    xref = 'paper', # Coordenadas relativas à figura
    yref = 'paper'
)

fig.add_annotation(
    x = 0.99,
    y = 0.000000005,
    text = "<b>214 Alunos</b>",
    showarrow = False,
    font = dict(size = 16, color = "black", family = "Tahoma"),
    align = "center",
    bordercolor = "black",
    borderwidth = 1,
    borderpad = 4,
    bgcolor = "white",
    xref = 'paper',
    yref = 'paper'
)
fig.update_layout(
    title = dict(text = '<b>Influência de Explicações e Internet nas Notas de Matemática</b>', font = dict(
            color = "#A11D1D",
            family = "Tahoma",
            weight = 'bold',
            size = 23)),
    title_x = 0.5,
    height = 600,
    width = 1000,
    margin = dict(t = 50, l = 0, r = 0, b = 0),
    legend = dict(
        title_text = '<b>Legenda:<b>',
        orientation = 'h',
        yanchor = 'bottom',
        y = -0.17,
        xanchor = 'center',
        x = 0.5,
        bgcolor = "#FFF1FA", # Cor de fundo da legenda
        bordercolor = 'black', # Cor da borda da legenda
        borderwidth = 0.3
    ),
    paper_bgcolor = 'white',  
    plot_bgcolor = 'white' ,
    xaxis = dict(showticklabels = False),
    yaxis = dict(showticklabels = False),
)

fig.show()


## -- RELAÇÃO ENTRE A PROFISSÃO DOS PAIS E AS NOTAS DOS ALUNOS -- ##
# Será quer se os pais forem professores que os alunos têm melhor desempenho?
# Dividir as notas em bins
notas = ["0 a 4 - Mt. Insuf.", "5 a 9 - Insuf.", "10 a 13 - Suf.", "14 a 17 - Bom", "18 a 20 - Mt. Bom"]
bins = [0,5,10,14,18,21]

print (df_mat['Mjob'].unique())
print (df_pt['Mjob'].unique())
print (df_mat['Fjob'].unique())
print (df_pt['Fjob'].unique())

# Escolher apenas os alunos que têm os pais como professores
job_teacher_mat = df_mat [(df_mat['Mjob'] == 'teacher') | (df_mat['Fjob'] == 'teacher')]
job_teacher_pt = df_pt [(df_pt['Mjob'] == 'teacher') | (df_pt['Fjob'] == 'teacher')]

# Escolher os alunos que não têm os pais como professores
job_mat = df_mat [(df_mat['Mjob'] != 'teacher') & (df_mat['Fjob'] != 'teacher')]
job_pt = df_pt [(df_pt['Mjob'] != 'teacher') & (df_pt['Fjob'] != 'teacher')]

# Dividir as notas em bins
job_teacher_mat['nota_cat'] = pd.cut (job_teacher_mat['G3'], bins = bins, labels = notas, include_lowest = True)
job_teacher_pt['nota_cat'] = pd.cut (job_teacher_pt['G3'], bins = bins, labels = notas, include_lowest = True)
job_mat['nota_cat'] = pd.cut (job_mat['G3'], bins = bins, labels = notas, include_lowest = True)
job_pt['nota_cat'] = pd.cut (job_pt['G3'], bins = bins, labels = notas, include_lowest = True)

# Contar os alunos
count_teacher = pd.concat([job_teacher_mat['nota_cat'], job_teacher_pt['nota_cat']]).value_counts().reindex(notas, fill_value = 0)
count_nonteacher = pd.concat([job_mat['nota_cat'], job_pt['nota_cat']]).value_counts().reindex(notas, fill_value = 0)
print (count_teacher)

fig = make_subplots(rows = 1, cols = 2, specs = [[{"type": "funnel"}, {"type": "funnel"}]],
                    subplot_titles = ("Pais Professores", "Pais não Professores")
)

fig.add_trace(go.Funnel(y = notas[::-1], x = count_teacher.values[::-1], textinfo = "percent total", 
                        marker = dict(color = "#FE97D6"), name = "Alunos com Pais Professores"),
            row = 1, col = 1
)

fig.add_trace(go.Funnel(y = notas[::-1], x = count_nonteacher.values[::-1], textinfo = "percent total",
                        marker = dict(color =  "#C1B1F9"), name = "Alunos sem Pais Professores"),
            row = 1, col = 2
)

fig.update_layout(title = dict(text = "Relação entre Pais Professores e Classificações Finais dos Alunos", 
                               font = dict(color = "#966FC1", family = "Tahoma", weight = 'bold', size = 25)),
                               title_x = 0.5, height = 600,
                legend = dict(title_text = '<b>Legenda:<b>',
                bordercolor = 'black',  # Cor da borda da legenda
                borderwidth = 0.3,
                title_font = dict (size = 13)
    ),
    plot_bgcolor = 'white'
)

# Mudar as anotações da legenda
fig.update_annotations(font = dict(family = "Tahoma", size = 19, weight = "bold",
                                   color = ["#FE97D6", "#C1B1F9"][0])
)

# Mudar cor individualmente
fig.layout.annotations[0].font.color = "#FE97D6"  
fig.layout.annotations[1].font.color =  "#C1B1F9"   

# Para o primeiro funnel
fig.update_yaxes(showgrid = True, gridcolor = "lightgrey", gridwidth = 1, griddash = "dash"
)
# Para o segundo funnel
fig.update_yaxes(showgrid = True, gridcolor = "lightgrey", gridwidth = 1, row = 1, col = 2, griddash = "dash"
)
# Remove grelha vertical
fig.update_xaxes(showgrid = False)

fig.show()


## -- RELAÇÃO ENTRE O TEMPO DE ESTUDO, A NOTA FINAL (G3) E SE O ALUNO QUER SEGUIR ENSINO SUPERIOR - (BARRAS HORIZONTAIS) -- ##
fig, ax = plt.subplots(figsize = (10,6))

# Agrupar dados por studytime e G3
grouped = df_todos.groupby(['studytime', 'G3']).agg(total = ('higher', 'size'), 
                                                    no = ('higher', lambda x: (x == 'no').sum())
).reset_index()

# Largura máxima da barra horizontal (para o ponto com mais alunos)
max_bar_width = 1.0 
bar_height = 0.4

# Escala proporcional ao número de alunos
max_total = grouped['total'].max()
scale_factor = max_bar_width / max_total

for _, row in grouped.iterrows():
    x = row['studytime']
    y = row['G3']
    total = row['total']
    no = row['no']
    yes = total - no

    # Largura proporcional ao número de alunos nesse ponto
    total_width = total * scale_factor
    yes_width = total_width * (yes / total)
    no_width = total_width * (no / total)

    # Barra empilhada horizontal centrada no ponto x
    left_start = x - total_width/2
    ax.barh(y = y, width = yes_width, left = left_start, height = bar_height, color = "#81C6FF", edgecolor = 'black', linewidth = 0.5, zorder = 3)
    ax.barh(y = y, width = no_width, left = left_start + yes_width, height = bar_height, color = '#FE7272', edgecolor = 'black', linewidth = 0.5, zorder = 3)

# Definir labels para tempo de estudo
study_time = {1: "menos de 2 horas", 2: "2 a 5 horas", 3: "5 a 10 horas", 4: "mais de 10 horas"}

# Layout
ax.set_xlim(0.5, 4.5)
ax.set_ylim(min(df_todos['G3']) - 1, max(df_todos['G3']) + 1)
ax.set_xticks(list(study_time.keys())) # Define a posição dos ticks
ax.set_xticklabels(list(study_time.values())) # Define os nomes correspondentes
ax.set_yticks(range(0,21))
ax.set_xlabel("Horas de estudo", fontsize = 14)
ax.set_ylabel("Nota final do ano", fontsize = 14)
ax.tick_params(axis = 'both', labelsize = 12)
ax.set_title("Influência das Horas de Estudo e intenção de seguir para o Ensino Superior na Nota Final", 
             fontsize = 16, fontname = 'Verdana', color = "#A11D1D", fontweight = "bold", pad = 25)
ax.grid(True, linestyle = '--', alpha = 0.5, zorder = 1)
ax.axhline(y = 10, color = 'red', linewidth = 2, linestyle = '-', zorder = 0)

# Legenda
legend_elements = [
    Patch(facecolor = "#81C6FF", edgecolor = 'black', label = 'Quer ir para faculdade'),
    Patch(facecolor = "#FE7272", edgecolor = 'black', label = 'Não quer ir')
]
leg = ax.legend(
    handles = legend_elements,
    title = 'Desejo de ir para faculdade: ',
    loc = 'upper center',
    fontsize = 8,
    title_fontsize = 8,
    bbox_to_anchor = (0.85, 0.27)
)
# Caixa de texto acima da linha y=10
ax.text(
    x = 3.3, # Posição horizontal (à direita do gráfico)
    y = 10.5, # Ligeiramente acima da linha
    s = "Desta linha para cima\n os alunos têm positiva",
    fontsize = 8.5,
    fontweight = 'bold',
    color = '#FE7272',
    fontname = "Tahoma"
)
leg.get_title().set_fontweight("bold")
leg.get_frame().set_alpha(1)
plt.show()


# -- RELAÇÃO ENTRE O TEMPO DE ESTUDO E O NÚMERO DE FAILURES E O FREETIME -- ##
# Agrupar dados por studytime, failures e freetime
bubble_data = df_todos.groupby(['studytime','failures','freetime']).size().unstack(fill_value = 0)
bubble_data['total'] = bubble_data.sum(axis = 1)

# Definir cores para cada nível de freetime
freetime_colors = {1: "#ffe8f5", 2: "#f9c1e0", 3: "#ec9fcb", 4: "#f0cdff", 5: "#d299fd"}

fig, ax = plt.subplots(figsize = (10,6))

for (studytime, failures), row in bubble_data.iterrows():
    total = row['total']
    start_angle = 90
    for ft in range(1,6):  # freetime de 1 a 5
        size = row.get(ft,0)
        if size == 0:
            continue
        angle = 360 * size / total
        wedge = Wedge(
            center = (studytime, failures),
            r = 0.2 * (total**0.1), # Tamanho da bolha conforme total
            theta1 = start_angle,
            theta2 = start_angle + angle,
            facecolor = freetime_colors[ft],
            edgecolor = 'black',
            linewidth = 0.5,
            zorder = 3
        )
        ax.add_patch(wedge)
        start_angle += angle

# Definir labels para tempo de estudo
study_time = {1: "menos de 2 h", 2: "2 a 5 h", 3: "5 a 10 h", 4: "mais de 10 h"}

ax.set_xlim(0.5, 4.5)
ax.set_ylim(-0.7, 3.5)
ax.set_xticks(list(study_time.keys())) # Define a posição dos ticks
ax.set_xticklabels(list(study_time.values())) # Define os nomes correspondentes
ax.set_yticks(range(0,4))
ax.tick_params(axis = 'both', labelsize = 12)
ax.set_xlabel("Número de horas de estudo", fontsize = 14)
ax.set_ylabel("Número de reprovações", fontsize = 14)
ax.set_title("Relação entre número de reprovações, horas de estudo e tempo livre dos alunos", color = "#966FC1", fontweight = "bold", 
             fontsize = 20, pad = 25)
ax.grid(True, linestyle = '--', alpha = 0.7, zorder = 0)

# Rótulos que queres escrever manualmente
labels = [
    "Muito pouco tempo livre",
    "Pouco tempo livre",
    "Tempo suficiente",
    "Algum tempo livre",
    "Muito tempo livre"
]

# Criar elementos da legenda
legend_elements = [
    Line2D([0], [0],
           marker = 'o',
           color = 'w',
           label = labels[i-1], 
           markerfacecolor = color,
           markeredgecolor = 'black',
           markeredgewidth = 0.8,
           markersize = 10)
    for i, color in freetime_colors.items()
]

# Adicionar legenda ao gráfico
leg = ax.legend(handles = legend_elements, loc = 'upper right', title = "Legenda:", fontsize = 9, title_fontsize = 10)
leg.get_title().set_fontweight('bold')

plt.show()


## --- COMPARAÇÃO ENTRE AS NOTAS DE PORTUGUÊS E MATEMÁTICA DOS ALUNOS --- ##
# Criar bins
bins = [0,5,10,14,18,21]

# Criar labels
labels = ["0 a 4 - Mt. Insuf.", "5 a 9 - Insuf.", "10 a 13 - Suf.", "14 a 17 - Bom", "18 a 20 - Mt. Bom"]

# Ordem em que as notas aparecem
ordem_notas = {
    "0 a 4 - Mt. Insuf.": 0,
    "5 a 9 - Insuf.": 1,
    "10 a 13 - Suf.": 2,
    "14 a 17 - Bom": 3,
    "18 a 20 - Mt. Bom": 4
}

# Dividir as notas por bins e ordená-las
df_mat['nota_cat'] = pd.cut(df_mat['G3'], bins = bins, labels = labels, include_lowest = True).astype(str).str.strip()
df_mat["nota_order"] = df_mat["nota_cat"].map(ordem_notas)

df_pt['nota_cat'] = pd.cut(df_pt['G3'], bins = bins, labels = labels, include_lowest = True).astype(str).str.strip()
df_pt["nota_order"] = df_pt["nota_cat"].map(ordem_notas)

# Função que calcula as percentagens de cada classe de notas
def percentagens_notas(df):
    return df['nota_cat'].value_counts(normalize = True).sort_index() * 100

percent_pt = percentagens_notas(df_pt)
percent_mat = percentagens_notas(df_mat)

# Gráfico com as barras na horizontal
# Garantir a mesma ordem das categorias
categorias = ["0 a 4 - Mt. Insuf.", "5 a 9 - Insuf.", "10 a 13 - Suf.",
              "14 a 17 - Bom", "18 a 20 - Mt. Bom"]

# Preencher valores Na
pct_mat = percent_mat.reindex(categorias).fillna(0)
pct_pt  = percent_pt.reindex(categorias).fillna(0)

# Transformar matemática em valores negativos (para ficarem para o eixo negativo)
pct_mat_neg = - pct_mat

plt.figure(figsize = (10, 6))
y_pos = np.arange(len(categorias))

# Definir as barras do gráfico
plt.barh(y_pos, pct_mat_neg, color = "#C1B1F9", edgecolor = "#000000", linewidth = 0.3, label = "Matemática", zorder = 3)
plt.barh(y_pos, pct_pt, color = "#FE97D6", edgecolor = "#000000", linewidth = 0.3, label = "Português", zorder = 3)

# Linhas centrais
plt.axvline(0, color = "#555454", linewidth = 1.2, zorder = 4)

# Rótulos do eixo Y
tick_labels = [60, 40, 20, 0, 20, 40, 60] # Tornar todos positivos
plt.xticks([-60, -40, -20, 0, 20, 40, 60], tick_labels, fontsize = 12)
plt.yticks(y_pos, categorias, fontsize = 12)
plt.title("Comparação entre as Notas de Matemática e Português", fontsize = 22, fontweight = "bold", pad = 15, color = "#966FC1", fontname = 'Tahoma')

# Legenda
leg = plt.legend(loc = "upper right", frameon = True, title = "Legenda:", title_fontsize = 11)
leg.get_title().set_fontweight('bold')
plt.xlabel("Percentagem de alunos (%)", fontsize = 14)

# Grelha por trás do gráfico
plt.grid(axis = "x", linestyle = "--", linewidth = 0.5, alpha = 0.7, zorder = 0)
plt.tight_layout()
plt.show()


## -- DISTRIBUIÇÕES DAS NOTAS CONSOANTE A IDADE E TRAVELTIME -- ##
plt.figure(figsize = (10,6))

# Linha horizontal y = 10 atrás de tudo
plt.axhline(y = 10, color = 'red', linestyle = '--', zorder = 5)

# Boxplot base - cor clara e uniforme, contornos maiores, média visível
sns.boxplot(
    x = 'age', 
    y = 'G3', 
    data = df_todos, 
    color = "#FEE7FA",  # cor clara
    showfliers = False,
    width = 0.4,
    boxprops = dict(linestyle = '-', linewidth = 1, edgecolor = "#203188"),
    whiskerprops = dict(linewidth = 1.5, color = "#203188"),
    capprops = dict(linewidth = 1.5, color = '#203188'),
    zorder = 6
)
# Notas que queres usar para a linha azul manualmente
linhas_azuis = [12, 12, 12, 11, 10, 12, 10, 6.5]

# Desenhar linha azul manualmente
for i, nota in enumerate(linhas_azuis):
    plt.hlines(y = nota, xmin = i-0.20, xmax = i+0.20, colors = "#203188", linewidth = 2.3, zorder = 7)

# Obter mapeamento de idade para posição x do boxplot
idades = sorted(df_todos['age'].unique())  # ordena as idades
idade_pos = {idade: i for i, idade in enumerate(idades)}

# Frequências por idade, categoria e nota
frequencias = df_todos.groupby(['age', 'traveltime', 'G3']).size().reset_index(name='count')

# Cores e deslocamentos das quatro categorias de travel time
cores = {1: "#81C6FF", 2: "#CEE9FF", 3: "#FFF29F", 4: "#FE7272"}
deslocamento = {1: -0.3, 2: -0.09, 3: 0.09, 4: 0.3} 

for _, row in frequencias.iterrows():
    x_pos = idade_pos[row['age']] + deslocamento[row['traveltime']] 
    plt.scatter(
        x=x_pos,
        y=row['G3'],
        s=row['count']*10,
        color=cores[row['traveltime']],
        edgecolor='black',
        linewidth=0.7,
        alpha=1,
        zorder=7
    )

# Ajustar xticks para mostrar idades reais
plt.xticks(range(len(idades)), idades)


# Título e legendas
plt.title(
    "Influência que a Idade dos alunos e o Tempo que demoram a ir para a Escola têm nas suas Notas",
    fontdict = {'family': 'Tahoma', 'color': '#A11D1D', 'weight': 'bold', 'size': 18},
    loc = 'center', # Centraliza o título
    pad = 25 
)
plt.xlabel('Idade', fontsize = 14)
plt.ylabel('Nota', fontsize = 14)

# Grelha com traços
plt.grid(zorder = 0, linestyle = "--")

# Limites do eixo Y
plt.ylim(-0.5, 20.5)
plt.xticks(fontsize = 12) # Tamanho dos números do eixo X
plt.yticks(range(0, 21), fontsize = 12)

# Legenda manual com contorno nos patches e nomes mais claros
handles = [
    mpatches.Patch(facecolor = "#81C6FF", edgecolor = "black", label = "menos de 15 min"),
    mpatches.Patch(facecolor = "#CEE9FF", edgecolor = "black", label = "entre 15 a 30 min"),
    mpatches.Patch(facecolor = "#FFF29F", edgecolor = "black", label = "entre 30 min a 1 h"),
    mpatches.Patch(facecolor = "#FE7272", edgecolor = "black", label = "mais de 1h")
]
leg = plt.legend(
    title = "Tempo de viagem para a escola:",
    handles = handles,
    loc = 'upper right',
    prop = {'size': 7},
    title_fontsize = 8
)

# Título em bold
leg.get_title().set_fontweight("bold")

# Aplica alpha ao fundo da legenda
leg.get_frame().set_alpha(1)

plt.text(
    x = 7.3, # Posição horizontal (ajusta para mais à direita/esquerda)
    y = 11, # Um pouco acima da linha y = 10
    s = "Desta linha para cima\nos alunos têm positiva",
    fontsize = 8,
    fontweight = "bold",
    color = "#FE7272",
    ha = "center",
    va = "bottom",
    bbox = dict(
        facecolor = "white",
        edgecolor = "black",
        boxstyle = "round,pad=0.35"
    ),
    zorder = 20 # Fica acima de tudo
)
plt.show()


## -- PIEPLOTS DO SEXO CONSOANTE A NOTA FINAL (NOS COM ATIVIDADES E SEM ATIVIDADES) -- ##
# Escolher dataframe
df = df_mat_le.copy()

# Criar coluna de categoria de notas
def categoriza_nota(nota):
    if nota <= 4:
        return "0 a 4 - Mt. Insuf."
    elif nota <= 9:
        return "5 a 9 - Insuf."
    elif nota <= 13:
        return "10 a 13 - Suf."
    elif nota <= 17:
        return "14 a 17 - Bom"
    else:
        return "18 a 20 - Mt. Bom"

df['nota_cat'] = df['G3'].apply(categoriza_nota)

# Separar alunos com e sem atividades
df_atividades = df[df['activities'] == 1]
df_sem_atividades = df[df['activities'] == 0]

# Dicionário de cores
nota_colors = {
    "0 a 4 - Mt. Insuf.": "#FE7272",
    "5 a 9 - Insuf.": "#FEA7A7",
    "10 a 13 - Suf.": "#FFF29F",
    "14 a 17 - Bom": "#CEE9FF",
    "18 a 20 - Mt. Bom": "#81C6FF"
}

# Função para contar categorias de nota
def contar_categorias(df):
    return df['nota_cat'].value_counts().reindex(nota_colors.keys(), fill_value = 0)

# Contar notas para cada grupo
meninas_com = contar_categorias(df_atividades[df_atividades['sex'] == 1])
meninos_com = contar_categorias(df_atividades[df_atividades['sex'] == 0])
meninas_sem = contar_categorias(df_sem_atividades[df_sem_atividades['sex'] == 1])
meninos_sem = contar_categorias(df_sem_atividades[df_sem_atividades['sex'] == 0])

fig_meninas = make_subplots(
    rows = 1, cols = 2,
    specs = [[{'type':'domain'}, {'type':'domain'}]]
)

# Meninas com
fig_meninas.add_trace(go.Pie(
    labels = meninas_com.index,
    values = meninas_com.values,
    marker_colors = [nota_colors[i] for i in meninas_com.index],
    hole = 0.30,
    sort = False,
    direction = 'clockwise',
    texttemplate = "<b>%{percent:.1%}<br></b>%{label}</b>",
    textposition = "inside",
    marker = dict(
        line = dict(width = 0.7, color = "black")
    )
), row = 1, col = 2)

# Meninas sem
fig_meninas.add_trace(go.Pie(
    labels = meninas_sem.index,
    values = meninas_sem.values,
    marker_colors = [nota_colors[i] for i in meninas_sem.index],
    hole = 0.30,
    sort = False,
    direction = 'clockwise',
    texttemplate = "<b>%{percent:.1%}<br></b>%{label}</b>",
    textposition = "inside",
    marker = dict(
        line = dict(width = 0.7, color = "black")
    )
), row = 1, col = 1)

# Texto no centro de cada donut
fig_meninas.add_annotation(text = "<b>Meninas<br>Sem atividades<b>", x = 0.17, y = 0.5, showarrow = False,
                           font = dict(size = 18, color="black", family = "Tahoma"))
fig_meninas.add_annotation(text = "<b>Meninas<br>Com atividades<b>", x = 0.83, y = 0.5, showarrow = False,
                           font = dict(size = 18, color = "black", family = "Tahoma"))

fig_meninas.update_layout(
    title = dict(text = "<b>Distribuição das Notas das Meninas (Com vs Sem Atividades Extracurriculares)</b>",
        x = 0.5,
        font = dict(size = 25, family = "Tahoma", color = "#A11D1D")
    ),
    legend = dict(title = dict(text="<b>Legenda:</b>"), font = dict(size = 14, family = "Tahoma"))
)

fig_meninas.show()

fig_meninos = make_subplots(
    rows = 1, cols = 2,
    specs = [[{'type':'domain'}, {'type':'domain'}]]
)

# Meninos com
fig_meninos.add_trace(go.Pie(
    labels = meninos_com.index,
    values = meninos_com.values,
    marker_colors = [nota_colors[i] for i in meninos_com.index],
    hole = 0.30,
    sort = False,
    direction = 'clockwise',
    texttemplate = "<b>%{percent:.1%}<br></b>%{label}</b>",
    textposition = "inside",
    marker = dict(
        line = dict(width = 0.7, color = "black")
    )
), row = 1, col = 2)

# Meninos sem
fig_meninos.add_trace(go.Pie(
    labels = meninos_sem.index,
    values = meninos_sem.values,
    marker_colors = [nota_colors[i] for i in meninos_sem.index],
    hole = 0.30,
    sort = False,
    direction = 'clockwise',
    texttemplate = "<b>%{percent:.1%}<br></b>%{label}</b>",
    textposition = "inside",
    marker = dict(
        line = dict(width = 0.7, color = "black")
    )
), row = 1, col = 1)

# Texto no centro de cada donut
fig_meninos.add_annotation(text = "<b>Meninos<br>Sem atividades<b>", x = 0.17, y = 0.5, showarrow = False,
                           font = dict(size = 18, color = "black", family = "Tahoma"))
fig_meninos.add_annotation(text = "<b>Meninos<br>Com atividades<b>", x = 0.83, y = 0.5, showarrow = False,
                           font = dict(size = 18, color = "black", family = "Tahoma"))

fig_meninos.update_layout(
    title = dict(
        text = "<b>Distribuição das Notas dos Meninos (Com vs Sem Atividades Extracurriculares)</b>",
        x = 0.5,
        font = dict(size = 25, family = "Tahoma", color = "#A11D1D"
        )
    ),
    legend = dict(title = dict(text="<b>Legenda:</b>"), font = dict(size = 14, family = "Tahoma"))
)
fig_meninos.show()