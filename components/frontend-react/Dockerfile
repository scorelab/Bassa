FROM node:12

WORKDIR /bassa

COPY package.json .
COPY package-lock.json .
RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
