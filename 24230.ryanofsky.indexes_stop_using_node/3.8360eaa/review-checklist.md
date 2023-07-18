- [ ] a035b6500f indexes, refactor: Remove index prune_violation code
- [ ] de311f9f9e indexes, refactor: Remove index Init method
- [ ] 43e03ec21f indexes, refactor: Remove index validation interface and block locator code
- [ ] a7f0612b5e indexes, refactor: Stop incorrectly calling Interupt() and Stop() in BaseIndex destructor
- [ ] 3eb92c59b3 indexes, refactor: Add Commit CBlockLocator& argument
- [ ] 00b2300f91 indexes, refactor: Remove remaining CBlockIndex* uses in index Rewind methods

Rewind -> Remove (block range vs. single block) seems fine conceptually.

- [ ] 5605e4e131 indexes, refactor: Remove remaining CBlockIndex* uses in index CustomAppend methods

Commit message has an error: "Move CustomAppend call from BaseIndex::ThreadSync to BaseIndex::ThreadSync"

- [ ] c6c230ba22 indexes, refactor: Move more new block logic out of ThreadSync to blockConnected
- [ ] dd9c76f60c indexes, refactor: Move Commit logic out of ThreadSync to notification handlers
- [ ] b4e914d58d indexes, refactor: Move Rewind logic out of Rewind to blockDisconnected and ThreadSync
- [ ] 52ef7e4de9 indexes, refactor: Move CustomInit and error handling code out of ThreadSync to notification handlers
- [ ] 3c31b91502 indexes, refactor: Move sync thread from index to node
- [ ] 1292d697a0 indexes, refactor: Remove SyncWithValidationInterfaceQueue call
- [ ] d602569c64 indexes: Rewrite chain sync logic, remove racy init
- [ ] 31038f9546 indexes: Initialize indexes without holding cs_main
- [ ] a1a7ba4f75 indexes, refactor: Remove UndoReadFromDisk calls from indexing code
- [ ] 079db6a2b7 indexes, refactor: Remove remaining CBlockIndex* pointers from indexing code
- [ ] 8360eaa0b2 Remove direct index -> node dependency
