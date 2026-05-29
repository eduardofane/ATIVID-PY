


# FUNÇÃO 1: CADASTRO DE DADOS DO ESTUDANTE
# ============================================================
def cadastro_estudante():
    """
    Coleta as informações básicas do estudante.
    
    Retorna: dicionário com nome, matrícula, número de bimestres e total de aulas
    """
    nome = input('Nome do estudante: ')
    matricula = int(input('Digite a matricula: '))
    num_bimestres = int(input('Digite quantos bimestres quer (1 a 4): '))
    aulas_totais = int(input('Digite o total de aulas no período (ex: 80, 200): '))
    
    return {
        'nome': nome,
        'matricula': matricula,
        'num_bimestres': num_bimestres,
        'aulas_totais': aulas_totais
    }



# FUNÇÃO 2: CADASTRO DE NOTAS E FALTAS POR DISCIPLINA
# ============================================================
def cadastro_notas(disciplina, num_bimestres):
    """
    Coleta as notas (caderno, trabalho, prova) e faltas de uma disciplina.
    
    Argumentos:
        - disciplina: nome da disciplina
        - num_bimestres: quantidade de bimestres
    
    Retorna: tuple com (lista de notas, lista de faltas)
    """
    notas_por_bimestre = []
    faltas_por_bimestre = []
    bimestres = ['bimestre 1', 'bimestre 2', 'bimestre 3', 'bimestre 4']
    
    print(f"\n--- Lançando notas de: {disciplina} ---")
    
    for j in range(num_bimestres):
        print(f"\n> {bimestres[j]}")
        
        # Coleta nota do caderno (máximo 2.5)
        while True:
            nota1 = float(input('  Caderno (max 2.5): '))
            if 0 <= nota1 <= 2.5: 
                break
            print("  Erro! A nota deve ser entre 0 e 2.5")

        # Coleta nota do trabalho (máximo 2.5)
        while True:
            nota2 = float(input('  Trabalho (max 2.5): '))
            if 0 <= nota2 <= 2.5: 
                break
            print("  Erro! A nota deve ser entre 0 e 2.5")

        # Coleta nota da prova (máximo 5.0)
        while True:
            nota3 = float(input('  Prova (max 5.0): '))
            if 0 <= nota3 <= 5.0: 
                break
            print("  Erro! A nota deve ser entre 0 e 5.0")
        
        # Coleta quantidade de faltas
        falta = int(input(f'  Faltas no {bimestres[j]}: '))
        faltas_por_bimestre.append(falta)
        
        # Soma as notas do bimestre
        soma_bimestre = nota1 + nota2 + nota3
        notas_por_bimestre.append(soma_bimestre)
        print(f"  Total do bimestre: {soma_bimestre:.2f}")
    
    return notas_por_bimestre, faltas_por_bimestre



# FUNÇÃO 3: CÁLCULO DE NOTAS (SOMA ANUAL E MÉDIA)
# ============================================================
def calcular_notas(notas_por_bimestre):
    """
    Calcula a soma anual e a média bimestral de notas.
    
    Argumentos:
        - notas_por_bimestre: lista com a soma de notas de cada bimestre
    
    Retorna: tuple com (soma_anual, media_bimestral)
    """
    soma_anual = sum(notas_por_bimestre)
    num_bimestres = len(notas_por_bimestre)
    media_bimestral = soma_anual / num_bimestres if num_bimestres > 0 else 0
    
    return soma_anual, media_bimestral


# FUNÇÃO 4: CÁLCULO DE FREQUÊNCIA (FALTAS E PERCENTUAL)
# ============================================================
def calcular_frequencia(faltas_por_bimestre, aulas_totais):
    """
    Calcula o total de faltas e o percentual de faltas.
    
    Argumentos:
        - faltas_por_bimestre: lista com faltas de cada bimestre
        - aulas_totais: total de aulas no período
    
    Retorna: tuple com (total_faltas, percentual_faltas)
    """
    total_faltas = sum(faltas_por_bimestre)
    
    if aulas_totais > 0:
        percentual_faltas = (total_faltas / aulas_totais) * 100
    else:
        percentual_faltas = 0
    
    return total_faltas, percentual_faltas


