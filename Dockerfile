FROM jenkins/jenkins:lts-jdk17

# Install Python and pip
USER root
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3.11-venv && \
    apt-get clean

# Switch back to Jenkins user
USER jenkins
