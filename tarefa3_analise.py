from lead import Lead
from tarefa1_grafo import fluxo_crm
from tarefa2_dijkstra import melhor_rota

paciente = Lead("Davis Junior", "11998887766", "davis@email.com", "555.666.333-00")

print(f"--- Analisando fluxo para paciente: {paciente.nome} ---")
rota, custo_total = melhor_rota(fluxo_crm, 'Lead recebido', 'Confirmação')

print(f"\nMelhor rota: {' -> '.join(rota)}")
print(f"Custo de conversão: {custo_total}")

print("\nANÁLISE DE NEGÓCIO:")
if 'Avaliação online' in rota:
    print("- O sistema sugere a prioridade da avaliação online para este lead devido ao menor conflito inicial.")
if 'Negociação' in rota:
    print("- A etapa de negociação foi incluída por conta da redução do custo final comparado ao fechamento direto.")