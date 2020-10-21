# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:1.10.3

# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements, if necessary (uncomment next line)
COPY actions/requirements-actions.txt ./

# Change back to root user to install dependencies
USER root

# Install extra requirements for actions code, if necessary (uncomment next line)
RUN pip install --upgrade pip
RUN pip install -r requirements-actions.txt
RUN python -m spacy download fr_core_news_md

# Copy actions folder to working directory
COPY ./actions /app/actions
COPY ./enigma.pkl /app/enigma.pkl
COPY ./action_data /app/action_data

# Add a user and add permission to this user
RUN useradd -u 1001 appuser && chown -R appuser:appuser /app

# By best practices, don't run the code with root user
USER appuser
