import random
from lead import Lead
from tarefa1_grafo import fluxo_crm
from tarefa2_dijkstra import melhor_rota

banco_insights = {
    "digital": [
        "- O atrito inicial foi reduzido usando o canal digital.",
        "- Eficiência digital: Menor resistência detectada via atendimento online.",
        "- O lead optou pela conveniência do fluxo remoto, acelerando o início."
    ],
    "negociação": [
        "- Passo de negociação acionado para baratear o esforço de fechamento.",
        "- Estratégia de consultoria: Negociação inserida para garantir a conversão.",
        "- O custo de fechamento caiu graças à etapa intermediária da negociação."
    ],
    "retomada": [
        "- Retomar este lead custa apenas metade do esforço de captar um novo!",
        "- Alerta de reengajamento: Este cliente já possui histórico, facilitando a venda.",
        "- Oportunidade de ouro: Lead reaquecido com baixo custo de conversão."
    ],
    "meta_parcial": [
        "- Meta da campanha atingida. Preparar equipe de recepção.",
        "- Foco em visita: O objetivo de levar o cliente à clínica foi cumprido.",
        "- Sucesso: Lead convertido para a etapa presencial conforme planejado."
    ]
}

def gerar_diagnostico_randomizado(rota, inicio, fim):
    insights_validos = []

    if 'Avaliação online' in rota:
        insights_validos.append(random.choice(banco_insights["digital"]))

    if 'Negociação' in rota:
        insights_validos.append(random.choice(banco_insights["negociação"]))

    if inicio == 'Orçamento':
        insights_validos.append(random.choice(banco_insights["retomada"]))

    if fim == 'Avaliação presencial':
        insights_validos.append(random.choice(banco_insights["meta_parcial"]))

    random.shuffle(insights_validos)

    return insights_validos


cenarios = [
    {"desc": "Novo lead", "paciente": Lead("Davis Junior", "1199...", "davis@...", "555..."), "inicio": 'Lead recebido',
     "fim": 'Confirmação'},
    {"desc": "Retorno", "paciente": Lead("Ana Silva", "1199...", "ana@...", "111..."), "inicio": 'Orçamento',
     "fim": 'Confirmação'}
]

for c in cenarios:
    print(f"\nCenário: {c['desc']} ({c['paciente'].nome})")
    rota, custo = melhor_rota(fluxo_crm, c['inicio'], c['fim'])

    print(f"Rota: {' -> '.join(rota)} (Custo total: {custo})")

    insights = gerar_diagnostico_randomizado(rota, c['inicio'], c['fim'])
    if insights:
        print("Diagnóstico:")
        for i in insights:
            print(f"{i}")