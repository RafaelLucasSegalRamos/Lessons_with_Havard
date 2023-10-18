"""Depth First Search Algorithm é quando você vai até o final de um caminho e depois volta para o começo e vai por outro
caminho. O caminho que será vasculhado primeiro é o caminho mais a esquerda e assim até o final."""

"""Breadth First Search Algorithm é quando a IA ela passa por todos os nodes possiveis de um nível antes de passar para
o próximo nível."""

"""O node que estão sendo pesquisados são chamados de frontier."""

"""Para termos uma noção de onde o algoritimo já passou, usamos uma lista de nós visitados. O Explored Set."""

"""A logica do algoritimo é:
1. Colocar o nó inicial na frontier.
2. Enquanto a frontier não estiver vazia:
    2.1. Retirar um nó da frontier.
    2.2. Se o nó for o objetivo, então retornar o caminho. Pulando então o passo 3.
    2.3. Se não for o objetivo, então colocar o nó no explored set.
    2.4. Expandir o nó e colocar os nós filhos na frontier. Caso o nó já esteja na frontier ou no explored set, então
    não colocar na frontier.
    
3. Retornar falha."""

"""Greedy Best First Search Algorithm é quando você escolhe o nó que está mais perto do objetivo. Para isso, você precisa
de uma heuristica que te diga qual nó está mais perto do objetivo. Por exemplo se num caminho tiver ambas as opções de ir para esquerda e direita,
mas a direita tem valor 14 e a esquerda tem valor 10, então o algoritimo vai escolher o caminho da esquerda. Isto pode ser bom ou ruim, pois
pode ser que o caminho da esquerda seja mais longo, mas o algoritimo não vai saber disso."""

"""por isso então utilizamos o *A search algorithm* que é um algoritimo que utiliza o Greedy Best First Search Algorithm,
mas ele também leva em consideração o custo do caminho. Então ele vai escolher o caminho que tem o menor custo. utilizando
a função que pega do menor valor de g(n)+h(n). Sendo g(n) o custo do caminho e h(n) a heuristica. 
Traduzindo seria a distancia até a chagada(Definida pelo Greedy Best First Search First Search)  +  Quantos passos foram dados até o momento."""
"""O algoritimo A* é ótimo, mas só é funcional se a heuristica(h(n)) for admissível. Ou seja, 
se a heuristica nunca superestimar o verdadeiro custo, e se o custo do caminho nunca for negativo e se for consistente (ou monotônico)."""


"""
    Existe tambem o estilo MinMax que podemos utiliza-lo no jogo da velha. Onde o exemplo do professor foi:
    O jogador 'O' é o jogador que quer minimizar o resultado. Sendo que quando ele ganha o resutado retorna -1,.
    O jogador 'X' é o jogador que quer maximizar o resultado. Sendo que quando ele ganha o resutado retorna 1.
    E quando acontece um empate o resultado retorna 0.
"""