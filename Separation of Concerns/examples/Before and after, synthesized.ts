// Before: selection, presentation, and I/O are intertwined.
async function showOverdueInvoices() {
  const response = await fetch("/api/invoices");
  const invoices = await response.json();
  document.body.innerHTML = invoices
    .filter((invoice: any) => Date.parse(invoice.dueAt) < Date.now())
    .map((invoice: any) => `<strong>${invoice.customer}: ${invoice.total}</strong>`)
    .join("");
}

// After: separate three kinds of change without adding framework layers.
type Invoice = { customer: string; total: number; dueAt: string };

const overdue = (invoices: Invoice[], now: number) =>
  invoices.filter(invoice => Date.parse(invoice.dueAt) < now);

const renderInvoices = (invoices: Invoice[]) =>
  invoices.map(i => `<strong>${i.customer}: ${i.total}</strong>`).join("");

async function displayOverdueInvoices() {
  const response = await fetch("/api/invoices");
  const invoices: Invoice[] = await response.json();
  document.body.innerHTML = renderInvoices(overdue(invoices, Date.now()));
}
