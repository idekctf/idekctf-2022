FROM node:lts-buster-slim

# Install packages
RUN apt update && apt install -y supervisor yarn

# Setup app
RUN mkdir -p /app && chown -R root:root /app

# Add application
WORKDIR /app
COPY challenge .

# Install dependencies
WORKDIR /app/app
RUN yarn

# Generate random flag filename
RUN mv flag.txt flag_`cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 5 | head -n 1`.txt

# Setup superivsord
COPY config/supervisord.conf /etc/supervisord.conf

# Expose the port node-js is reachable on
EXPOSE 1337

# Switch to use a non-root user from here on
USER nobody

WORKDIR /app/app

# Start the node-js application
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
