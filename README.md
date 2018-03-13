
**********************************
CI065 

Algoritmos e Teoria dos Grafos  

Primeiro semestre de 2017  

### 2º trabalho - Sumidouros ### 
**********************************


**Ideia geral:**
 	- Para cada folha(sumidouro) subir para todos os pais, até a raiz, acrescentando o atributo no nodo que passar. 

**Ideia mais detalhada:**
 	- Para saber se é um vértice sumidouro verifica-se cada nodo e é feito uma contagem de filhos que este nodo possui, se ele não tiver uma aresta direcionada de saída (filho) será um vertice sumidouro. Também é feita uma contagem de vértices pai, pois um vertice pode possuir mais de uma aresta de entrada. A biblioteca pygraphviz é utilizada na implementação, as contagens são feitas para a lógica da utilização desta biblioteca. 
	- Cada vez que descobrimos um vértice sumidouro, subimos recursivamente pelos pais e acrescetado o atributo no nodo que passa,  até encontrar a raiz. Este será o vertice que não irá conter nenhuma aresta de entrada, apenas saída. 


OBS.: Gera arquivo temporário. Precisa poder de escrita.

