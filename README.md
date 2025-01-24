<a href="https://www.docker.com/"> <img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/97_Docker_logo_logos-512.png" alt="docker" width="40" height="40"/> </a>

## Docker Commands

### Docker image

```bash
# 1. List all local Docker images
docker images
# - Displays all images available on your system.

# 2. Build an image from a Dockerfile
docker build -t <image_name>:<tag> <path_to_dockerfile>
# Example:
docker build -t my_app:1.0 .  # ("." current folder)

# 3. Pull an image from Docker Hub
docker pull <image_name>:<tag>
# Example:
docker pull ubuntu:20.04
# - Downloads the "ubuntu" image with tag "20.04" from Docker Hub.

# 4. Remove an image by name or ID
docker rmi <image_id_or_name>
```

### Docker container

```bash
# 1. List all running containers
docker ps

# 2. List all containers (including stopped ones)
docker ps -a

# 3. Run a container from an image
docker run -it --name <container_name> <image_name>:<tag>
# Example:
docker run -it --name my_container ubuntu:20.04

# 4. Run a container in interactive mode
docker run -it <image_name>:<tag>
# Example:
docker run -it ubuntu:20.04

# 5. Run a container in detached mode (background)
docker run -d --name <container_name> <image_name>:<tag>
# Example:
docker run -d --name my_web_server nginx

# 6. Run a container and publish ports
docker run -d -p <host_port>:<container_port> <image_name>:<tag>
# Example:
docker run -d -p 8080:80 --name my_nginx nginx
# - Maps port 80 of the container to port 8080 on the host machine.

# 7. Run a container with interactive mode and publish ports
docker run -it -p <host_port>:<container_port> <image_name>:<tag>
# Example:
docker run -it -p 5000:5000 python:3.9-slim bash
# - Opens an interactive shell and maps port 5000 for a Python application.

# 8. Stop a running container
docker stop <container_name_or_id>
# Example:
docker stop my_container

# 9. Start a stopped container
docker start <container_name_or_id>
# Example:
docker start my_container

# 10. Remove a container
docker rm <container_name_or_id>
# Example:
docker rm 

# 11. Access to running container
docker exec -it <container_id_or_name> bash
```

### Docker Compose
```bash
# 1. Start the containers defined in docker-compose.yml
docker compose up

# 2. Start the containers and rebuild the images (if there are changes in the Dockerfile)
docker compose up --build

# 3. Stop the running containers
docker compose down
```







