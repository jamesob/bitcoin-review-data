- [x] 20f2973ae2 indexes, refactor: Remove index prune_violation code
- [x] 151bad5de4 indexes, refactor: Remove index Init method
- [x] 8d0bcf4033 indexes, refactor: Remove index validation interface and block locator code
- [x] fa6efbff7f indexes, refactor: Stop incorrectly calling Interupt() and Stop() in BaseIndex destructor
- [x] e62683db04 indexes, refactor: Add Commit CBlockLocator& argument
- [x] e1e040fdd4 indexes, refactor: Remove remaining CBlockIndex* uses in index Rewind methods
- [x] 16f6a9900a indexes, refactor: Remove remaining CBlockIndex* uses in index CustomAppend methods

Commit message incorrect: "Move CustomAppend call from BaseIndex::ThreadSync to BaseIndex::ThreadSync"

- [x] bc71b09151 indexes, refactor: Move more new block logic out of ThreadSync to blockConnected
- [x] 627887a9b9 indexes, refactor: Move Commit logic out of ThreadSync to notification handlers
- [-] ac1369650d indexes, refactor: Move Rewind logic out of Rewind to blockDisconnected and ThreadSync

Maybe just too late in the day, but really couldn't understand the contents of this commit, too much for me.

- [x] 3038c883fd indexes, refactor: Move CustomInit and error handling code out of ThreadSync to notification handlers
- [ ] 01297836c7 indexes, refactor: Move sync thread from index to node

In progress; sadly, my diff tool doesn't consider the contents of ThreadSync() to have been moved.

- [ ] 9ce316c79a indexes, refactor: Remove SyncWithValidationInterfaceQueue call
- [ ] d8ab12f275 indexes: Rewrite chain sync logic, remove racy init
- [ ] e4c89baf9a indexes: Initialize indexes without holding cs_main
- [ ] 7a1f7a3e38 indexes, refactor: Remove UndoReadFromDisk calls from indexing code
- [ ] 74a8394a46 indexes, refactor: Remove remaining CBlockIndex* pointers from indexing code
- [ ] ad9f581fcc Remove direct index -> node dependency
