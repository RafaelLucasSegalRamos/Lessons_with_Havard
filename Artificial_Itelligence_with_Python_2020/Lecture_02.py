"""
Probabilidade e Incertezas de informações da IA.

- Probabilidade

Para representar a probabilidade de um evento, usamos a notação P(w), onde w (considrando w como simbolo do Ômega) é o evento em questão.

Exemplo de como funciona:
    0 <= P(w) <= 1
    0 <= P(w) <= 100%

    P(w) = 0 -> Impossível
    E -> (Considerando E como simbolo de Summation)
    E P(w) = 1 -> Certeza (Sendo que Ômega pentenece ao Onh) -> O que siginifaca que com o simbolo E vai continuar adcionando a P(w) até chegar em 1.
    Por exemplo
     Dado de 6 lados, a probabilidade de sair um número é 1/6, então a probabilidade de sair um número é 1/6 + 1/6 + 1/6 + 1/6 + 1/6 + 1/6 = 1
     Então P("O lado de 2 pontos") = 1/6

    Agora com dois dados:
    Primeiro consideramos todas as possibilidades de qualquer saida, no caso como são dois dados, então temos 6 * 6, ou seja 36 possibilidades.
    Ou seja a chance de cada lado sair é de P("combinação de dois dados") = 1/36

    Mas se formos considerar as somas, então temos:
    P(2 como soma total) = 1/36
    P(3 como soma total) = 2/36
    P(4 como soma total) = 3/36
    P(5 como soma total) = 4/36
    P(6 como soma total) = 5/36
    P(7 como soma total) = 6/36
    P(8 como soma total) = 5/36
    P(9 como soma total) = 4/36
    P(1 como soma total0) = 3/36
    P(1 como soma total1) = 2/36
    P(1 como soma total2) = 1/36

Probabilidade Condicional
    Base: P(A|B) -> Neste tipo de probabilidade temos que considerar que A é True, e que B é uma evidencia que A é True.
    Exemplo:
        P("Choveu Hoje"|"Choveu Ontem")

        P("A rota de trânsito mudou"|"Condição do tráfico de trasito") -> poderimos traduzir
        para o potuguês assim: "A rota de trânsito mudou dado a condição do tráfico de trasito"

        P("Doença"| "Resultado dos teste") -> "Você tem a doença dado o resultado dos teste"

        Na forma de progamção o compudador vai entender assim:
        P(A|B) = P(A ^ B) / P(B)

        Agora nós vamos ter evidencias na concional:
        P(Sum 12 ^ "Lado de 6 pontos") = 1/6
        Já que temos certeza que vai sair o lado de 6 pontos no dado vermelho,
        e só uma possibilidade de sair o lado de 6 pontos no dado azul então podemos assumir que só existe 1/6 de chance de acontecer.

        P(A ^ B) = P(B) * P(A|B)
        P(A ^ B) = P(A) * P(B|A)

        outras variaveis aleátorias:
        clima = {"Chuvoso", "Ensolarado", "Nublado", "Ventania", "Neve"}

        trafico = {"Leve", "Pesado", "Nenhum"}

        Voô = {"Atrasado", "No Horário", "Cancelado"}

        Distribuição de probabilidade:
        P(voô = "Atrasado") = 0.3
        P(voô = "No Horário") = 0.6
        P(voô = "Cancelado") = 0.1
        No caso o resultado é o percentual de chance de acontecer, no caso são 30%, 60% e 10% respectivamente.
        No caso a nossa variavel fica assim:
        P(voô) = <0.3,0.6,0.1>

        Tambem podemos ter eventos independentes, que são eventos que mesmo que aconteçam ou não, não irá interfiir no resultado de outro evento.
        OBS: tambem podem ter eventos ocorram e aumentem a chance de outro evento acontecer tambem. Como por exemplo um céu nublabo aumenta a chance de chover.

        Sua expressão é: P(A ^ B) = P(A) * P(B)

        P("Lado de 6 pontos""Lado de 4 pontos") != P("Lado de 6 pontos") * P("Lado de 4 pontos")

        Então pela regra de Bayes
        P(A|B) = P(A) * P(B|A) / P(B) ou P(A|B) = P(B) * P(A|B) / P(A)

        Negation de probabilidade:
        P(¬ A) = 1 - P(A)
    """