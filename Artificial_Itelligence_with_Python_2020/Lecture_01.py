"""
Knowledge-based agents, são agentes que interpretam o mundo e tomam decisões baseadas no conhecimento que eles tem.
Sentece é uma afirmação que é verdadeira ou falsa. E um conjunto de sentenças é chamado de knowledge base.


Conectivos lógicos:
    ^ = and
    v = or
    ¬  = not
    => = (implicação)
    <=> = (equivalência)

    Exemplo:

    Se P = True, então ¬P = False.
    Se P = False, então ¬P = True.

    Se P = True e Q = True, então P ^ Q = True.
    Se P = True e Q = False, então P ^ Q = False.
    Se P = False e Q = True, então P ^ Q = False.
    Se P = False e Q = False, então P ^ Q = False.

    Se P = True e Q = True, então P v Q = True.
    Se P = True e Q = False, então P v Q = True.
    Se P = False e Q = True, então P v Q = True.
    Se P = False e Q = False, então P v Q = False.

    Se P = True e Q = True, então P => Q = True.
    Se P = True e Q = False, então P => Q = False.
    Se P = False e Q = True, então P => Q = True.
    Se P = False e Q = False, então P => Q = True.
        Um exemplo para implicação:
            P =(Se estiver chovendo), Q = (eu vou estar dentro de casa). Frase original.
            Se estiver chovendo, eu vou estar dentro de casa. -> P = True, Q = True, então P => Q = *True*.
            Se estiver chovendo, eu não vou  estar dentro de casa. -> P = True, Q = False, então P => Q = *False*. Pois não faz sentido eu estar fora de casa se estiver chovendo.
            Se não estiver chovendo, eu vou estar dentro de casa. -> P = False, Q = True, então P => Q = *True*. Pois não importa se está chovendo ou não, eu vou estar dentro de casa.
            Se não estiver chovendo, eu não vou estar dentro de casa. -> P = False, Q = False, então P => Q = *True*. Pois não importa se está chovendo ou não, eu posso estar ou nao dentro de casa.

    OBS: Ou seja quando P for False, então P => Q = True, independente do Q. E quando P for True, então P => Q = Q.

        Exemplo de equivalência ou Bicondicional:
            P = (Se estiver chovendo), Q = (eu vou estar dentro de casa). Frase original.
            Se estiver chovendo, eu vou estar dentro de casa. -> P = True, Q = True, então P <=> Q = *True*
            Se estiver chovendo, eu não vou  estar dentro de casa. -> P = True, Q = False, então P <=> Q = *False*.
            Pois na bicondicional acontece somente se ambas as condiçoes forem preenchidas ou se ambas falaharam.

            Se não estiver chovendo, eu vou estar dentro de casa. -> P = False, Q = True, então P <=> Q = *False*.
            Se não estiver chovendo, eu não vou estar dentro de casa. -> P = False, Q = False, então P <=> Q = *True*.
            Desta forma funcionando de uma forma parecida com o and, mas quando todos o valores tamebem resultam False, o retorno tambem será True.

    OBS: Ou seja quando P for False ou Q for False, então P <=> Q = False, apenas se o outro não for False tambem.
     E quando P for True e o Q tambem for então, então P <=> Q = True, e o mesmo vale caso for P = Q = False.

    OBS: O ¬ é mais forte que o ^ e o v, e o ^ é mais forte que o v.

    Um Modelo é uma interpretação de um conjunto de sentenças. Ou seja, é uma forma de interpretar as sentenças, criando um "Possivel Mundo".
    Um modelo é consistente se ele satisfaz todas as sentenças. Ou seja, se ele for verdadeiro para todas as sentenças.
    Um modelo é satisfatório se ele satisfaz uma sentença. Ou seja, se ele for verdadeiro para uma sentença.
    Um modelo é insatisfatório se ele não satisfaz uma sentença. Ou seja, se ele for falso para uma sentença.

    Exemplo de modelo:

    P = (Se estiver chovendo), Q = (É Terça-Feira).
    Neste modelo foi assumido que P = True e Q = False.
    Então P ^ Q = False, P v Q = True, P => Q = False, P <=> Q = False.

    O knowledge base é um conjunto de sentenças que são verdadeiras. Ou seja, é um conjunto de sentenças que são verdadeiras em um modelo. E que a IA pode utilizar para tomar decisões.

    Entailment é quando uma sentença é verdadeira em todos os modelos onde o knowledge base é verdadeiro. Ou seja, quando uma sentença é verdadeira em todos os modelos que satisfazem o knowledge base.

    a |= B, significa que B é consequência logica de a. Ou seja, B é verdadeiro em todos os modelos que satisfazem a. Ou seja se A for verdadeiro, então B tambem é verdadeiro. Sendo a = Alfa e B = Beta.
"""