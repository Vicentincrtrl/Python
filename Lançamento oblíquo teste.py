import numpy as np
import matplotlib.pyplot as plt

def plot_lancamento_obliquo(v0, theta_graus):
    g = 9.84  #Aceleração da gravidade (padrão = 9.84m/s^2)
    theta = np.deg2rad(theta_graus)  #Converte ângulo para radianos (facilita a vida do aluno rs)

    #bloco das componentes vx e vy (velocidades horizontais e verticais)
    vx = v0 * np.cos(theta)
    vy = v0 * np.sin(theta)

    # Tempo total de voo
    t_total = 2 * vy / g
    t = np.linspace(0, t_total, 300)

    #bloco de fórmulas da posição em x e y (horizontal e vertical)
    x = vx * t
    y = vy * t - 0.5 * g * t**2

    #bloco de fórmulas de alcance e altura máxima
    alcance = (v0**2) * np.sin(2*theta) / g
    altura_max = (v0**2) * (np.sin(theta))**2 / (2*g)

    #bloco de impressão dos dados
    print(f"\n → Resultados para v₀ = {v0} m/s e θ = {theta_graus}°:")
    print(f"→ Alcance: {alcance:.2f} metros")
    print(f"→ Altura máxima: {altura_max:.2f} metros")
    print(f"→ Tempo total de voo: {t_total:.2f} segundos\n")

    #bloco para plotar o gráfico de trajetória, alcance e os pontos mais importantes
    lt.figure(figsize=(10, 5))
    plt.plot(x, y, label='Trajetória')
    plt.scatter([alcance], [0], color='red', label='Alcance')
    plt.scatter([x[np.argmax(y)]], [altura_max], color='green', label='Altura Máxima')
    plt.xlabel('Distância (m)')
    plt.ylabel('Altura (m)')
    plt.title(f'Lançamento Oblíquo\nv₀ = {v0} m/s, θ = {theta_graus}°')
    plt.xlim(0, alcance * 1.1)
    plt.ylim(0, altura_max * 1.2)
    plt.grid(True)
    plt.legend()p
    plt.tight_layout()
    plt.show()

#Escolha suas variáveis:
velocidade_inicial = 30  # em m/s
angulo_graus = 45        # em graus
plot_lancamento_obliquo(velocidade_inicial, angulo_graus)
