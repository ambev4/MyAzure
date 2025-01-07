from pathlib import Path

TERRAFORM_FOLDER = Path(__file__).parent.parent.parent
TERRAFORM_FILE = TERRAFORM_FOLDER / 'Terraform' / 'main.tf'
script_terraform =''

with open(TERRAFORM_FILE, 'r', encoding='utf-8') as arquivo:
    script_terraform_file = arquivo.readlines()

    for line in script_terraform_file:
        line += ' '
        script_terraform += line


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
        os conhecimentos adquiridos principalmente nos últimos anos de estudo alinhando estes \
        com a experiência profissional obtida no mercado ao longo da carreira. Este front é um HTML e CSS \
        básicos que escrevi do zero para demonstrar e descrever a estrutura por trás que ele possui já que \
        frontend não é a minha praia. Uma das coisas que mais gostei deste desafio foi a busca por eficiência, \
        escalabilidade, automação e redução de custos. Eu realmente levei estas coisas bem a sério neste pequeno \
        site, procurei criar algo mais caprichado e limpo que eu conseguisse e o resultado foi muito positivo. \
        Como dito anteriormente, este app roda no Azure Container Apps em dois containers separados, um Nginx \
        como proxy reverso e também servidor de imagens e CSS e o segundo como backend com os códigos Python, \
        Django e toda a parte lógica rodando nele de forma inacessível externamente. Investi um bom tempo enxugando \
        todo o código e as Dockerfiles com o objetivo de deixar tudo o mais enxuto e eficiente possível. Também \
        desenvolvi pipelines CI/CD no Jenkins e Git para busca, empacotamento, teste, criação das imagens Docker \
        e upload no Registry de forma automática e estável. E por fim, a estrutura na Azure com os containers \
        foram criados por script Terraform. Lembrando que todo o código deste projeto incluindo Dockerfiles, \
        scripts Terraform e pipelines do jenkins estão públicos no meu GitHub.",

        "script_terraform": script_terraform,
        
        "descricao_terraform": "Este foi o script Terraform utilizado para criar os recursos na Cloud Azure, \
        ele também está disponibilizado no GitHub. A infraestrutura necessária para rodar os containers foi \
        muito menor e mais simples em comparação ao primeiro projeto na AWS, aonde existia subnets, security_groups, \
        VMs e toda uma lógica para executar comandos dentro das EC2 para subir a aplicação de forma automatizada. \
        Futuramente pretendo implantar uma infraestrutura um pouco mais complexa dentro das limitações do free \
        tier da Azure, conforme for fazendo modificações no ambiente elas serão refletidas neste quadro de forma \
        automatizada buscando diretamente a versão utilizada em \"produção\".  ",
        
}