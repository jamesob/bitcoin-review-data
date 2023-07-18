I put about a day into reviewing commits locally, building them incrementally.
Every time I review this PR I seem to drop off earlier and earlier - not a great
testament to the health of my brain I guess.

Funny enough I had forgotten I'd written this in a previous review, but it still
captures my sentiments pretty exactly:

> At a high level I think this is a great change - the more "peripheral" parts
> of the system we can put on the other side of the Chain interface, the easier
> it is to carve off those parts both in terms of process separation (limiting
> "contagion" risk of non-essential code) and deeper modularization (allowing
> for more straightforward progression of e.g. libbitcoinkernel). The indexing
> system is a great candidate for this kind of change, and I'm really glad to
> see this PR doing it.
> 
> That said, it took me a while to get through the changes. ~~I think there's some
> potentially unnecessary churn within the commits (noted below).~~ While the code
> quality is very good, behavioral equivalence with existing code is not
> immediately obvious to me when reading through the changes (given there are just
> so many of them), and so to have confidence that this PR isn't really changing
> any behavior, I'm really going to need to dig in and do some testing as well as
> review the coverage of the existing functional tests.

I'd really like to sign off on this code, but I don't feel like I have the
horsepower to actually review the latter part of the changeset with much
confidence. It'd almost be easier to review the entire thing squashed down IMO.
If I ACK'd as-is, I'd be leaning on correctness verification via manual testing
and verifying functional coverage.

I feel bad because you've clearly put a ton of work into this PR, and I don't
want to be throwing out "stop energy;" I'm just having a really tough time
reading through this and maintaining confidence that I know it's correct.

---

Could we somehow characterize in the PR description the general strategy
explaining what's happening in the middle commits - i.e.  why exactly are we
wanting to move code out of ThreadSync and into notification handler classes? I
understand that this probably has to do with keeping node code on the node, but
getting some kind of clear definition in the PR description might help. I.e.
which processes/threads which classes are executed on.

I don't have a good model that helps me understand, e.g., why we want to avoid
`FatalError()` in `ThreadSync()` and instead set `block_info.error`.

---

- [x] 257ef9f7b9 indexes, refactor: Remove index prune_violation code

Simple change; introduces `hasDataFromTipDown()` and moves. Some variable
renames.

- [x] 2f71f52b9b indexes, refactor: Remove index Init method

One of the keys to reviewing this commit is to compare Init() with
attachChain().

Basically, this move index initialization from `Index::Init()` into a combination of
`attachChain()` and the first `blockConnected()` call. BlockConnected events are
moved from being called within the same process to the BaseIndexNotifications
object which is attached to the Chain instance and holds a reference to the
index object itself.

- [x] ecedecac38 indexes, refactor: Remove index validationinterface hooks
- [x] 5e07d66a6d indexes, refactor: Stop incorrectly calling Interupt() and Stop() in BaseIndex destructor
- [x] c2ab79db68 indexes, refactor: Add Commit CBlockLocator& argument
- [x] f3d1bdae0e indexes, refactor: Remove remaining CBlockIndex* uses in index Rewind methods

Perhaps useful to keep in mind that the motivation for moving Rewind() from a
range of blocks to a single block at a time (Remove()) is to avoid usage of
CBlockIndex* entries.

- [x] a6d1c22dc1 indexes, refactor: Remove remaining CBlockIndex* uses in index CustomAppend methods
- [x] 8b63269e7c indexes, refactor: Move more new block logic out of ThreadSync to blockConnected
- [x] 1df5b0b6f9 indexes, refactor: Move Commit logic out of ThreadSync to notification handlers

Nice improvement to avoid duplicating commit/chainStateFlushed logic.

- [?] 15f8349271 indexes, refactor: Move Rewind logic out of Rewind to blockDisconnected and ThreadSync

Minor typo in the commit message: "This main thing" -> "The main thing".

This is the hardest commit for me to follow. It's distributing the contents
of `Rewind()` over `ThreadSync()` and `blockDisconnected()`.

I'm not sure how to decompose this to make it easier to follow, but it's a real
challenge for me to feel confident about this not changing behavior.

- [?] ed79c47c13 indexes, refactor: Move CustomInit and error handling code out of ThreadSync to notification handlers

I don't have a good model that helps me understand, e.g., why we want to avoid
`FatalError()` in `ThreadSync()` and instead set `block_info.error`.

- [x] 2897678732 indexes: Add blockfilterindex mutex
- [x] 53a1aa56af indexes, refactor: Move sync thread from index to node

Move-only stuff is pretty clear. So now the initial index sync is going to
happen all in the node process? Would there be a way to offload this to the
index processes?

- [x] ac61e33545 indexes, refactor: Remove SyncWithValidationInterfaceQueue call
- [ ] 2eceaee59f indexes: Rewrite chain sync logic, remove racy init
- [ ] e2f6c6ddf7 indexes: Initialize indexes without holding cs_main
- [ ] 3543161c82 indexes, refactor: Remove UndoReadFromDisk calls from indexing code
- [ ] 5cadd3636e indexes, refactor: Remove remaining CBlockIndex* pointers from indexing code
- [ ] f8a26680e9 Remove direct index -> node dependency
