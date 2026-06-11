# 🗺️ Roadmap de Desenvolvimento — ChemInsights AI

## Visão geral

O **ChemInsights AI** é a evolução do projeto inicialmente chamado **AI Data Insights**.

A primeira versão consistia em um MVP genérico de análise de arquivos CSV, com upload, estatísticas, gráficos e interpretação por IA.

Após a primeira avaliação do processo seletivo, foi recebido o seguinte feedback:

> “Faça o app mais aplicado em conceitos avançados de química. Está muito genérico.”

A partir desse retorno, foi tomada a decisão de **não reconstruir o sistema do zero**.

A arquitetura funcional já existente foi reaproveitada e especializada para análise exploratória de dados químicos e laboratoriais.

---

# 1. Fase inicial — interpretação do desafio

## Objetivos

* Ler e compreender o documento do case técnico.
* Identificar as competências avaliadas.
* Definir um MVP executável dentro do prazo.
* Criar uma solução funcional, explicável e demonstrável.
* Evitar complexidade incompatível com o estágio inicial de aprendizado.

## Decisões tomadas

* Utilizar Python como linguagem principal.
* Utilizar Streamlit para construir a interface web.
* Utilizar Pandas para leitura e análise dos dados.
* Utilizar Plotly para as visualizações.
* Integrar uma IA generativa para interpretação complementar.
* Manter uma arquitetura simples e modular.

## Resultado

Foi definido o primeiro escopo do **AI Data Insights**:

```text
Upload de CSV
→ prévia dos dados
→ estatísticas
→ gráficos
→ insights automáticos
→ insights com IA
```

**Status:** concluído.

---

# 2. Primeiro MVP — AI Data Insights

## Funcionalidades implementadas

* Upload de arquivos CSV.
* Tentativas de leitura com diferentes separadores e codificações.
* Validação de arquivo vazio.
* Exibição do DataFrame.
* Quantidade de linhas e colunas.
* Identificação dos tipos de dados.
* Estatísticas numéricas.
* Gráfico de barras.
* Histograma.
* Gráfico de dispersão.
* Insights automáticos baseados em regras.
* Integração com a API Gemini.
* Uso de `st.session_state` para preservar respostas da IA.
* Modularização dos arquivos.

## Estrutura inicial

```text
app.py
utils/
├── charts.py
├── insights.py
└── ai_insights.py
```

## Resultado

Foi construído um MVP funcional de análise exploratória de dados.

Entretanto, a solução ainda era aplicável a praticamente qualquer dataset e não demonstrava suficientemente o domínio químico.

**Status:** concluído e posteriormente especializado.

---

# 3. Feedback e redefinição estratégica

## Feedback recebido

O principal retorno da avaliação foi que o sistema precisava aplicar conceitos mais avançados de química e deixar de ser genérico.

## Alternativas consideradas

### Criar um novo projeto

Vantagens:

* liberdade para redesenhar todo o sistema;
* arquitetura criada especificamente para química.

Desvantagens:

* maior risco técnico;
* perda de funcionalidades já validadas;
* aumento do retrabalho;
* prazo reduzido;
* necessidade de testar tudo novamente.

### Especializar o projeto existente

Vantagens:

* reaproveitamento da arquitetura;
* menor risco;
* preservação das funcionalidades prontas;
* demonstração de capacidade de adaptação;
* maior foco nas regras de domínio.

## Decisão

Foi escolhida a especialização do projeto existente.

O AI Data Insights foi transformado em:

# ⚗️ ChemInsights AI

Plataforma de análise exploratória de dados químicos e laboratoriais com cálculos determinísticos, regras químicas explícitas e interpretação complementar por IA.

**Status:** concluído.

---

# 4. Reposicionamento do produto

## Alterações realizadas

* Mudança do nome para ChemInsights AI.
* Atualização da identidade visual.
* Alteração da descrição da aplicação.
* Adaptação dos textos para o público químico.
* Inclusão dos contextos químicos disponíveis na sidebar.
* Mudança da proposta de valor do produto.

## Público-alvo considerado

* estudantes de Química;
* graduandos;
* químicos;
* pesquisadores;
* analistas laboratoriais;
* profissionais de controle de qualidade;
* profissionais de monitoramento ambiental.

## Princípio de produto

O sistema deveria utilizar conceitos técnicos e avançados, mas continuar acessível a usuários com pouca experiência em ciência de dados.

**Status:** concluído.

---

# 5. Especialização por contexto químico

Foram implementados quatro contextos de análise.

## 5.1 Química Analítica

Foco em:

* concentração;
* absorbância;
* espectrofotometria;
* curvas analíticas;
* regressão linear;
* Lei de Beer-Lambert;
* limitações da validação de métodos.

