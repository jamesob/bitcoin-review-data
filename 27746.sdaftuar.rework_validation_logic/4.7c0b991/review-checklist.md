- [ ] fe86a7cd48 Explicitly track maximum block height stored in undo files
- [ ] 1cfc887d00 Remove CChain dependency in node/blockstorage
- [ ] 5f696116b0 Move block-arrival information / preciousblock counters to ChainstateManager
- [ ] e384d21620 Add wrapper for adding entries to a chainstate's block index candidates
- [ ] abdc34f4f4 Update CheckBlockIndex invariants for chains based on an assumeutxo snapshot
- [ ] a9bfceb79f test: Clear block index flags when testing snapshots
- [ ] ee831d9aa8 Move block-storage-related logic to ChainstateManager
- [ ] 2e5fb47629 Tighten requirements for adding elements to setBlockIndexCandidates
- [ ] bcc8d1e6a4 Fix initialization of setBlockIndexCandidates when working with multiple chainstates
- [ ] 53951723f5 Documentation improvements for assumeutxo
- [ ] 093697d89f Move CheckBlockIndex() from Chainstate to ChainstateManager
- [ ] 7c0b991442 Cache block index entry corresponding to assumeutxo snapshot base blockhash