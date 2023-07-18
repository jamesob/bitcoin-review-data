- [x] c70934c80 init: Use existing chainman
- [x] 1b21b6095 test/util: Use existing chainman in ::PrepareBlock
- [x] f172c8a22 test/miner_tests: Pass in chain tip to CreateBlockIndex
- [x] 8469d6b7b test: Pass in CoinsTip to ValidateCheckInputsForAllFlags
- [x] 92313bd8d scripted-diff: test: Use existing chainman in unit tests
- [x] 33215dd29 fuzz: Initialize a TestingSetup for test_one_input
- [x] 2485e6cc1 scripted-diff: wallet/test: Use existing chainman
- [x] 634e1236e qt/test: Use existing chainman in ::TestGUI (can be scripted-diff)
- [x] 0ac46831f tree-wide: Remove stray review-only assertion
- [x] 216663076 scripted-diff: tree-wide: Remove all review-only assertions
- [x] 274581123 qt/test: Reset chainman in ~ChainstateManager instead
- [x] cc8cc9c4a validation: Farewell, global Chainstate!

Many scripted-diffs make this an easy, mechanical change. All the ActiveTip() nits can be probably be addressed by doing a single scripted-diff cleanup that seds `'ActiveChain\(\).Tip\(\)'`.

Nice job with all the scripted-diffs; they make review much easier. Man oh man that's a lot of asserts! I like your thinking moving `UnloadBlockIndex()` into the ChainstateManager destructor.

Big moves! Nice work on this! Who ever thought we'd have chainstate deglobalized?? What a world.
