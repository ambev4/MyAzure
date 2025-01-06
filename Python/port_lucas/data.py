posts = {
        "descricao_pessoal": "Há 14 anos atuando no mercado de TI, \
        formado em Engenharia da Computação na faculdade Anhanguera em 2017.\
        Dediquei os últimos 3 anos em estudo de arquitetura de cloud AWS e Azure, \
        IaC (Terraform), Conteinerização de aplicações (Docker), Pipeline CI/CD (Git e Jenkins) e Python. \
        No ano de 2023 conquistei a certificação AWS Architect Associate e em \
        2024 a HashiCorp Terraform Associate. Busco manter um rítmo constante de aprendizado, \
        seja em novas tecnologias ou aprofundando ainda mais em conceitos já conhecidos.",
        
        "descricao_projeto": "Inicialmente, eu tinha pensado em uma estrutura mais conservadora para este portifólio, \
        com um ambiente de rede e EC2 na AWS servindo o conteúdo do site através de um Nginx de \
        forma monolítica. A estrutura toda seria criada e mantida por um script Terraform, \
        demonstrando o domínio da ferramenta. Porém esbarrei em algumas questões de custo \
        para manter este pequeno site rodando da forma que pensei inicialmente na AWS, ao lado \
        (ou acima se estiver vendo pelo celular) está o diagrama de como foi pensado e construído, \
        note que eu tinha intenção de criar mais coisas usando a mesma estrutura de rede. \
        Ao entrar neste dilema, precisei repensar na arquitetura e também na disponibilidade de \
        free tier oferecido pela AWS e por suas principais concorrentes, foi quando pesquisando \
        alternativas encontrei o service Container apps da Azure que encaixou perfeitamente pro \
        objetivo deste portifólio que é demonstrar domínio de tecnologias nas quais busco continuidade \
        e crescimento na carreira profissional.",
        
        "descricao_ambiente": "O projeto deste site tem como objetivo por em prática \
        os conhecimentos adquiridos principalmente no último ano de estudo alinhando estes \
        com a experiência profissional obtida no mercado ao longo da carreira. \
        ",

        "script_terraform": '''
        # Resource group do projeto
            resource "azurerm_resource_group" "myazure_rg" {
              name     = "myazure_rg"
              location = var.myazure_location
            }
            
            # Criação do ambiente de container apps
            resource "azurerm_container_app_environment" "myazure_app_env" {
              name                = "myazure-app-env"
              location            = var.myazure_location
              resource_group_name = azurerm_resource_group.myazure_rg.name
            }
            
            # Criação do container de backend
            resource "azurerm_container_app" "myazure_app_backend" {
              name                         = "myazure-app-backend"
              container_app_environment_id = azurerm_container_app_environment.myazure_app_env.id
              resource_group_name          = azurerm_resource_group.myazure_rg.name
              revision_mode                = "Single"
            
              template {
                container {
                  name   = "myazure-app-backend"
                  image  = "ambev4/lab1:myazure-backend"
                  cpu    = 0.25
                  memory = "0.5Gi"
                }
              }
            
              ingress {
                allow_insecure_connections = true
                external_enabled           = false
                target_port                = 8000
                traffic_weight {
                  percentage      = 100
                  latest_revision = true
                }
              }
            }
            
            # Criação do container Nginx com as imagens estáticas
            resource "azurerm_container_app" "myazure_app_nginx" {
              name                         = "myazure-app-nginx"
              container_app_environment_id = azurerm_container_app_environment.myazure_app_env.id
              resource_group_name          = azurerm_resource_group.myazure_rg.name
              revision_mode                = "Single"
            
              template {
                container {
                  name   = "myazure-app-nginx"
                  image  = "ambev4/lab1:myazure-nginx"
                  cpu    = 0.25
                  memory = "0.5Gi"
                }
              }
            
              ingress {
                allow_insecure_connections = true
                external_enabled           = true
                target_port                = 80
                traffic_weight {
                  percentage      = 100
                  latest_revision = true
                }
              }
            }
        ''',
        
        "descricao_terraform": "Este foi o script Terraform utilizado para \
        criação e atualização do ambiente citado acima, tudo o que está rodando \
        na AWS neste momento é mantido e atualizado diretamente nele, \
        com excessão da regra SSH para meu IP pessoal, além dele existe um outro \
        arquivo de variáveis que utilizei para definição de nomes e de outros \
        tipos de configuração",
        
        
}