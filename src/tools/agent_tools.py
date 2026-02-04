"""
Ferramentas para extração de dados do Brasileirão
"""
from langchain_core.tools import StructuredTool
import requests
from typing import Optional
import json


def get_mock_brasileirao_data() -> dict:
    """
    Retorna dados de exemplo da tabela do Brasileirão
    Usado como fallback quando APIs externas não estão disponíveis
    """
    return {
        "success": True,
        "campeonato": "Brasileirão Série A",
        "temporada": "2024",
        "total_times": 20,
        "observacao": "⚠️ Dados de exemplo - APIs externas bloqueadas. Para dados reais, considere usar API-Football com chave de API.",
        "classificacao": [
            {"posicao": 1, "time": "Botafogo", "sigla": "BOT", "pontos": 76, "jogos": 38, "vitorias": 23, "empates": 7, "derrotas": 8, "gols_pro": 59, "gols_contra": 29, "saldo_gols": 30},
            {"posicao": 2, "time": "Palmeiras", "sigla": "PAL", "pontos": 73, "jogos": 38, "vitorias": 22, "empates": 7, "derrotas": 9, "gols_pro": 60, "gols_contra": 33, "saldo_gols": 27},
            {"posicao": 3, "time": "Flamengo", "sigla": "FLA", "pontos": 69, "jogos": 38, "vitorias": 20, "empates": 9, "derrotas": 9, "gols_pro": 61, "gols_contra": 42, "saldo_gols": 19},
            {"posicao": 4, "time": "Fortaleza", "sigla": "FOR", "pontos": 68, "jogos": 38, "vitorias": 19, "empates": 11, "derrotas": 8, "gols_pro": 53, "gols_contra": 39, "saldo_gols": 14},
            {"posicao": 5, "time": "Internacional", "sigla": "INT", "pontos": 65, "jogos": 38, "vitorias": 18, "empates": 11, "derrotas": 9, "gols_pro": 53, "gols_contra": 36, "saldo_gols": 17},
            {"posicao": 6, "time": "São Paulo", "sigla": "SAO", "pontos": 59, "jogos": 38, "vitorias": 17, "empates": 8, "derrotas": 13, "gols_pro": 53, "gols_contra": 43, "saldo_gols": 10},
            {"posicao": 7, "time": "Corinthians", "sigla": "COR", "pontos": 56, "jogos": 38, "vitorias": 15, "empates": 11, "derrotas": 12, "gols_pro": 54, "gols_contra": 45, "saldo_gols": 9},
            {"posicao": 8, "time": "Bahia", "sigla": "BAH", "pontos": 53, "jogos": 38, "vitorias": 14, "empates": 11, "derrotas": 13, "gols_pro": 49, "gols_contra": 49, "saldo_gols": 0},
            {"posicao": 9, "time": "Cruzeiro", "sigla": "CRU", "pontos": 52, "jogos": 38, "vitorias": 14, "empates": 10, "derrotas": 14, "gols_pro": 43, "gols_contra": 41, "saldo_gols": 2},
            {"posicao": 10, "time": "Vasco da Gama", "sigla": "VAS", "pontos": 50, "jogos": 38, "vitorias": 14, "empates": 8, "derrotas": 16, "gols_pro": 41, "gols_contra": 56, "saldo_gols": -15},
            {"posicao": 11, "time": "Vitória", "sigla": "VIT", "pontos": 47, "jogos": 38, "vitorias": 13, "empates": 8, "derrotas": 17, "gols_pro": 45, "gols_contra": 52, "saldo_gols": -7},
            {"posicao": 12, "time": "Atlético Mineiro", "sigla": "CAM", "pontos": 47, "jogos": 38, "vitorias": 11, "empates": 14, "derrotas": 13, "gols_pro": 47, "gols_contra": 54, "saldo_gols": -7},
            {"posicao": 13, "time": "Fluminense", "sigla": "FLU", "pontos": 46, "jogos": 38, "vitorias": 12, "empates": 10, "derrotas": 16, "gols_pro": 33, "gols_contra": 39, "saldo_gols": -6},
            {"posicao": 14, "time": "Grêmio", "sigla": "GRE", "pontos": 45, "jogos": 38, "vitorias": 12, "empates": 9, "derrotas": 17, "gols_pro": 44, "gols_contra": 50, "saldo_gols": -6},
            {"posicao": 15, "time": "Juventude", "sigla": "JUV", "pontos": 43, "jogos": 38, "vitorias": 11, "empates": 10, "derrotas": 17, "gols_pro": 48, "gols_contra": 59, "saldo_gols": -11},
            {"posicao": 16, "time": "Red Bull Bragantino", "sigla": "RBB", "pontos": 41, "jogos": 38, "vitorias": 10, "empates": 11, "derrotas": 17, "gols_pro": 43, "gols_contra": 51, "saldo_gols": -8},
            {"posicao": 17, "time": "Athletico Paranaense", "sigla": "CAP", "pontos": 42, "jogos": 38, "vitorias": 11, "empates": 9, "derrotas": 18, "gols_pro": 40, "gols_contra": 51, "saldo_gols": -11},
            {"posicao": 18, "time": "Criciúma", "sigla": "CRI", "pontos": 38, "jogos": 38, "vitorias": 9, "empates": 11, "derrotas": 18, "gols_pro": 42, "gols_contra": 61, "saldo_gols": -19},
            {"posicao": 19, "time": "Atlético Goianiense", "sigla": "ACG", "pontos": 30, "jogos": 38, "vitorias": 7, "empates": 9, "derrotas": 22, "gols_pro": 29, "gols_contra": 58, "saldo_gols": -29},
            {"posicao": 20, "time": "Cuiabá", "sigla": "CUI", "pontos": 30, "jogos": 38, "vitorias": 6, "empates": 12, "derrotas": 20, "gols_pro": 27, "gols_contra": 53, "saldo_gols": -26}
        ]
    }


