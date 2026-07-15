// First occurrence: keep the rule local.
const activeUsers = users.filter(user => user.enabled && !user.deletedAt);

// Second occurrence: note the resemblance, but the concepts may still diverge.
const activeAdmins = admins.filter(admin => admin.enabled && !admin.deletedAt);

// Third occurrence confirms one domain concept: an active account.
type AccountState = { enabled: boolean; deletedAt?: Date };
const isActive = (account: AccountState) =>
  account.enabled && !account.deletedAt;

const filteredUsers = users.filter(isActive);
const filteredAdmins = admins.filter(isActive);
const activeEditors = editors.filter(isActive);

// If the three rules merely looked alike but changed for different stakeholders,
// retain duplication instead of inventing flags to force them together.
