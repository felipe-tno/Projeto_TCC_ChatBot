**Projeto MoneyMate**

Este repositório contém uma aplicação web em Flask chamada `moneymate_web.py` que usa Supabase para persistência e a API Groq para interpretar mensagens de gastos em português.

**Pré-requisitos**:
- **Python 3.10+**: instale do site oficial ou use gerenciador de pacotes.
- **pip**: para instalar dependências.
- Uma conta Supabase e uma tabela para `gastos` e `orcamentos` (veja SQL de exemplo abaixo).
- Chaves de API: `SUPABASE_URL`, `SUPABASE_KEY`, `GROQ_API_KEY`.

**Arquivos importantes**:
- `moneymate_web.py`: aplicação Flask principal.
- `requirements.txt`: dependências Python.
- `credenciais.env`: arquivo com variáveis de ambiente (não comitar no repositório).
- `templates/index.html`, `static/`: assets do frontend.

**Configurar variáveis (arquivo `credenciais.env`)**
Crie um arquivo chamado `credenciais.env` na raiz do projeto com o conteúdo (exemplo):

```
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=eyJ...sua_chave
GROQ_API_KEY=sk-...sua_chave_groq
```

Mantenha esse arquivo privado e não o compartilhe publicamente.

**Instalação (PowerShell)**
```
python -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
```

Observação: se estiver usando outra shell, adapte os comandos de ativação conforme a plataforma.

**Executar a aplicação**
```
python moneymate_web.py
```
Por padrão a aplicação roda em `http://127.0.0.1:5000` com `debug=True`.

Abra o navegador em `http://127.0.0.1:5000` para usar a interface.

**Testes manuais (exemplos de requisições)**
- Enviar mensagens (usar um `UUID` como primeiro envio para registrar o usuário):

PowerShell (exemplo):
```
Invoke-RestMethod -Method Post -Uri 'http://127.0.0.1:5000/mensagem' -ContentType 'application/json' -Body '{"texto":"seu-uuid-aqui"}'
Invoke-RestMethod -Method Post -Uri 'http://127.0.0.1:5000/mensagem' -ContentType 'application/json' -Body '{"texto":"Uber 25 reais"}'
```

- Definir ou atualizar orçamento (exemplo):
```
Invoke-RestMethod -Method Post -Uri 'http://127.0.0.1:5000/definir_orcamento' -ContentType 'application/json' -Body '{"categoria":"alimentacao","valor":200}'
```

- Listar gastos do usuário (GET):
```
Invoke-RestMethod -Method Get -Uri 'http://127.0.0.1:5000/gastos'
```

As requisições acima retornam JSON com a resposta do bot e/ou conteúdo salvo no Supabase.

**Tabelas Supabase (exemplo SQL)**
Use o SQL editor do Supabase para criar as tabelas mínimas esperadas.

Tabela `gastos` (exemplo):
```
create table gastos (
  id serial primary key,
  id_usuario uuid,
  descricao text,
  valor numeric,
  categoria text,
  criado_em timestamp with time zone default timezone('utc'::text, now())
);
```

Tabela `orcamentos` (exemplo):
```
create table orcamentos (
  id_orcamento serial primary key,
  id_usuario uuid,
  categoria text,
  limite_mensal numeric,
  criado_em timestamp with time zone default timezone('utc'::text, now())
);
```

**Comportamento e notas**
- Ao iniciar, a aplicação carrega `credenciais.env`. Se as variáveis não estiverem definidas, o app irá levantar uma exceção.
- A lógica de interpretação de texto usa a API Groq; se a IA não tiver certeza sobre categoria/valor, ela pede confirmação ao usuário e mantém o gasto em `usuarios["gasto_pendente"]`.
- As categorias esperadas: `alimentacao`, `lazer`, `saude`, `transporte`, `entretenimento`, `moradia`, `outros`.

**Resolução de problemas comuns**
- Erro: "SUPABASE_URL ou SUPABASE_KEY não encontrados": verifique `credenciais.env` e se o arquivo está na raiz.
- Erro: "GROQ_API_KEY não encontrado": defina a variável no `credenciais.env`.
- Se a aplicação não conseguir salvar no Supabase, verifique a URL/KEY e permissões das tabelas.

**Próximos passos sugeridos**
- Adicionar testes automatizados (pytest) para endpoints.
- Adicionar validação/normalização de UUID no frontend antes do envio.

Se quiser, eu posso: (1) criar um script de inicialização (`scripts/run.ps1`), (2) adicionar um exemplo `.env.example`, ou (3) criar testes básicos com `pytest`.

*** Obrigado! ***
