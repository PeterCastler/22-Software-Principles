// Before: time, database access, policy, and sending are one operation.
async function notifyExpired(db: any, mailer: any) {
  for (const user of await db.users()) {
    if (user.expiresAt <= Date.now() && !user.trial) {
      await mailer.send(user.email, `Expired: ${user.name}`);
    }
  }
}

type User = { name: string; email: string; expiresAt: number; trial: boolean };
type Message = { to: string; body: string };

// Functional core: all decisions are explicit inputs and ordinary outputs.
const expiryMessages = (users: User[], now: number): Message[] => users
  .filter(user => user.expiresAt <= now && !user.trial)
  .map(user => ({ to: user.email, body: `Expired: ${user.name}` }));

// Imperative shell: effects are visible and thin.
async function sendExpiryMessages(db: any, mailer: any) {
  const messages = expiryMessages(await db.users(), Date.now());
  await Promise.all(messages.map(message => mailer.send(message.to, message.body)));
}
