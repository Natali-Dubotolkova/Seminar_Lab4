# 🛠️ Jenkins CI Pipeline with NTP Integration using Docker Compose

![Docker](https://img.shields.io/badge/Docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-%232C5263.svg?style=for-the-badge&logo=jenkins&logoColor=white)

This project sets up a **Continuous Integration (CI) pipeline** using Jenkins, which is running inside a Docker container. Additionally, it integrates **NTP (Network Time Protocol)** to ensure system time synchronization within the Docker environment.

## 🎯 Task Overview

In this lab, you'll:
1. Set up **Jenkins** in Docker to run CI jobs.
2. Integrate **NTP** for time synchronization.
3. Use **Docker Compose** to manage both services.
4. Follow **security best practices**, including using non-root users, setting resource limits, and using specific versions of Docker images.

---

## 📦 Services Included

### 🧑‍💻 Jenkins CI Server
- Jenkins is used for **continuous integration** to automate running tests and other processes each time new code is committed to a project.
- The Jenkins service will be available at [http://localhost:8080](http://localhost:8080).

### ⏲️ NTP (Network Time Protocol)
- **NTP** ensures accurate system time within the Docker containers.
- The NTP service synchronizes the system clock to UTC/Moscow time, ensuring that Jenkins jobs are timestamped correctly.

---

## 🛠️ Setup Instructions

### Prerequisites
- **Docker** and **Docker Compose** installed on your machine.
- For Docker installation, follow the [official instructions](https://docs.docker.com/get-docker/).
- For Docker Compose installation, follow the [official instructions](https://docs.docker.com/compose/install/).

### 🚀 How to Run the Project

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Start the Docker services** using Docker Compose:

    ```bash
    docker-compose up -d
    ```

3. **Access Jenkins** by visiting:

    ```bash
    http://localhost:8080
    ```

    - Jenkins will require you to enter an initial admin password, which can be retrieved from the Jenkins container logs or from the `jenkins_home` directory:

    ```bash
    docker exec -it jenkins-ci cat /var/jenkins_home/secrets/initialAdminPassword
    ```

4. **Access NTP Service**: The NTP service will automatically sync the system time with Moscow timezone settings inside the Docker environment.

---

## 🔧 Configuration Details

### Docker Compose Services

- **Jenkins**: CI server that runs on `http://localhost:8080`.
- **NTP**: Network Time Protocol service that syncs the system time in Docker containers.

### Docker Compose Configuration
The `docker-compose.yml` includes:
- **Specific image versions** to prevent unexpected changes.
- **Security best practices**, such as:
  - Running Jenkins as a non-root user.
  - Limiting resource usage with CPU and memory constraints.
  - Using `no-new-privileges` for privilege escalation protection.

### Environment Variables
The services are configured to run with the **Moscow timezone (Europe/Moscow)** to ensure accurate time for Jenkins jobs.
