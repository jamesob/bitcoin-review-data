- [ ] 6345e65d31 node: Extract chainstate loading sequence
- [ ] 165b30b649 node/chainstate: Decouple from GetTimeMillis
- [ ] 64195bf2e4 node/chainstate: Decouple from stringy errors
- [ ] bb8245bedc node/chainstate: Decouple from ArgsManager
- [ ] aa6bc732b1 node/chainstate: Decouple from concept of NodeContext
- [ ] 0d2f1a458e Move mempool nullptr Assert out of LoadChainstate
- [ ] 49d2d11aa5 Move init logistics message for BAD_GENESIS_BLOCK to init.cpp
- [ ] 0b340cd586 node/chainstate: Remove do/while loop
- [ ] 019da3dc84 Split off VerifyLoadedChainstate
- [ ] efe9bd2876 node/chainstate: Decouple from concept of uiInterface
- [ ] 71c78844ee node/chainstate: Reduce coupling of LogPrintf
- [ ] 02c5d48532 Move -checkblocks LogPrintf to AppInitMain
- [ ] ca13555758 init: Delay RPC block notif until warmup finished
- [ ] e073634c37 node/chainstate: Decouple from GetAdjustedTime
- [ ] 2a2a496fe8 node/chainstate: Decouple from ShutdownRequested
- [ ] 7d0cf02654 validation: VerifyDB only needs Consensus::Params
- [ ] fefd26434c node/caches: Extract cache calculation logic
- [ ] 4a50ef72d7 node/chainstate: Add options for in-memory DBs
- [ ] 526b218273 test/setup: Use LoadChainstate
- [ ] 8b3080f2d6 test/setup: Unify m_args and gArgs
- [ ] 97162b171e Remove all #include // for * comments
- [ ] fdc07a1d29 Collapse the 2 cs_main locks in LoadChainstate