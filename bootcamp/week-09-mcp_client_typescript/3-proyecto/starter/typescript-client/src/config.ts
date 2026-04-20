// config.ts — Valida variables de entorno al arrancar
// Falla rápido si faltan vars requeridas

const required = (name: string): string => {
  const value = process.env[name];
  if (!value) throw new Error(`Missing environment variable: ${name}`);
  return value;
};

export const config = {
  serverCommand: process.env["SERVER_COMMAND"] ?? "python",
  serverPath: required("SERVER_PATH"),
  dbPath: process.env["DB_PATH"] ?? "./data/library.db",
} as const;
