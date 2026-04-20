FROM node:22-slim

RUN corepack enable && corepack prepare pnpm@9.15.4 --activate

WORKDIR /app

COPY package.json ./
RUN pnpm install

COPY . .
RUN pnpm build

CMD ["node", "dist/index.js"]