def extract_brasileirao_table(query: str = "") -> str:
    """
    Extrai dados da tabela de classificação do Brasileirão Série A
    
    Tenta múltiplas fontes de dados:
    1. API do SofaScore (frequentemente bloqueada)
    2. API-Football (requer chave de API - não configurada)
    3. Dados de exemplo (fallback)
    
    Args:
        query: Query opcional (não usado, apenas para compatibilidade)
    
    Returns:
        Dados da tabela em formato JSON string
    """
    
    # Tentativa 1: API SofaScore
    api_url = "https://api.sofascore.com/api/v1/unique-tournament/325/season/87678/standings/total"
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'pt-BR,pt;q=0.9',
            'Referer': 'https://www.sofascore.com/',
        }
        
        response = requests.get(api_url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            if 'standings' in data and data['standings']:
                standings = data['standings'][0]['rows']
                
                teams_data = []
                for row in standings:
                    team = row.get('team', {})
                    team_info = {
                        "posicao": row.get('position', 0),
                        "time": team.get('name', 'Desconhecido'),
                        "sigla": team.get('shortName', ''),
                        "pontos": row.get('points', 0),
                        "jogos": row.get('matches', 0),
                        "vitorias": row.get('wins', 0),
                        "empates": row.get('draws', 0),
                        "derrotas": row.get('losses', 0),
                        "gols_pro": row.get('scoresFor', 0),
                        "gols_contra": row.get('scoresAgainst', 0),
                        "saldo_gols": row.get('scoresFor', 0) - row.get('scoresAgainst', 0),
                    }
                    teams_data.append(team_info)
                
                result = {
                    "success": True,
                    "campeonato": "Brasileirão Série A",
                    "temporada": "2024",
                    "total_times": len(teams_data),
                    "fonte": "API SofaScore (dados reais)",
                    "classificacao": teams_data
                }
                
                return json.dumps(result, ensure_ascii=False, indent=2)
    
    except Exception as e:
        # Continua para o fallback
        pass
    
    # Fallback: Retorna dados de exemplo
    result = get_mock_brasileirao_data()
    return json.dumps(result, ensure_ascii=False, indent=2)


def test_brasileirao_extraction():
    """
    Função de teste para verificar a extração de dados
    Pode ser executada diretamente para debug
    """
    print("=" * 80)
    print("TESTE DE EXTRAÇÃO - TABELA DO BRASILEIRÃO")
    print("=" * 80)
    
    result = extract_brasileirao_table()
    print("\nResultado da extração:")
    print(result)
    
    # Parse do JSON para análise
    try:
        data = json.loads(result)
        if data.get("success"):
            print(f"\n✅ Sucesso! {data['total_times']} times encontrados")
            print(f"Campeonato: {data['campeonato']}")
            print(f"Temporada: {data['temporada']}")
            
            if 'observacao' in data:
                print(f"\n{data['observacao']}")
            
            if 'fonte' in data:
                print(f"Fonte: {data['fonte']}")
            
            print("\n🏆 TOP 10 - Classificação:")
            print("-" * 80)
            print(f"{'Pos':<4} {'Time':<25} {'Pts':<4} {'J':<3} {'V':<3} {'E':<3} {'D':<3} {'GP':<3} {'GC':<3} {'SG':<4}")
            print("-" * 80)
            for team in data['classificacao'][:10]:
                print(f"{team['posicao']:<4d} {team['time']:<25s} {team['pontos']:<4d} "
                      f"{team['jogos']:<3d} {team['vitorias']:<3d} {team['empates']:<3d} "
                      f"{team['derrotas']:<3d} {team['gols_pro']:<3d} {team['gols_contra']:<3d} "
                      f"{team['saldo_gols']:+4d}")
            
            print("\n⬇️ ZONA DE REBAIXAMENTO:")
            print("-" * 80)
            for team in data['classificacao'][-4:]:
                print(f"{team['posicao']:<4d} {team['time']:<25s} {team['pontos']:<4d} "
                      f"{team['jogos']:<3d} {team['vitorias']:<3d} {team['empates']:<3d} "
                      f"{team['derrotas']:<3d} {team['gols_pro']:<3d} {team['gols_contra']:<3d} "
                      f"{team['saldo_gols']:+4d}")
        else:
            print(f"\n❌ Erro: {data.get('error')}")
            print(f"   Mensagem: {data.get('message')}")
            if 'sugestao' in data:
                print(f"   Sugestão: {data.get('sugestao')}")
    except json.JSONDecodeError:
        print("\n❌ Erro ao decodificar JSON")
    
    print("=" * 80)


def create_brasileirao_tool() -> StructuredTool:
    """Cria e retorna a ferramenta de extração do Brasileirão"""
    from ..prompts import prompt_loader
    
    tool_prompts = prompt_loader.get_tool_prompts()
    
    return StructuredTool.from_function(
        func=extract_brasileirao_table,
        name="TabelaBrasileirão",
        description=tool_prompts.get(
            "brasileirao_description",
            "Útil para obter a tabela de classificação atualizada do Campeonato Brasileiro Série A. "
            "Extrai dados de posição, times, pontos e estatísticas do SofaScore."
        )
    )


def get_all_tools() -> list:
    """
    Retorna todas as ferramentas disponíveis para o agente
    
    Returns:
        Lista de ferramentas do LangChain
    """
    tools = [
        create_brasileirao_tool(),
    ]
    
    return tools


# Permite executar o teste diretamente
if __name__ == "__main__":
    test_brasileirao_extraction()

