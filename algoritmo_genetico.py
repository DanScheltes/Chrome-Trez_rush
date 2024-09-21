import random
import dinogame
import numpy


class Dino_Int:
    def __init__(self, qnt_peso, peso = None) -> None:
        # Inicializa os pesos aleatórios entre -1000 e 1000
        self.qnt_peso = qnt_peso
        self.pesos = peso if peso is not None else numpy.random.uniform(-1000, 1000, qnt_peso)
        self.pesos = self.pesos.astype(int)
        
    # Função de mutação para variar os genes dos dinossauros
    def mutate(self, mutation_rate=0.1):

        for i in range(len(self.pesos)):
            # Aplica a mutação com uma taxa definida, modificando os genes aleatoriamente
            if random.random() < mutation_rate:
                self.pesos[i] = numpy.random.uniform(-1000,1000,1)  # Gera uma nova ação aleatória
                self.pesos[i] = self.pesos[i].astype(int)


    def clone(self):
         return Dino_Int(self.qnt_peso, self.pesos)

    def get_action(self, game_state):
        # Calcula a soma ponderada (produto escalar) dos pesos e do estado do jogo
        weighted_sum = numpy.dot(self.pesos, game_state)

        # Usa a soma ponderada para decidir a ação:
        # - Se o valor for menor que 0, pular (ação 0)
        # - Se o valor for entre 0 e 500, agachar (ação 1)
        # - Se o valor for maior que 500, continuar correndo (ação 2)
        #print(weighted_sum)
        if weighted_sum < 0:
            return 0  # Pular
        elif 0 <= weighted_sum <= 500:
            return 1  # Agachar
        else:
            return 2  # Correr

# Define a função de avaliação (fitness) baseada no tempo de sobrevivência ou distância percorrida
def fitness(population, game):
        game.reset()
        while not game.game_over:
            game_state = game.get_state()
            actions = [agente.get_action(game_state[i]) for i, agente in enumerate(population)]
            game.step(actions)
        scores = game.get_scores()
        resultados = [(score, agente) for score, agente in zip(scores, population)]
        return resultados

# Função para gerar a população inicial de dinossauros
def generate_population(size):
    return [Dino_Int(10) for _ in range(size)]  # cria dinossauros com genes aleatórios




# Função principal para evoluir as gerações de dinossauros
def evolve(population, generations):
        game = dinogame.MultiDinoGame(fps=0, dino_count = pop_size) 
        for gen in range(generations): # Ordena a população com base no fitness (distância percorrida)
            agentes = fitness(population, game)
            agente_sort = sorted(agentes, key=lambda x: x[0], reverse=True)
            next_generation = []
            print(f"Geração {gen}: Melhor pontuação = {agente_sort[0][0]}")
            # Seleciona os dinossauros com melhor performance para o crossover
            top_dinos = agente_sort[0][1]

            # Gera a nova geração usando o crossover
            while len(next_generation) < len(population):
                parent1 = top_dinos.clone()
                next_generation.extend([parent1])
            for dino in next_generation:
                dino.mutate(1)
            # Atualiza a população para a próxima geração
            population = next_generation
        return population

# Exemplo de uso da função evolve
# População inicial de dinossauros
pop_size = 1000
generations = 50
population = generate_population(pop_size)

# Evoluir a população por várias gerações
final_population = evolve(population, generations)