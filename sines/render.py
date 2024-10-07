import matplotlib.pyplot as plt
import numpy as np

# Input
print('Escolha as funções trigonométricas:')
print(' [1] seno')
print(' [2] cosseno')
print(' [3] sobrepor ambas')
print(' Digite o número correspondente a uma opção acima:')
input_f = int(input())
if input_f == 1 or input_f == 2 or input_f == 3:
    print('Você deverá inserir os valores para a, b, c e d a seguir.')
    print('Insira um valor para a (amplitude):')
    input_a = float(input())
    print('Insira um valor para b (frequência):')
    input_b = float(input())
    print('Insira um valor para c (deslocamento horizontal):')
    input_c = float(input())
    print('Insira um valor para d (deslocamento vertical):')
    input_d = float(input())
else:
    print('Escolha inválida')
    exit()

def render():

    # Axis and grid setup
    _, ax = plt.subplots(figsize=(10, 10))

    xmin, xmax, ymin, ymax = -5, 5, -5, 5
    ticks_frequency = 1

    ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.set_xlabel('$x$', size=14, labelpad=-24, x=1.02)
    ax.set_ylabel('$y$', size=14, labelpad=-21, y=1.02, rotation=0)

    x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
    y_ticks = np.arange(ymin, ymax+1, ticks_frequency)

    ax.set_xticks(x_ticks[x_ticks[x_ticks != 0]])
    ax.set_yticks(y_ticks[y_ticks[y_ticks != 0]])
    ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
    ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    # Sine
    sin_x = np.arange(-5, 5*np.pi, 0.01)
    sin_y = input_a * np.sin(input_b * sin_x + input_c) + input_d

    if input_f == 1 or input_f == 3:
        plt.plot(sin_x, sin_y, color=('green', 0.5), linewidth=1)

    # Cosine
    cos_x = np.arange(-5, 5*np.pi, 0.01)
    cos_y = input_a * np.cos(input_b * cos_x + input_c) + input_d

    if input_f == 2 or input_f == 3:
        plt.plot(cos_x, cos_y, color=('purple', 0.5))

    # Title and Scale
    if input_f == 1:
        title_string = 'Função Seno'
    elif input_f == 2:
        title_string = 'Função Cosseno'
    else:
        title_string = 'Funções \nseno (verde) \ne cosseno (roxo)'

    plt.text(-5, 6, title_string, fontsize=15, color=('k', 1),
             horizontalalignment='left', verticalalignment='top')
    plt.text(6, -6, 'Escala: 1:1', fontsize=10, color=('k', 0.6), horizontalalignment='right')

    plt.show()
