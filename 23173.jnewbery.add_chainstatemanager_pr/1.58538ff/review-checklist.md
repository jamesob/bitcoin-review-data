- [ ] aee26d9d52 [test] Don't set bypass_limits to true in txvalidationcache_tests.cpp
- [ ] e405bc88b2 [test] Don't set bypass_limits to true in txvalidation_tests.cpp
- [ ] f916354766 [validation] Add CChainState::ProcessTransaction()
- [ ] 9ece3fb06b [MOVEONLY] Move CChainState::MaybeUpdateMempoolForReorg() lower in validation.cpp
- [ ] e265765ca2 [refactor] Don't call AcceptToMemoryPool() from outside validation.cpp
- [ ] 4ec1fb5780 [validation] Remove bypass_limits argument from ChainstateManager::ProcessTransaction()
- [ ] 58538ff6ff [validation] Always call mempool.check() after processing a new transaction