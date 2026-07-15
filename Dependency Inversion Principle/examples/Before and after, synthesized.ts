type Receipt = { orderId: string; total: number };

// Before: checkout policy creates and depends on one infrastructure detail.
class Checkout {
  async complete(receipt: Receipt) {
    const client = new VendorEmailSdk(process.env.EMAIL_KEY!);
    await client.send(receipt.orderId, receipt.total);
  }
}

// After: the policy owns the smallest domain-shaped need.
type SendReceipt = (receipt: Receipt) => Promise<void>;

const completeCheckout = async (receipt: Receipt, sendReceipt: SendReceipt) => {
  await sendReceipt(receipt);
};

const sendVendorReceipt: SendReceipt = receipt =>
  vendorClient.send(receipt.orderId, receipt.total);

// A function type is enough; no interface, factory, or container is required.
