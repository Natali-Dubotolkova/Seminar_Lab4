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

---

## Step 2: Launch Jenkins and Verify NTP Setup

### 2.1. Use Docker Compose to bring up the Jenkins and NTP services
- Run the following command to start Jenkins and NTP services:

    ```bash
    docker-compose up -d
    ```

### 2.2. Access Jenkins via [http://localhost:8080](http://localhost:8080)
- After starting the services, open Jenkins by navigating to `http://localhost:8080` in your browser.
- Follow the instructions to enter the initial admin password (found using `docker logs`).

### 2.3. Complete the Jenkins Setup
- Install the suggested plugins during Jenkins' initial setup.
- Set up your admin account.

### 2.4. Verify NTP Service
- To verify NTP service is working, access the NTP container logs or manually check the synchronized system time:

    ```bash
    docker logs ntp-service
    ```

- Ensure the system clock inside the Docker environment is synced to the Moscow timezone.

---

## Step 3: Create a Simple Python Application

### 3.1. Create a Basic Python Application
- Create a simple Python application with one or two basic functions (e.g., arithmetic operations).

### 3.2. Write Unit Tests
- Use a Python testing framework like **unittest** or **pytest** to write unit tests for the application. 

### 3.3. Push the Code to a GitHub Repository
- Ensure that the Python application and the corresponding unit tests are added to a GitHub repository. Jenkins will use this repository for the CI pipeline.

---

## Step 4: Configure a Jenkins Pipeline

### 4.1. Create a New Pipeline Job in Jenkins
- In Jenkins, create a new **Pipeline Job**:
    - Go to Jenkins dashboard.
    - Click on `New Item`.
    - Select `Pipeline` and give it a name (e.g., "Python CI Pipeline").

### 4.2. Configure the Pipeline to Pull from GitHub
- In the pipeline configuration, set the **Pipeline Definition** to "Pipeline script from SCM".
- Choose **Git** as the SCM and provide the URL to your GitHub repository.

### 4.3. Define the Jenkinsfile Pipeline Stages
- Add a `Jenkinsfile` to the root of your GitHub repository. This file defines the CI stages.
- In the `Jenkinsfile`, define the pipeline stages using the **Declarative Pipeline** syntax.
- **Checkout** the code from the GitHub repository.
- **Install Python** and required dependencies.
- **Run Unit Tests** using the `unittest` framework.
- **Build and Deploy** the application (if necessary).

### 4.4. Pipeline Stages Breakdown
- **Checkout Code**: Pulls the latest code from the GitHub repository.
- **Install Python and Dependencies**: Installs Python and any required packages from `requirements.txt`.
- **Run Unit Tests**: Executes the unit tests defined in `app_test.py`.
- **Build and Deploy**: Builds the application and deploys it to a production environment (if necessary)


---

## Step 5: Run the Pipeline and Analyze the Results

### 5.1. Trigger the Pipeline
- You can trigger the pipeline by:
  - Pushing code changes to your GitHub repository, which will automatically initiate the pipeline.
  - Manually running the pipeline from the Jenkins UI:
    - Navigate to your pipeline job in Jenkins.
    - Click on the `Build Now` button.

### 5.2. Monitor the Jenkins Logs
- Monitor the Jenkins logs to ensure the pipeline executes correctly:
  - Click on the build number in the Jenkins dashboard.
  - Review the console output for each stage to confirm the correct execution flow.

### 5.3. Analyze the Pipeline Results
- Once the pipeline completes, check the results:
  - Ensure that the Python tests are run successfully.
  - Look for any indicators of success or failure in the Jenkins UI.

### 5.4. Investigate Errors or Test Failures
- If any errors or test failures occur:
  - Investigate the logs for detailed error messages.
  - Make necessary changes to your application code or tests.
  - Rerun the pipeline after making corrections.

---

## Step 6: Integrate NTP with Jenkins

### 6.1. Verify NTP Synchronization
- Check that the Jenkins container is synchronizing with the NTP server correctly:
  - Access the Jenkins container's shell:

    ```bash
    docker exec -it jenkins-ci /bin/bash
    ```

  - Use the `ntpq` command to query the NTP server status:

    ```bash
    ntpq -p
    ```

### 6.2. Confirm System Time
- Confirm that the system time inside the Jenkins container matches the actual system time:
  - Inside the Jenkins container, check the current time:

    ```bash
    date
    ```

  - Compare it with the time on your host machine using:

    ```bash
    date
    ```

---