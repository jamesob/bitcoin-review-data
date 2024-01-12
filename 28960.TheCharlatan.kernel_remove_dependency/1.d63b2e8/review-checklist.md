- [x] cfb94ef2b3 [refactor] De-globalize CMainSignals

Moving CMainSignals global onto `NodeContext`; good stuff, probably been a long time coming.

Easier to review with `--color-moved=dimmed-zebra --color-moved-ws=ignore-all-space`.

- [x] 2eb6be4407 [refactor] Make MainSignalsImpl RAII styled
- [ ] b1aca69b11 [refactor] Move scheduler client to CMainSignals
- [ ] d63b2e8878 kernel: Remove dependency on CScheduler
