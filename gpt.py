import json

# Dados da vaga (exemplo)
job_requirements = {
    "experience_years": 3,  # Anos de experiência necessários
    "skills": ["Python", "Machine Learning", "SQL"],  # Habilidades obrigatórias
}

# Função para avaliar um único candidato
def evaluate_candidate(candidate, job_requirements):
    # Inicializar justificativa
    justification = []

    # Avaliar anos de experiência
    if candidate["experience_years"] >= job_requirements["experience_years"]:
        experience_score = True
    else:
        experience_score = False
        justification.append(
            f"Experiência insuficiente: {candidate['experience_years']} anos (mínimo: {job_requirements['experience_years']} anos)."
        )

    # Avaliar habilidades
    required_skills = set(job_requirements["skills"])
    candidate_skills = set(candidate["skills"])
    missing_skills = required_skills - candidate_skills

    if not missing_skills:
        skills_score = True
    else:
        skills_score = False
        justification.append(f"Faltam as seguintes habilidades: {', '.join(missing_skills)}.")

    # Decisão final
    if experience_score and skills_score:
        status = "Aprovado"
    elif experience_score or len(candidate_skills.intersection(required_skills)) > 0:
        status = "Aprovado parcialmente"
    else:
        status = "Reprovado"

    return {
        "name": candidate["name"],
        "status": status,
        "justification": justification or ["Atende todos os critérios exigidos."],
    }

# Função para avaliar todos os candidatos
def evaluate_all_candidates(candidates, job_requirements):
    results = []
    for candidate in candidates:
        result = evaluate_candidate(candidate, job_requirements)
        results.append(result)
    return results

# Função para carregar candidatos de um arquivo JSON
def load_candidates_from_file(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Carregar dados dos candidatos
candidates = load_candidates_from_file("candidates.json")

# Avaliar candidatos
results = evaluate_all_candidates(candidates, job_requirements)

# Exibir resultados
for result in results:
    print(f"Nome: {result['name']}")
    print(f"Status: {result['status']}")
    print("Justificativa:")
    for reason in result["justification"]:
        print(f"  - {reason}")
    print("-" * 50)
