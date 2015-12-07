# findphone

# Sobre a abordagem
Para resolver o problema de conversão de telefones, apesar de ser um problema simples,
optei por criar uma classe chamada PhoneConverter que contém um Dicionário com as letras->número.
Vários motivos me levaram a abordar dessa maneira e não apenas criar métodos soltos no arquivo.
Com o encapsulamento além de ser mais organizado é mais fácil implementar novas funções e/ou dar manutenção.
A entrada para conversão é um arquivo chamado input.txt.

# Funcionamento da classe
Para converter uma entrada existem três maneiras de utilização da classe:

1.<code> PhoneConverter("MINHA-ENTRADA").convert() </code>  # Inicializa a variável str_input no construtor e converte

2.<code> PhoneConverter().convert("MINHA-ENTRADA") </code> # Seta a variável str_input e converte

3.<code>obj = PhoneConverter()                  
    obj.set_input("MINHA-ENTRADA")
    obj.convert()
   </code>   # Cria o objeto, inicializa a variável de entrada e converte.
   
Todos os modos de utilização têm o mesmo resultado.

As variáveis str_input e str_converted foram criadas para que os valores de entrada e saída sejam guardados e manipulados
caso novas funcionalidades sejam acrescentadas a classe.

# Como rodar a aplicação
A solução foi feita em Python 3.4.x.

Basta acessar a pasta findphone e para rodar os testes digite o comando <code> python tests.py </code>.
Para rodar a leitura do arquivo de entrada <code> python main.py" </code>

Para alterar a entrada basta editar o arquivo "input.txt"
