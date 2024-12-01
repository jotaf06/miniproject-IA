import json

# Dados da vaga (exemplo)
job_requirements = {
    "experience_years": 3,  # Anos de experiência necessários
    "skills": ["Python", "Machine Learning", "SQL"],  # Habilidades obrigatórias
}

# Função para avaliar um único candidato
def evaluate_candidate(candidate, job_requirements):
    """
    Avalia um candidato com base nos requisitos da vaga.

    Args:
        candidate: Dicionário com informações do candidato.
        job_requirements: Dicionário com os requisitos da vaga, incluindo habilidades e níveis de proficiência.

    Returns:
        Dicionário com o resultado da avaliação e a justificativa.
    """

    # Definir pesos para as habilidades (ajustável)
    skill_weights = {"Python": 3, "Machine Learning": 2, "SQL": 1}

    # Definir níveis de proficiência (ajustável)
    proficiency_levels = ["básico", "intermediário", "avançado"]

    # Inicializar a justificativa e o score
    justification = []
    total_score = 0

    # Avaliar a experiência
    # ... (código similar ao original)

    # Avaliar as habilidades
    candidate_skills = set(candidate["skills"])
    required_skills = set(job_requirements["skills"])
    missing_skills = required_skills - candidate_skills

    # Calcular o score de habilidades com base nos pesos e níveis de proficiência
    for skill, required_level in job_requirements["skills"].items():
        if skill in candidate_skills:
            # Simular a obtenção do nível de proficiência do candidato (a ser substituído por uma lógica mais robusta)
            candidate_level = "intermediário" if candidate["experience_years"] > 2 else "básico"

            if proficiency_levels.index(candidate_level) >= proficiency_levels.index(required_level):
                skill_score = skill_weights.get(skill, 0)
                total_score += skill_score
            else:
                justification.append(f"Nível de proficiência em {skill} insuficiente (requerido: {required_level}, candidato: {candidate_level}).")
        else:
            justification.append(f"Falta a habilidade: {skill}.")

    # Avaliar o score total e definir o status
    if total_score >= 80:  # Ajustar o threshold conforme necessário
        status = "Aprovado"
    elif total_score >= 60:
        status = "Aprovado parcialmente"
    else:
        status = "Reprovado"

    return {
        "name": candidate["name"],
        "status": status,
        "justification": justification,
        "total_score": total_score
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
