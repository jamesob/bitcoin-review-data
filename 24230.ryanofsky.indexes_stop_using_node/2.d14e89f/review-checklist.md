- [x] cf5d340448 interfaces, refactor: Add more block information to block connected notifications
- [x] f72ebd3eb9 indexes, refactor: Pass Chain interface instead of CChainState class to indexes
- [x] 624ee1ee9b indexes, refactor: Remove CBlockIndex* uses in coinstatsindex LookUpOne function
- [x] 15daa47ee0 indexes, refactor: Remove CBlockIndex* uses in index Init methods
- [x] ae7b272886 indexes, refactor: Remove CBlockIndex* uses in index WriteBlock methods
- [x] 820ac9302d indexes, refactor: Remove CBlockIndex* uses in index Rewind methods
- [x] 65d5ac7ae5 indexes, refactor: Remove CChainState use in index CommitInternal method
- [x] fc78244754 indexes, refactor: Remove index prune_violation code
- [x] b2b3ab4cd4 indexes, refactor: Remove index Init method
- [x] e470119fe5 indexes, refactor: Remove index validation interface and block locator code
- [x] ed0afe9092 indexes, refactor: Stop incorrectly calling Interupt() and Stop() in BaseIndex destructor
- [x] 714be24cb7 indexes, refactor: Add Commit CBlockLocator& argument
- [x] 0e80167cc8 indexes, refactor: Remove remaining CBlockIndex* uses in index Rewind methods
- [x] afce60462f indexes, refactor: Remove remaining CBlockIndex* uses in index CustomAppend methods
- [x] bf6a0f8ae8 indexes, refactor: Move more new block logic out of ThreadSync to blockConnected
- [x] 7add4807d8 indexes, refactor: Move Commit logic out of ThreadSync to notification handlers
- [ ] 4e0b09777b indexes, refactor: Move Rewind logic out of Rewind to blockDisconnected and ThreadSync

Really hard to follow this one.

- [x] 480387218c indexes, refactor: Move CustomInit and error handling code out of ThreadSync to notification handlers
- [x] c4e0a9dd45 indexes, refactor: Move sync thread from index to node
- [x] d39c6d0062 indexes, refactor: Remove SyncWithValidationInterfaceQueue call
- [ ] 8c0c231840 indexes: Rewrite chain sync logic, remove racy init

For easier reviewability it would be nice to absorb this into prior commits if possible; i.e. 
avoid introducing the `Ignore*` methods only to take them away in this commit. Creates
a lot of churn to review. But would be curious to know if this is particularly difficult
to do for some reason.

For what it's worth, I the code in this commit much clearer than previous equivalents of
`SyncChain`. Again there seems to be some churn in `attachChain()` that would save on 
unnecessary review of prior commits.

The `NotificationsHandlerImpl` could use some doc; I've had a hard time
determining generally how it fits in and e.g. what the `connect` parameter
does.

- [ ] c7729d1f0c indexes: Initialize indexes without holding cs_main
- [ ] 278cc3d737 indexes, refactor: Remove UndoReadFromDisk calls from indexing code
- [ ] d14e89f701 indexes, refactor: Remove remaining CBlockIndex* pointers from indexing code
