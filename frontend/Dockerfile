FROM node:18-alpine AS builder

WORKDIR /usr/src/frontend

COPY . ./

ENV SECRET=

RUN npm ci

RUN npm run build

EXPOSE 5173

CMD [ "npm", "start" ]