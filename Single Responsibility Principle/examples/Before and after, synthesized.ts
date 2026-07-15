// Before: policy, persistence, and presentation change for different reasons.
class Invoice {
  constructor(readonly items: Array<{ price: number }>) {}
  total() { return this.items.reduce((sum, item) => sum + item.price, 0); }
  async save(db: any) { await db.insert("invoices", this); }
  toHtml() { return `<p>Total: ${this.total()}</p>`; }
}

// After: separate change ownership; avoid an interface per class.
type InvoiceData = { items: Array<{ price: number }> };

const invoiceTotal = (invoice: InvoiceData) =>
  invoice.items.reduce((sum, item) => sum + item.price, 0);

const saveInvoice = (db: any, invoice: InvoiceData) =>
  db.insert("invoices", invoice);

const invoiceHtml = (invoice: InvoiceData) =>
  `<p>Total: ${invoiceTotal(invoice)}</p>`;
