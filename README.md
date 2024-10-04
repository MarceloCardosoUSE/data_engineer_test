## **Documentação Desafio Data**

Irei detalhar passo a Passo da Solução feita para esse Desafio!
desde ja agradeço a oportunidade.

### **Extração de dados**
A extração dos dados foi feita a 2 sites deixados no Desafio. Escolhi usar o do Censo Escolar de 2023 para obter dados das matrículas e site de benefícios para recebimento dos materiais escolares.

Fiz o Scraping do 2 Sites usando a biblioteca **Selenium**. A escolha desta biblioteca foi motivada pela necessidade de extrair dados apresentados em JavaScript, o que impossibilita o uso de outras bibliotecas como Beautiful Soup.
O primeiro site [QEdu](https://qedu.org.br/municipio/3550308-sao-paulo/censo-escolar) foi coletada informações sobre matrículas de alunos das creches,  pré-escola, anos iniciais: `1º  Ano ao 5º  Ano`, anos finais: `6º  Ano ao 9º  Ano` e o Ensino Médio, EJA e  Educação Especial!

O Segundo Site foi o [Portal de Uniformes](https://portaldeuniformes.sme.prefeitura.sp.gov.br/) Onde foram coletadas informações sobre os valores liberados e o público-alvo. 

Após a extração dos dados Brutos, foi gerado um CSV e JSON e foi armazenado na camada Bronze.

### **Arquitetura usada:** Medallion Architecture
[Imagem, exemplo da arquitetura:](/arquitetura.png)

### **Trasnformação dos Dados**
Foi utilizada a Medallion Architecture para extrair, transformar e carregar os dados deste projeto. Na estrutura do projeto, na pasta `/Data`, existem três camadas que armazenam os dados:

Camada Bronze: Armazena os dados brutos extraídos do web scraping.

Camada Silver: Contém os dados transformados, estruturados em DataFrames, com tabelas e colunas padronizadas. Nessa camada, também são realizadas a renomeação das colunas e a padronização dos dados.

Camada Gold:Armazena uma cópia do banco de dados SQLite, onde todos os dados estão tratados e prontos para uso. Nesta camada, também existem datasets que auxiliam o time de BI a consumir e criar visualizações.

A pasta `/scripts`: está com todos os arquivos contendo as transformações de dados.




### **Load dos Dados**

Foi desenvolvido um script para criar o banco de dados SQLite denominado test_engineer.db, que inclui as tabelas `beneficio` e `matriculas`. 
O Script está localizado em: `/scripts/create_database.py`

Após o tratamento dos dados, foi realizado o carregamento (load) em um banco de dados SQLite estruturado, também nomeado test_engineer.db.
O Script está localizado em:`/scripts/transform_gold.py`


