- [x] 3fe223c36f Explicitly track maximum block height stored in undo files
- [x] 59b085f4d8 Remove CChain dependency in node/blockstorage
- [x] 96cd3b0635 Move block-arrival information / preciousblock counters to ChainstateManager

Unsure how this is related to assumeutxo? Just general cleanup?

- [ ] 1c3f815670 Add wrapper for adding entries to a chainstate's block index candidates
- [ ] b6997f10dc Update CheckBlockIndex invariants for chains based on an assumeutxo snapshot
- [ ] d998ea1cff test: Clear block index flags when testing snapshots
- [ ] 943bd665e2 Move block-storage-related logic to ChainstateManager
- [ ] 55e27ee995 Tighten requirements for adding elements to setBlockIndexCandidates
- [ ] c21624c14b Fix initialization of setBlockIndexCandidates when working with multiple chainstates
- [ ] 2d20f75b0b Documentation improvements for assumeutxo
- [ ] 3110dbcee2 Move AcceptBlock, ReceivedBlockTransactions, and AcceptBlockHeader out of ChainstateManager
- [ ] 78fcc8fbdc fixup! Fix initialization of setBlockIndexCandidates when working with multiple chainstates
- [ ] f1ee72fd12 Move CheckBlockIndex() from Chainstate to ChainstateManager
- [ ] 4a69901104 fixup! Remove CChain dependency in node/blockstorage
