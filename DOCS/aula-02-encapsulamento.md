Com certeza, aqui está o texto completo da documentação presente na imagem:

Encapsulamento e @property - Aula 02

Entrada conceitual do catálogo. Não é um padrão GoF - é a base de OO que os
padrões vão usar a partir de 18/09. Construída com TDD.

O problema que resolve

Um atributo público aceita qualquer valor, inclusive inválido. Uma Reserva com
diária negativa ou zero diárias passa sem reclamar. A regra do negócio existe só
na cabeça do programador - o código não garante nada.

A solução

O objeto controla o acesso ao próprio estado. Com @property e setter, ler e
escrever um atributo vira operação que valida antes de gravar - sem mudar o
códigos de quem usa a classe. (Analogia: o cofre do quarto. O hóspede usa; não
mexe na fechadura.)

Como foi construída (TDD)

1.  Teste primeiro (🔴): test_cria_reservas, sem a classe -> ModuleNotFoundError
2.  Classe mínima (🔴): init que guarda os dados
3.  Teste do negativo (🔴): DID NOT RAISE - a classe aceitava valor inválido
4.  @property + setter (🟢): validação levanta ValueError
5.  Diárias (regra < 1) e total (calculado, sem setter)

Exemplo em Python

[colar aqui a classe Reserva final]

Quando usar / quando NÃO usar

USAR: atributo com regra (valor >= 0, diárias >= 1), dependente de outros (total
= diárias * valor), ou só-leitura. NÃO usar: atributo sem regra (hóspede, um
texto livre). Vira cerimônia - e proteção sem problema que a justifique conta
zero (critério antifachada).

Fonte

Documentação oficial do Python - property:
https://docs.python.org/pt-br/3/library/functions.html#property FREEMAN &
FREEMAN, Use a Cabeça! Padrões de Projetos - Cap. 1.