# 📚 Sistema de Boletim Escolar

Sistema em Python para cadastro e geração de boletins escolares, com controle de notas bimestrais e frequência por disciplina.

---

## 📋 Funcionalidades

- Cadastro de dados do estudante (nome, matrícula, número de bimestres)
- Lançamento de notas por disciplina e por bimestre (caderno, trabalho e prova)
- Validação automática de notas dentro dos limites permitidos
- Cálculo de soma anual e média bimestral
- Controle de faltas com cálculo de percentual de frequência
- Determinação automática do status final em cada disciplina
- Geração de boletim completo ao final do processo

---

## 🏫 Disciplinas

O sistema cobre as seguintes matérias:

- Português
- Matemática
- Geografia
- História
- Artes
- Educação Física

---

## 📊 Critérios de Avaliação

Cada bimestre é composto por três notas:

| Avaliação | Peso Máximo |
|-----------|-------------|
| Caderno   | 2,5 pontos  |
| Trabalho  | 2,5 pontos  |
| Prova     | 5,0 pontos  |
| **Total por bimestre** | **10,0 pontos** |

### Status Final

| Status | Critério |
|--------|----------|
| ✅ Aprovado | Soma anual ≥ 25 pontos |
| ⚠️ Recuperação | Média bimestral ≥ 6,0 |
| ❌ Reprovado por Nota | Nenhum critério de aprovação atingido |
| ❌ Reprovado por Faltas | Percentual de faltas > 60% |

---

## 🚀 Como Executar

**Pré-requisito:** Python 3.x instalado.

```bash
python project.py
```

Siga as instruções no terminal:

1. Informe os dados do estudante (nome, matrícula, número de bimestres e total de aulas)
2. Para cada disciplina, insira as notas de cada bimestre e o número de faltas
3. Ao final, o boletim completo será exibido no terminal

---

## 🗂️ Estrutura do Código

```
project.py
├── cadastro_estudante()      # Coleta dados básicos do estudante
├── cadastro_notas()          # Coleta notas e faltas por disciplina
├── calcular_notas()          # Calcula soma anual e média bimestral
├── calcular_frequencia()     # Calcula total e percentual de faltas
├── determinar_status()       # Define o status final na disciplina
└── gerar_relatorio()         # Exibe o boletim final formatado
```

---

## 💡 Exemplo de Saída

```
============================================================
BOLETIM FINAL: João Silva (ID: 12345)
============================================================

Matéria: Matemática
Notas Bimestrais: [8.5, 7.0, 9.0, 6.5]
Soma Anual de Pontos: 31.00 / 40.0
Média Bimestral: 7.75
Faltas: 5 ausências (6.3%)
Status Final: Aprovado
------------------------------------------------------------
```

---

## 🛠️ Tecnologias

- Python 3.x
- Biblioteca padrão (sem dependências externas)
