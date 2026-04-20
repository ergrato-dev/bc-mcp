FROM node:22-slim

RUN corepack enable && corepack prepare pnpm@10.11.0 --activate

WORKDIR /app

COPY package.json ./
RUN pnpm install --frozen-lockfile --prod

COPY src/ ./src/
COPY tsconfig.json ./

RUN pnpm build

CMD ["node", "dist/index.js"]
