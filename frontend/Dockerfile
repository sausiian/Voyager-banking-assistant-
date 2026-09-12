# ----------------------------------------------------
# Base Stage: Install dependencies
# ----------------------------------------------------
FROM node:22-alpine AS base
WORKDIR /app

# Install dependencies based on package-lock.json
COPY package*.json ./
RUN npm ci

# ----------------------------------------------------
# Stage 1: Development with Vite Hot Reloading
# ----------------------------------------------------
FROM base AS development
WORKDIR /app
COPY . .
EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]

# ----------------------------------------------------
# Stage 2: Production Build
# ----------------------------------------------------
FROM base AS builder
WORKDIR /app
COPY . .
RUN npm run build

# ----------------------------------------------------
# Stage 3: Production Nginx Server
# ----------------------------------------------------
FROM nginx:alpine AS production
COPY --from=builder /app/dist /usr/share/nginx/html
# Custom nginx config for SPA routing fallback
RUN printf 'server {\n\
    listen 80;\n\
    server_name localhost;\n\
    root /usr/share/nginx/html;\n\
    index index.html;\n\
    location / {\n\
        try_files $uri $uri/ /index.html;\n\
    }\n\
}\n' > /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