# FUNÇÃO 5: DETERMINAÇÃO DE STATUS (APROVADO/REPROVADO)
# ============================================================
def determinar_status(soma_anual, media_bimestral, percentual_faltas):
    """
    Determina o status final do estudante em uma disciplina.
    
    Critérios:
        - Reprovado por Faltas: se faltas > 60%
        - Aprovado: se soma_anual >= 25
        - Recuperação: se media_bimestral >= 5.0
        - Reprovado por Nota: se nenhum critério é atendido
    
    Argumentos:
        - soma_anual: soma total de notas do ano
        - media_bimestral: média de notas por bimestre
        - percentual_faltas: percentual de faltas
    
    Retorna: string com o status
    """
    if percentual_faltas > 60:
        status = "Reprovado por Faltas"
    elif soma_anual >= 25:
        status = "Aprovado"
    elif media_bimestral >= 6.0:
        status = "Recuperação"
    else:
        status = "Reprovado por Nota"
    
    return status



# FUNÇÃO 6: GERAÇÃO E EXIBIÇÃO DO RELATÓRIO
# ============================================================
def gerar_relatorio(estudante_info, historico_escolar):
    """
    Exibe o boletim final com todos os dados do estudante.
    
    Argumentos:
        - estudante_info: dicionário com dados do estudante
        - historico_escolar: lista de boletins de cada disciplina
    
    Retorna: nada (apenas imprime)
    """
    print("\n" + "="*60)
    print(f"BOLETIM FINAL: {estudante_info['nome']} (ID: {estudante_info['matricula']})")
    print("="*60)
    
    for item in historico_escolar:
        print(f"\nMatéria: {item['Disciplina']}")
        print(f"Notas Bimestrais: {item['Notas']}")
        print(f"Soma Anual de Pontos: {item['Soma_Anual']:.2f} / 40.0")
        print(f"Média Bimestral: {item['Media_Bimestral']:.2f}")
        print(f"Faltas: {item['Total_Faltas']} ausências ({item['Percentual_Faltas']:.1f}%)")
        print(f"Status Final: {item['Status']}")
        print("-" * 60)


# PROGRAMA PRINCIPAL
# ============================================================
if __name__ == "__main__":
    # Lista de disciplinas
    materias = ['Português', 'Matemática', 'Geografia', 'História', 'Artes', 'Educação Física']
    
    # PASSO 1: Cadastro do estudante
    estudante_info = cadastro_estudante()
    
    # PASSO 2: Processamento de cada disciplina
    historico_escolar = []
    
    for disciplina in materias:
        # Coleta notas e faltas da disciplina
        notas, faltas = cadastro_notas(disciplina, estudante_info['num_bimestres'])
        
        # Calcula soma anual e média de notas
        soma_anual, media_bimestral = calcular_notas(notas)
        
        # Calcula total e percentual de faltas
        total_faltas, percentual_faltas = calcular_frequencia(faltas, estudante_info['aulas_totais'])
        
        # Determina o status na disciplina
        status = determinar_status(soma_anual, media_bimestral, percentual_faltas)
        
        # Monta o dicionário com todos os dados da disciplina
        boletim = {
            'Disciplina': disciplina,
            'Notas': notas,
            'Soma_Anual': soma_anual,
            'Media_Bimestral': media_bimestral,
            'Total_Faltas': total_faltas,
            'Percentual_Faltas': percentual_faltas,
            'Status': status
        }
        
        historico_escolar.append(boletim)
    
    # PASSO 3: Gera e exibe o relatório final
    gerar_relatorio(estudante_info, historico_escolar)
