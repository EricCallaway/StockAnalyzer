# Frontend server Dockerfile
FROM node:20-alpine

# Set working directory
WORKDIR /server

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy source code
COPY . .

# Expose port
EXPOSE 4000

# Start the server
CMD ["node", "index.js"]
