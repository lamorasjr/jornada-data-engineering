# Workshop: Infra, Linux e Docker

- **Principais Comandos**
    - `docker pull <imagem>` - carrega uma imagem do docker hub
    - `docker images`
    - `docker ps` ou `docker ps -a` - visualizar os containers
    - `docker stop <container id>` - para um container
    - `docker rm <container id>` - remove um container
- **Por que utilizar Docker?**
    - **Qual foi o cenário que gerou o Docker?**
        - “Mas na minha máquina roda …”
    - **Rodar o Docker na máquina local**
        - Baixar e instalar via site oficial
- **Deploy de um Docker na AWS EC2 e no Render**
    
    **Passo 1 - Desenvolver o app and rodar o docker Build**
    
    - `docker build -t minha-primeira-imagem`
    - `docker run -d -p 8501:8501 —name meu-primeiro-container minha-primeira-imagem`
    
    **Passo 2 - Enviar para o Render (Ambiente de QA)**
    
    **Passo 3 - Enviar para o AWS (Ambiente Prod)**
    
    - Passo a passo do deploy:
        - sudo yum update -y
        - sudo youm install docker -y
        - sudo usermod -a -G docker ec2-user
        - newgrp docker
        - sudo service docker start
        - sudo systemctl enable docker
        - sudo docker run hello-world
        - sudo yum install git -y
        - git clone <repo-git>
        - cd <repo-git>
        - sudo docker build -t minha-primeira-imagem .
        - sudo docker run -d -p 8501:8501 —name meu-primeiro-container minha-primeira-imagem
        - sudo docker ps
- **Docker Compose**
    - Utilizado quando necessário subir um app que roda +1 docker image ao mesmo tempo