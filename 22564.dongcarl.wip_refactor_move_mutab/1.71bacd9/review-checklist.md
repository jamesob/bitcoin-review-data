- [x] 3ea18162a4 Move pindexBest{Header,Invalid} to BlockManager
- [x] fa455c0339 Move setDirty{BlockIndex,FileInfo} to BlockManager
- [x] a5d50a092b validation: Add missing cs_LastBlockFile locks in PruneAndFlush() and UnloadBlockIndex(). Add missing locking annotation for nLastBlockFile and fCheckForPruning.
- [x] 952482e859 Guard vinfoBlockFile with cs_LastBlockFile as well
 
  You may have already intended to do this, but you can probably absorb this into the previous commit.

- [x] 81f0828ade Move cs_LastBlockFile guarded objects to BlockManager
- [x] c2ffc0c660 validation: Guard nBlockReverseSequenceId with cs_main
 
  Change is fine but seems sort of unrelated to PR?

- [x] 024f19f8ef Move fHavePruned to BlockManager
 
  First few lines of diff seem unrelated (I see, needed for blockman ref). Why std::ref? 

  - [ ] is avoiding fHavePruned = false in UnloadBlockIndex safe? Even if it is, let's
    do this in a separate commit to ease review.
 
- [x] 17f227f6d4 Move versionbitscache to BlockManager

  - [ ] should this eventually be covered by a lock? maybe blockman specific?
  - [ ] maybe break up those longass lines
  - [ ] forward declaration in versionbits.h unnecessary?

- [x] 318d8ffdf1 warningcache: C-array to std::array
- [x] 9ab4a88eda Move warningcache to BlockManager
  
  - [ ] can probably be squashed into prev commit
  
- [x] b48d7c010f No more heap BlockIndices
 
  - [ ] performance implications for all the new copies?
  - [ ] why remove const on LookupBlockIndex? (prob due to returning cblockindex vals)
    - [ ] TODO try making it const again, see how compilation fails
  - [ ] `neue` weird name for cblockindex?
  
- [x] f4e61fac35 No more heap, no mo weirdneess
- [x] 3de7842f50 init: Reset mempool and chainman via reconstruction
 
  - best reviewed using --color-move=dimmed_zebra
  - [ ] this will need a lot of testing to avoid init bugs
 
- [x] 913b47cb42 validation: Prune UnloadBlockIndex and callees

  - Love this commit.
  
- [x] 71bacd9265 scripted-diff: Rename cs_LastBlockFile to cs_blockfiles
