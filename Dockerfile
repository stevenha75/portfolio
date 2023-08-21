# Pull base image
FROM python:3.10.4-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory (location where all subsequent commands are run)
WORKDIR /code

# Install dependencies
COPY ./requirements.txt .
RUN apt-get update && apt-get install -y curl \
  && curl -sL https://deb.nodesource.com/setup_14.x | bash - \
  && apt-get install -y nodejs --no-install-recommends \
  && rm -rf /var/lib/apt/lists/* \
  && pip install -r requirements.txt

# Copy project
COPY . .

# !!Tailwind setup and build commands (Do this before pushing to prod)
# RUN SECRET_KEY=nothing python manage.py tailwind install --no-input;
# RUN SECRET_KEY=nothing python manage.py tailwind build --no-input;
# RUN SECRET_KEY=nothing python manage.py collectstatic --no-input;