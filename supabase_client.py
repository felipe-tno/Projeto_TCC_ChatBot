from supabase import create_client, Client

# 🔧 Substitua abaixo com suas credenciais
url = "https://SEU_URL_SUPABASE.supabase.co"
key = "SUA_CHAVE_API_SUPABASE"
supabase: Client = create_client(url, key)

def inserir_gasto(usuario_id, descricao, valor, categoria):
    try:
        data = {
            "usuario_id": usuario_id,
            "descricao": descricao,
            "valor": valor,
            "categoria": categoria
        }
        res = supabase.table("gastos").insert(data).execute()
        return res
    except Exception as e:
        print("Erro ao inserir no Supabase:", e)
        return None

def listar_gastos(usuario_id):
    try:
        data = supabase.table("gastos").select("*").eq("usuario_id", usuario_id).execute()
        return data.data
    except Exception as e:
        print("Erro ao listar gastos:", e)
        return []
