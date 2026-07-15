// Before: every combination of transport and formatting needs a subclass.
class Logger { log(message: string) { console.log(message); } }
class JsonLogger extends Logger {
  log(message: string) { super.log(JSON.stringify({ message })); }
}
class FileLogger extends Logger { /* file-specific override */ }
class JsonFileLogger extends FileLogger { /* duplicated JSON override */ }

// After: two independent behaviors compose without combination classes.
type Format = (message: string) => string;
type Write = (message: string) => void;

const createLogger = (format: Format, write: Write) => (message: string) =>
  write(format(message));

const text: Format = message => message;
const json: Format = message => JSON.stringify({ message });
const consoleWrite: Write = message => console.log(message);

const jsonConsoleLogger = createLogger(json, consoleWrite);
const textConsoleLogger = createLogger(text, consoleWrite);
