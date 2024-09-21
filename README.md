# Chrome-Trez_rush
# Seleção dos Algoritmos e Justificativas
## Algoritmo de Seleção
Optamos por usar o Algoritmo de Seleção por Roleta no nosso projeto. Este algoritmo funciona atribuindo a cada indivíduo da população uma probabilidade de ser selecionado baseada em sua aptidão (fitness). Quanto maior a aptidão de um indivíduo, maior a sua chance de ser escolhido para a próxima geração.

A implementação da seleção por roleta garante que indivíduos com melhores desempenhos têm mais chances de continuar no processo evolutivo, mantendo a diversidade e dando a chance de indivíduos menos aptos contribuírem para a próxima geração. Testamos também Seleção por Torneio, mas notamos que o algoritmo por roleta gerava uma convergência mais estável ao longo das gerações, pois evitava a concentração muito rápida de bons indivíduos.

## Algoritmo de Crossover
Utilizamos o Crossover Uniforme para gerar os descendentes. Neste tipo de crossover, cada gene de um indivíduo é trocado com o gene correspondente do outro indivíduo com uma probabilidade de 50%. Isso permite uma maior variação genética entre as novas gerações. Além disso, testamos o crossover One-point (corte único), mas observamos que o uniforme gerava maior diversidade, aumentando a probabilidade de soluções mais variadas.

## Algoritmo de Mutação
Para a mutação, escolhemos o Algoritmo de Mutação de Gene Único. Neste algoritmo, há uma chance predefinida de que cada gene em um indivíduo seja modificado. Essa taxa de mutação foi ajustada para 5% em nossos experimentos, o que resultou em um bom equilíbrio entre exploração e exploração. Tentativas com mutações mais frequentes tornaram o processo de convergência mais lento.

## Avaliação da Aptidão (Fitness)
Para avaliar o fitness, consideramos o tempo de sobrevivência do dinossauro durante o jogo. O objetivo do algoritmo era maximizar o tempo em que o dinossauro permanecia vivo, evitando os obstáculos. A função fitness foi crucial para selecionar indivíduos mais aptos, levando ao resultado de um individuo que não perde mais o jogo.

https://github.com/user-attachments/assets/bf5b0547-dc63-4b39-be7e-26558c93a4d4

## Treinamento
Segue o vídeo do treinamento do dino, percebe-se que primeiro foram necessario 5 gerações para que enfim ele chegasse a um nível onde o dino não morria mais para os catus nem para os pteros.



https://github.com/user-attachments/assets/bc59d549-dbe2-4a50-82ff-2c0eb534c33f



## Desempenho Geral e Ajustes
Durante o desenvolvimento, identificamos que o ajuste da taxa de mutação e do tipo de seleção foi essencial para alcançar uma convergência eficiente. Por exemplo, ao diminuir a taxa de mutação, os indivíduos começaram a se adaptar mais rapidamente aos obstáculos, mas uma mutação muito baixa resultava em estagnação.

Outro desafio foi ajustar a velocidade do jogo para que a população não se adaptasse a um cenário estático. Introduzimos uma aceleração gradual no jogo para aumentar a dificuldade ao longo do tempo, forçando a adaptação contínua da população.


## Apresentação




## Curiosidades e Dificuldades:

* Otimização do Crossover: Embora o crossover uniforme tenha proporcionado mais diversidade, demorou mais tempo para estabilizar o fitness médio da população.
* Dificuldade na Mutação: O ajuste da taxa de mutação foi um ponto crítico, pois valores muito altos causavam uma grande flutuação no desempenho da população.
* Escalabilidade: A implementação do algoritmo genético com uma população maior melhorou significativamente a diversidade genética, mas aumentou o tempo de execução.
