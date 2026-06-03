# 🗺️ Roadmap de Desenvolvimento — AI Data Insights

## 1. Planejamento

### Análise do desafio

* Leitura do documento do case técnico em formato PDF.
* Identificação do problema principal: transformar arquivos CSV em informações úteis para tomada de decisão.
* Levantamento das funcionalidades mínimas necessárias para um MVP funcional.

### Planejamento inicial

* Definição do escopo do projeto.
* Escolha da stack tecnológica.
* Estruturação inicial da arquitetura.
* Elaboração de um esboço de planejamento em papel para organizar ideias, prioridades e fluxo do sistema.

### Refinamento pós-primeira avaliação

* Revisão do planejamento inicial.
* Ajustes de escopo para manter foco no MVP.
* Priorização da experiência do usuário e da clareza da análise de dados.
* Definição de melhorias viáveis dentro do prazo disponível.

---

## 2. Desenvolvimento

### Estrutura base

* Criação do projeto em Python.
* Configuração do Streamlit.
* Organização da estrutura de arquivos.

### Manipulação de dados

* Implementação da leitura de arquivos CSV.
* Validação de arquivos enviados.
* Criação da visualização tabular utilizando Pandas.

### Análises automáticas

* Implementação das estatísticas descritivas.
* Geração de métricas básicas.
* Desenvolvimento dos insights automáticos baseados em regras.

### Visualização dos dados

* Implementação do gráfico de barras.
* Implementação do histograma para variáveis numéricas.

---

## 3. Integração da IA

### Estruturação da solução

* Escolha da API Gemini.
* Criação do módulo dedicado à IA.

### Preparação dos dados

* Conversão de estatísticas e amostras dos dados em contexto interpretável para o modelo.
* Construção e refinamento dos prompts.

### Otimização

* Implementação de botão para execução manual da IA.
* Redução de chamadas desnecessárias à API.
* Melhoria do controle de consumo de tokens.

---

## 4. Testes

### Testes funcionais

* Upload de diferentes arquivos CSV.
* Verificação da geração de gráficos.
* Validação das estatísticas apresentadas.

### Testes da IA

* Validação dos insights gerados.
* Ajustes no formato dos dados enviados ao modelo.
* Comparação entre respostas obtidas em diferentes cenários.

### Tratamento de erros

* Testes com arquivos inválidos.
* Testes com formatos diferentes de CSV.
* Verificação de mensagens de erro para o usuário.

---

## 5. Documentação

### Documentação técnica

* Criação do README.
* Descrição da arquitetura.
* Documentação da instalação e execução.

### Transparência no uso de IA

* Criação do documento "Uso da IA no Desenvolvimento".
* Registro das atividades realizadas com apoio de IA.
* Registro das decisões conduzidas pelo desenvolvedor.

### Demonstração

* Produção de capturas de tela da aplicação.
* Preparação do roteiro de apresentação.

---

## 6. Entrega

### Revisão final

* Verificação do funcionamento completo do sistema.
* Revisão da documentação.
* Revisão da organização do repositório.

### Publicação

* Atualização do GitHub.
* Organização dos arquivos finais.
* Disponibilização do código-fonte e materiais complementares.

### Apresentação

* Gravação do vídeo demonstrativo.
* Explicação do problema, solução, arquitetura e aprendizados obtidos durante o desenvolvimento.
