- [x] 66b8d3c23d reindex, log, test: fixes #21379

Tested locally. The source of the bug (reading through SaveBlockToDisk -> FindBlockPos) is still somewhat unclear to me... I guess I'm trying to determine where those 8 header bytes are accounted for in the case of an existing block during reindex. In other words, exactly what line is responsible for the addition of those 8 bytes to the `FlatFilePos* dbp`, which is passed into SaveBlockToDisk.

Near as I can figure, the answer to that question is somewhere in the `LoadExternalBlockFile -> AcceptBlock` call chain.

[after writing the above and rereading the code]

My best guess is that those 8 bytes are included in LoadExternalBlockFile (`nRewind = blkdat.GetPos()`) after an existing block is read (which then determines the value of `dbp`), whereas during the addition of a new block, no existing data is read and therefore those 8 header bytes are unaccounted for.

Anyway, I've tested this patch pretty extensively:
- multiple subsequent -reindex calls with -stopatheight=105000
- using this branch with an existing mainnet datadir, waiting for new tips to come in, switching back to master and ensuring init happens properly
- revert change in validation.cpp, ensure included unittests fail

So I have good confidence that this is safe and correct.

Thanks for working on this; I think this is a pretty important issue to iron out even if it doesn't immediately cause true data corruption. It's the kind of thing that could easily cascade into a bigger problem.
