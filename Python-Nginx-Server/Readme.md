## Creating a reverse proxy for an nginx container, that will run the Python code in port 80 internally on the docker container python running on port 8080 only.

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
   3. Create a network

           docker network create my_network

   4. Create Directory & following files:
      
           mkdir python-app
           cd python-app
      1. nano [app.py](https://github.com/Viveksati5143/Docker-Server/blob/main/Python-Nginx-Server/app.py)
      2. nano [Dockerfile](https://github.com/Viveksati5143/Docker-Server/blob/main/Python-Nginx-Server/Dockerfile)

                mkdir nginx_conf
                cd nginx_conf
         1. nano [nginx.conf](https://github.com/Viveksati5143/Docker-Server/blob/main/Python-Nginx-Server/nginx_conf/nginx.conf)
         2. nano [Dockerfile](https://github.com/Viveksati5143/Docker-Server/blob/main/Python-Nginx-Server/nginx_conf/Dockerfile)
   5. Move back to python-app

           cd ..
   6. Build using Docker
  
           docker build -t python-server .
      <!--sudo docker...(if doesn't work) -->
   8. Run using Docker
      
           docker run -d -p 8080:8080 python-container --name network=my_network <image-name-in-dockerhub>
      <!-- or use AWS ECR to fetch image -->
   9. Check logs in case of errors

           docker logs <container-id>
4. Check on your locahost @publicIP:8080

      ### Now you have completed setting-up Python server in AWS EC2 using Docker

## To set up Nginx server in AWS EC2 follow the below commands after completing Step 4:

<!--1. cd nginx_conf-->
1. Build using Docker
   
        docker build -t nginx-server .
2. Run using Docker
   
        docker run -d -p 80:80 nginx-container --name network=my_network <nginx-image>
3. Check on your locahost @publicIP:80

      ### Now you have completed setting-up Nginx server in AWS EC2 using Docker
