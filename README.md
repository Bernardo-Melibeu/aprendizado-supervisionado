Caro aluno(a) Bernardo,
Nessa disciplina, aprendemos nossos conhecimentos em algoritmos supervisionados, família de algoritmos que é extremamente importante para o dia-a-dia de um cientista de dados. Agora iremos validar nosso conhecimento. 



1) Faça o módulo do Kaggle Intro to Machine Learning:
Comprove a finalização do módulo com um print que contenha data e identificação do aluno. 
[FEITO]


Trabalho com base:

Iremos usar a base de dados de vinhos verdes portugueses (nas variantes branco e tinto) que encontra-se disponível no Kaggle:

Para as questões 2-5 usaremos apenas os vinhos do tipo "branco".



2) Faça o download da base - esta é uma base real, apresentada no artigo:
P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.

Ela possui uma variável denominada "quality", uma nota de 0 a 10 que denota a qualidade do vinho. Crie uma nova variável, chamada "opinion" que será uma variável categórica igual à 0, quando quality for menor e igual à 5. O valor será 1, caso contrário. Desconsidere a variável quality para o restante da análise.
[FEITO]




3) Descreva as variáveis presentes na base. Quais são as variáveis? Quais são os tipos de variáveis (discreta, categórica, contínua)? Quais são as médias e desvios padrões?
As variaveis são:

As variáveis da base descrevem caracteristicas da composição do vinho. De catégorica temos somente a variavel "tipo", de discreta "qualidade", e o resto é contínua. Médias e desvios padrões estão na seção "Média e desvio padrão"
do arquivo "pt1.ipynb".




4) Com a base escolhida:


a) Descreva as etapas necessárias para criar um modelo de classificação eficiente.

Os primeiros passos(arquivo prep.py) são preparar a base, cortando valores nulos e criando as categorias extras relevantes(opinion). Depois(arquivo pt1.ipynb) precisa-se fazer um estudo da base e ver como as varivaveis se relacionam com a variavel
"qualidade". Feito isso, podemos passar a testar modelos(arquivo pt2.ipynb),lembrando sempre de escalar a variaveis e de separar partes para treino e teste. 




b) Treine um modelo de regressão logística usando um modelo de validação cruzada estratificada com k-folds (k=10) para realizar a classificação. Calcule para a base de teste:
i. a média e desvio da acurácia dos modelos obtidos;
ii. a média e desvio da precisão dos modelos obtidos;
iii. a média e desvio da recall dos modelos obtidos;
iv. a média e desvio do f1-score dos modelos obtidos.
[FEITO]




c) Treine um modelo de árvores de decisão usando um modelo de validação cruzada estratificada com k-folds (k=10) para realizar a classificação. Calcule para a base de teste:
i. a média e desvio da acurácia dos modelos obtidos;
ii. a média e desvio da precisão dos modelos obtidos;
iii. a média e desvio da recall dos modelos obtidos;
iv. a média e desvio do f1-score dos modelos obtidos.
[FEITO]



d) Treine um modelo de SVM usando um modelo de validação cruzada estratificada com k-folds (k=10) para realizar a classificação. Calcule para a base de teste:
i. a média e desvio da acurácia dos modelos obtidos;
ii. a média e desvio da precisão dos modelos obtidos;
iii. a média e desvio da recall dos modelos obtidos;
iv. a média e desvio do f1-score dos modelos obtidos.
[FEITO]


5) Em relação à questão anterior, qual o modelo deveria ser escolhido para uma eventual operação. Responda essa questão mostrando a comparação de todos os modelos,
usando um gráfico mostrando a curva ROC média para cada um dos gráficos e justifique.

Considerando o uso do programa para apontar vinhos de alta qualidade, eu usaria o modelo SVM para ter a maior taxa de recall(88%) e um f1 score alto(84%).


6) Com a escolha do melhor modelo, use os dados de vinho tinto, presentes na base original e faça a inferência (não é para treinar novamente!!!)
para saber quantos vinhos são bons ou ruins. Utilize o mesmo critério utilizado com os vinhos brancos, para comparar o desempenho do modelo. Ele funciona da mesma forma para essa nova base? Justifique.


Não. Os criterios para um vinho branco bom são diferentes do que os de um tinto, o que resulta num classificador ineficiente.






7) Disponibilize os códigos usados para responder da questão 2-6 em uma conta github e indique o link para o repositório.
[FEITO]


Assim que terminar, salve o seu arquivo PDF e poste no Moodle. Utilize o seu nome para nomear o arquivo, identificando também a disciplina no seguinte formato: “nomedoaluno_nomedadisciplina_pd.PDF”.
