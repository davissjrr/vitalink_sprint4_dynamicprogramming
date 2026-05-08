# tarefa1_grafo.py

fluxo_crm = {
    'Lead recebido': {
        'Triagem': 1
    },
    'Triagem': {
        'Avaliação online': 2,
        'Avaliação presencial': 4
    },
    'Avaliação online': {
        'Orçamento': 1
    },
    'Avaliação presencial': {
        'Orçamento': 1
    },
    'Orçamento': {
        'Negociação': 3,
        'Confirmação': 6
    },
    'Negociação': {
        'Confirmação': 2
    },
    'Confirmação': {}
}