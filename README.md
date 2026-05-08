# Vitalink - Challenge 2026 - Sprint 4 - Dynamic Programming

## Visão Geral
Em uma instituição de saúde, nem todo caminho até a venda é igual. Algumas etapas geram mais resistência (ou custo) que outras. O VitaLink aplica o Algoritmo de Dijkstra para calcular a rota de menor resistência dentro de um grafo que representa o CRM.

## Arquitetura do Sistema
O projeto é dividido em módulos para facilitar a manutenção e escalabilidade:

- **`lead.py`**: Modelo de dados do paciente.
- **`tarefa1_grafo.py`**: Modelagem do funil de vendas (nós e pesos).
- **`tarefa2_dijkstra.py`**: Motor matemático (Dijkstra com Min-Heap).
- **`tarefa3_analise.py`**: Interface de saída e geração de insights de negócio.

## O Grafo do Funil (CRM)
O VitaLink analisa as seguintes etapas:
1. **Lead recebido** -> triagem
2. **Triagem** -> Escolha entre avaliação online ou presencial
3. **Avaliação** -> orçamento
4. **Orçamento** -> negociação ou confirmação direta

1. ## Diagnóstico de Eficiência e "Menor Caminho"
O "menor caminho" identificado não refere-se à distância, mas à fluidez do processo. O algoritmo selecionou o caminho que minimiza os pesos (atritos), demonstrando que o fluxo pela avaliação online é o caminho de menor resistência. Isto ocorre porque o sistema identifica matematicamente que remover barreiras físicas e logísticas no início da jornada reduz o custo total de aquisição do cliente, tornando a operação da clínica mais leve e rápida.

2. ## Redução de Custos via Inteligência de Fluxo
A análise revela que o custo total é otimizado ao incluir etapas estratégicas, como a negociação. Embora pareça um passo adicional, o sistema prova que investir tempo nessa etapa tem um custo menor (peso 5) do que o risco de um fechamento direto (peso 6), que possui maior taxa de rejeição. Assim, a eficiência do VitaLink reside em converter dados técnicos em uma verdadeira economia, escolhendo caminhos que demandam menos recursos da equipe para atingir o fechamento do serviço.

## Como Executar
Certifique-se de que todos os arquivos `.py` estão no mesmo diretório e execute:

```bash
python tarefa3_analise.py
