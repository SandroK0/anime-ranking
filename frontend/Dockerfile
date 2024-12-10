# Build stage
FROM node:16 as build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json first (caching dependencies layer)
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy project files
COPY . .

# Build the app
RUN npm run build

# Production stage
FROM httpd:alpine

# Copy built assets from build stage to the Apache server's document root
COPY --from=build /app/dist/ /usr/local/apache2/htdocs/

# Expose port 80
EXPOSE 80

# Start Apache server
CMD ["httpd-foreground"]
