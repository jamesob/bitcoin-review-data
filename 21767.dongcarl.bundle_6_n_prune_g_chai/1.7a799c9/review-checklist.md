- [x] fc1c28284 rpc/blockchain: Use existing blockman in gettxoutsetinfo
  
  Oneline fix.

- [x] 9ecade142 rest: Add GetChainman function and use it
 
  I don't know the REST code well but all changes seem consistent with 
  existing conventions.

- [x] e6b4aa6eb miner: Pass in chainman to RegenerateCommitments
  
  Question about assertion -> assignment change.

- [x] 91226eb91 bench: Use existing NodeContext in DuplicateInputs

  `ActiveTip()` nit as already noted by John.

- [x] f4a47a1fe bench: Use existing chainman in AssembleBlock
 
- [x] db33cde80 index: Add chainstate member to BaseIndex

  See questions around active chainstate management in the context
  of `ActivateSnapshot()` use. The indexer probably needs to be made
  aware of the new active chainstate, or it should just hold a reference
  to chainman and not have to worry about being notified.

- [x] 7a799c9c2 index: refactor-only: Reuse CChain ref

  Could probably be fixed-up into the previous commit.
