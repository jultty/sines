#import "@local/skolar:0.2.0": *
#import "@preview/tablex:0.0.8": tablex, cellx, colspanx, rowspanx

#let meta = (
  title: [Representação Gráfica de \ Qualquer Função Seno e Cosseno],
  author: "Juno Takano",
  course: "Tópicos Avançados de Matemática para Computação",
  course_id: "TAMC",
  date: datetime.today().display("[day]/[month]/[year]"),
  flipped: true,
  margin_x: 2cm,
  margin_y: 2cm,
)

#let fig(path, caption) = {
  pad(y: 0em, [
    #figure(
      image(path, width: 100%),
      caption: caption
    )
  ])
}

#generate_document(properties: meta)[
  #fig("img/overlay-a0.7-b2.4-c0-d1.png", [Saída do algoritmo desenvolvido para as entradas `a = 0.7`, `b = 2.4`, `c = 0` e `d = 1` com a opção de sobrepor ambas as funções (seno e cosseno).])

  O presente trabalho e o código fonte associado implementam um algoritmo para a representação gráfica das funções seno e cosseno seguindo uma lei de formação onde $f(x) = a sin(b x + c) + d$ ou $g(x) = a cos(b x + c) + d$.

  Como resultado, é possível observar as curvas resultantes para:

  1. A função seno
  1. A função cosseno
  1. Ambas as funções sobrepostas

  O programa solicita à pessoa usuária que forneça a opção correspondente a quais funções trigonométricas deseja visualizar, e em seguida solicita os valores para $a$, $b$, $c$ e $d$:

  ```sh
  Escolha as funções trigonométricas:
   [1] seno
   [2] cosseno
   [3] sobrepor ambas
  Digite o número correspondente a uma opção acima:
  2
  Você deverá inserir os valores para a, b, c e d a seguir.
  Insira um valor para a (amplitude):
  -0.5
  Insira um valor para b (frequência):
  1.2
  Insira um valor para c (deslocamento horizontal):
  0.3
  Insira um valor para d (deslocamento vertical):
  2.1
  ```
  #align(center)[Código 1: Exemplo de entrada de dados.]

  #fig("img/sine-a1.5-b5-c-2.5-d-0.5.png", [Saída do algoritmo desenvolvido para as entradas `a = 1.5`, `b = 5`, `c = -2.5`, d= `-0.5` usando apenas a opção de exibir a função seno.])

  Estas representações são exibidas sobre um plano cartesiano, com eixos $x$ e $y$ anotados com os respectivos valores em uma escala decimal de 1:1. O título exibido acima permite diferenciar as funções e explicita quais cores correspondem a quais funções caso a opção escolhida seja de sobrepô-las.

  #fig("img/cosine-a-0.5-b1.2-c0.3-d2.1.png", [Saída do algoritmo desenvolvido para as entradas `a = 1.5`, `b = 5`, `c = -2.5`, d= `-0.5` usando apenas a opção de exibir a função cosseno.])

  O código fonte deste algoritmo foi entregue junto ao trabalho e também está disponível online em #link("https://github.com/jultty/sines").

]
