import heapq


def melhor_rota(grafo, inicio, fim):

    distancias = {no: float('inf') for no in grafo}
    distancias[inicio] = 0
    rota_anterior = {no: None for no in grafo}

    fila_prioridade = [(0, inicio)]

    while fila_prioridade:
        distancia_atual, no_atual = heapq.heappop(fila_prioridade)

        if distancia_atual > distancias[no_atual]:
            continue

        for vizinho, peso in grafo[no_atual].items():
            distancia = distancia_atual + peso

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                rota_anterior[vizinho] = no_atual
                heapq.heappush(fila_prioridade, (distancia, vizinho))

    rota = []
    atual = fim
    while atual is not None:
        rota.insert(0, atual)
        atual = rota_anterior[atual]

    return rota, distancias[fim]