type RawConfig = { port?: unknown };

// Before: validation returns no knowledge. Later code casts and checks again.
function validateConfig(value: RawConfig): void {
  if (!Number.isInteger(value.port) || (value.port as number) <= 0) {
    throw new Error("Invalid port");
  }
}

function startRaw(value: RawConfig) {
  validateConfig(value);
  const port = value.port as number; // the type still permits undefined/string
  server.listen(port);
}

// After: parsing returns the trusted representation or an explicit error.
type Config = { port: number };

function parseConfig(value: RawConfig): Config {
  if (!Number.isInteger(value.port) || (value.port as number) <= 0) {
    throw new Error("Invalid port");
  }
  return { port: value.port as number };
}

function start(value: RawConfig) {
  const config = parseConfig(value);
  server.listen(config.port);
}
