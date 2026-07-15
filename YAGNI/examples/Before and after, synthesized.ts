// Before: one caller needs JSON, but a speculative export subsystem is built.
type Format = "json" | "xml" | "csv";

interface Serializer {
  serialize(value: unknown): string;
}

class ExportService {
  constructor(private readonly serializers: Map<Format, Serializer>) {}

  export(format: Format, value: unknown): string {
    const serializer = this.serializers.get(format);
    if (!serializer) throw new Error(`Unsupported format: ${format}`);
    return serializer.serialize(value);
  }
}

// After: implement the only requirement. Add another format when a real caller
// supplies its concrete rules (escaping, schema, streaming, error behavior).
export const exportJson = (value: unknown): string => JSON.stringify(value);
