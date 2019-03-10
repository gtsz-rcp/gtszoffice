FROM node:10.4.0
WORKDIR /gtszoffice-admin
COPY package*.json ./
COPY . .

RUN npm install -g vue-cli webpack
RUN npm install
ENV HOST 0.0.0.0
ENV PORT 8080