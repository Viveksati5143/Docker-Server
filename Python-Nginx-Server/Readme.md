# Creating a reverse proxy for an nginx container, that will run the Python code in port 80 internally on the docker container python running on port 8080 only.

# Start

1. Create a EC2 Instance
2. Connect to server
3. Work on CLI
        1. Install updates:
            sudo apt update
        2. Create a user & login
            sudo adduser newuser
            su - newuser
                        or
           Use root user(not recommended) 
            sudo -i
        <!--Install Python
             sudo apt-get python3-pip-->
        3. docker network create my_network
        4. mkdir python-app
            cd python-app
            vim app.py
            vim Dockerfile
            vim nginx_conf
            cd nginx_conf
            vim nginx_conf
            vim Dockerfile
        5. cd ..
        6. docker build -t python-server . <!--sudo docker...(if doesn't work) -->
        6. docker run -d -p 8080:8080 python-container --name network=my_network python-app1
        7. Check 'docker logs <container-id> in case of errors
4. Check on your locahost @publicIP:8080
        1. cd nginx_conf
        2. docker build -t nginx-server .
        3. docker run -d -p 80:80 nginx-container --name network=my_network nginx-app1
5. Check on your locahost @publicIP:80