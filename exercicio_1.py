print('''\033[1;32m]
primeiro repositorio aula_1 git

Cenário1: Você trabalha em uma equipe que deseja utilizar o git em seus projetos,
vocês já possuem um repositório criado e precisam configurar o repositório
(configurações do projeto, bibliotecas, documentação e etc) para começarem a trabalhar.
Descreva o que deverá ser feito para conseguir realizar o cenário acima. Lembre-se de 
que é necessário efetuar a configuração e disponibilizá-la para os demais colegas de 
equipe. Cite comandos que serão usados, qual a ordem que serão usados e etc.

R: Utilizar o comando pull, na main branch.Esse comando irá buscar as últimas alterações 
no repositório remoto e aplicá-las localmente. Criar uma branch. utilizar o merge para
unir o codigo. E utilizar o push, para o codigo ser enviado al repositório remoto, para
que os outros colegas de equipe possam atualizar o código deles com a ultima versão 
criada.
-------------------------------------------------------------------------------------------
\033[1;36m
Cenário2: Você e seus colegas de equipe estão trabalhando em cima do mesmo conjunto de
arquivos. Você precisa de uma atualização no seu repositório que algum de seus colegas
acabou de finalizar e fez o merge para a branch main. Descreva o que deverá ser feito
para conseguir realizar o cenário acima. Cite comandos que serão usados, qual a ordem 
que serão usados e etc

R: Sera usado o comando pull, para a atualização após essa atualização voltamos para a 
branch que estamos trabalhando e fazemos um rebase para atualizarmos a branch que estamos
trabalhando, neste processo usamos o comando de checkout para poder navegar entre as
branches e atualizá-las conforme a necessidade.
-------------------------------------------------------------------------------------------
\033[1;31m
Cenário3: Após um dia de trabalho você finalizou a codificação de uma tarefa e precisa 
unir o seu código com a main branch. Descreva o que deverá ser feito para conseguir 
realizar o cenário acima. Cite comandos que serão usados, qual a ordem que serão usados 
e etc

R: Utilizamos o comando push, esse comando é normalmente usado quando finalizamos a
 implementação de uma tarefa.
-------------------------------------------------------------------------------------------
\033[2;35m
Cenário4: A sua equipe estava tendo muitos problemas com o versionamento do código e 
decidiu pensar em uma estratégia para poder organizar melhor o código através de 
“versões candidatas” para produção. Para isso foi decidido criar uma nova branch com
o padrão de nome “rc_v150” (abreviação para “Release Candidate Version 1.5.0”) para 
a primeira versão a ser usada nesta nova estratégia. Descreva o que deverá ser feito
para conseguir realizar o cenário acima. Lembre-se de comentar como que a equipe irá
unir o código nessa branch, como criá-la e etc. Cite comandos que serão usados, qual
a ordem que serão usados e etc

R: Utilizaremos o checkout para restaurar a branch que estamos trabalhando para voltarmos
a última vesão que criamos,fazemos o pull para atualizar com a branch main, criamos uma 
nova branch para trabalhar o novo versionamento.
''')