## 5.2 Cinética Química

Foco em:

* tempo de reação;
* consumo de reagentes;
* formação de produtos;
* variação da concentração;
* comportamento temporal;
* tendências cinéticas.

## 5.3 Controle de Qualidade

Foco em:

* comparação entre lotes;
* pH;
* condutividade;
* rendimento;
* dispersão;
* consistência;
* anomalias;
* limites de especificação.

## 5.4 Monitoramento Ambiental

Foco em:

* qualidade da água;
* pH;
* condutividade;
* salinidade;
* nitrato;
* fosfato;
* diferenças entre pontos de coleta;
* possíveis fontes de alteração ambiental.

**Status:** concluído.

---

# 6. Camada determinística de análise química

## Objetivo

Evitar que toda a lógica do sistema dependesse da IA generativa.

## Funcionalidades implementadas em Python

* identificação de colunas numéricas;
* média;
* mínimo;
* máximo;
* desvio padrão;
* correlação;
* regressão linear;
* inclinação;
* intercepto;
* coeficiente de determinação R²;
* validação básica do intervalo convencional de pH;
* reconhecimento da relação concentração–absorbância;
* reconhecimento da relação tempo–concentração;
* detecção de tendência crescente ou decrescente.

## Cuidados científicos incorporados

O sistema evita afirmar que:

* correlação prova causalidade;
* R² alto valida sozinho um método;
* linearidade define automaticamente a ordem da reação;
* um valor diferente representa necessariamente uma não conformidade;
* a ausência de limites permite classificar um resultado como aceitável.

**Status:** concluído.

---

# 7. Regressão linear e visualização didática

## Funcionalidades implementadas

* gráfico de dispersão;
* linha de tendência linear;
* equação estimada;
* inclinação;
* intercepto;
* R²;
* interpretação automática do sentido da tendência;
* classificação didática da qualidade do ajuste;
* explicações sobre os limites da interpretação.

## Objetivo pedagógico

O usuário não recebe apenas um valor numérico.

A interface explica:

* o que é a linha de tendência;
* o que significa a inclinação;
* o que representa o intercepto;
* como interpretar o R²;
* o que esses indicadores não permitem concluir.

**Status:** concluído.

---

# 8. Compatibilidade do dataset com o contexto

## Problema identificado

O usuário poderia escolher um contexto químico incompatível com as colunas do arquivo enviado.

Exemplo:

```text
Contexto: Cinética Química
Dataset: concentração e absorbância, sem tempo
```

## Solução implementada

Foi criado o módulo:

```text
utils/chemical_analysis.py
```

Responsável por:

* normalizar nomes de colunas;
* identificar variáveis químicas;
* verificar compatibilidade;
* apontar variáveis ausentes;
* orientar o usuário sem bloquear a análise.

## Comportamento

O sistema informa quando:

* o arquivo possui as variáveis esperadas;
* determinadas variáveis não foram identificadas;
* as conclusões podem ser limitadas.

**Status:** concluído.

---

# 9. Sugestão automática de eixos

## Objetivo

Reduzir erros na construção dos gráficos e orientar usuários menos experientes.

## Regras implementadas

### Química Analítica

```text
X = concentração
Y = absorbância
```

### Cinética Química

```text
X = tempo
Y = concentração
```

O usuário ainda pode alterar manualmente os eixos.

## Decisão de escopo

Não foram criadas sugestões obrigatórias para Controle de Qualidade e Monitoramento Ambiental, pois diferentes relações podem ser relevantes nesses contextos.

**Status:** concluído.

---

# 10. Integração com Gemini

## Objetivo

Utilizar a IA como camada complementar de interpretação, não como calculadora principal.

## Estrutura da resposta

A análise foi organizada em:

1. diagnóstico principal;
2. evidências observadas;
3. possíveis anomalias;
4. interpretação química;
5. próximos passos recomendados;
6. limitações.

## Regras adicionadas ao prompt

* não inventar valores;
* diferenciar observação, interpretação e hipótese;
* não afirmar causalidade apenas por correlação;
* não definir mecanismo ou ordem sem evidência;
* não validar método somente pelo R²;
* não declarar conformidade sem especificações;
* não declarar risco ambiental sem referências;
* informar quais dados adicionais seriam necessários.

**Status:** concluído.

---

# 11. Resiliência da integração com IA

## Problemas encontrados

Durante os testes, foram observados:

* modelo descontinuado;
* erro 404 de modelo inexistente;
* alta demanda com erro 503;
* limite de cota com erro 429;
* respostas vazias;
* mensagens técnicas extensas;
* preservação indevida de estado no Streamlit.

## Soluções implementadas

* atualização dos modelos utilizados;
* listagem dos modelos disponíveis;
* fallback entre modelos Gemini;
* tratamento diferenciado de erros;
* mensagens amigáveis para o usuário;
* detalhes técnicos mantidos apenas no terminal;
* manutenção das funcionalidades determinísticas quando a IA falha.

## Resultado

A indisponibilidade da IA não impede:

* upload;
* gráficos;
* estatísticas;
* regressão;
* validação do contexto;
* sugestão de eixos;
* insights determinísticos.

**Status:** concluído.

---

# 12. Testes e validação

## Cenários testados

### Química Analítica

* concentração × absorbância;
* tendência crescente;
* regressão linear;
* R² próximo de 1;
* interpretação associada à curva analítica.

### Cinética Química

* tempo × concentração;
* tendência decrescente;
* inclinação negativa;
* aviso sobre ordem e mecanismo.

### Controle de Qualidade

* comparação de lotes;
* pH;
* condutividade;
* rendimento;
* identificação de possíveis anomalias;
* ausência de declaração de conformidade sem limites.

### Monitoramento Ambiental

* salinidade;
* nitrato;
* fosfato;
* parâmetros físico-químicos;
* interpretação sem declarar contaminação definitiva.

## Outros testes

* CSV vazio;
* separadores diferentes;
* codificações diferentes;
* ausência de colunas numéricas;
* apenas uma coluna numérica;
* valores ausentes;
* troca de arquivo;
* troca de contexto;
* falha da API;
* cota excedida;
* indisponibilidade temporária.

**Status:** concluído.

---

# 13. Organização e documentação

## Materiais preparados

* README atualizado;
* roadmap de desenvolvimento;
* documento sobre uso da IA;
* capturas da versão final;
* evidências do planejamento inicial;
* arquivo `.env.example`;
* proteção da chave com `.gitignore`;
* organização dos módulos;
* requirements atualizado;
* vídeo demonstrativo gravado e publicado.

## Estrutura final

```text
cheminsight-ai/
├── app.py
├── README.md
├── ROADMAP.md
├── uso_da_IA.md
├── requirements.txt
├── .env.example
├── .gitignore
├── test_gemini.py
├── utils/
├── docs/
└── images/
```

**Status:** concluído.

---

# 14. Entrega

## Etapas concluídas

* [x] Concluir as funcionalidades do MVP.
* [x] Validar os quatro contextos químicos.
* [x] Organizar as imagens.
* [x] Atualizar o README.
* [x] Atualizar o roadmap.
* [x] Atualizar o documento `uso_da_IA.md`.
* [x] Revisar links e caminhos das imagens.
* [x] Gravar o novo vídeo demonstrativo.
* [x] Adicionar o novo vídeo ao README.

## Pendências finais

* [ ] Fazer a última revisão do repositório.
* [ ] Verificar se arquivos sensíveis estão protegidos.
* [ ] Criar o commit da versão final.
* [ ] Enviar as alterações ao GitHub.
* [ ] Conferir a entrega diretamente pelo GitHub.

**Status:** em finalização.

---

# 15. Melhorias futuras

As funcionalidades abaixo foram deliberadamente deixadas fora do MVP para reduzir riscos e preservar a estabilidade.

* análise automática da ordem de reação;
* comparação entre modelos cinéticos integrados;
* análise de resíduos;
* coeficiente de variação;
* detecção automática de outliers;
* boxplots;
* limites de especificação configuráveis;
* referências ambientais configuráveis;
* upload de Excel;
* exportação em PDF;
* geração de relatório;
* testes automatizados;
* deploy público;
* autenticação;
* banco de dados;
* armazenamento de análises anteriores;
* refatoração das seções da interface.

---

# Estado atual do projeto

```text
Planejamento              ✅ concluído
Primeiro MVP              ✅ concluído
Feedback recebido         ✅ incorporado
Especialização química    ✅ concluída
Regras determinísticas    ✅ concluídas
Regressão linear          ✅ concluída
Integração com IA         ✅ concluída
Fallback e erros          ✅ concluídos
Testes funcionais         ✅ concluídos
README                    ✅ atualizado
ROADMAP                   ✅ atualizado
Uso da IA                 ✅ atualizado
Novo vídeo                ✅ concluído
Revisão final             ✅ concluído
Commit final              ✅ concluído
Push para o GitHub        ✅ concluído
```

---

> O roadmap foi mantido como registro da evolução real do projeto: de um analisador genérico de CSV para uma plataforma de análise exploratória aplicada ao domínio químico.
