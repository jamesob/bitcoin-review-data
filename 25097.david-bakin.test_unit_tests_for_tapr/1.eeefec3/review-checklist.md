- [x] 12ae33708e Add new test utility methods; break out some existing ones

A lot of this code is fairly elaborate in terms of use of C++ templating
features - for example, all the machinations necessary to get `Hex()` to work -
which I think I'd be hesitant to include in non-test code. But since these are
tests, the complexity/convenience trade-off seems okay.

- [x] eeefec3435 Unit tests for Tap{root,script} of `interpreter.cpp`, #23279

- Might be good to break out that `ParseScriptError`/`ParseScriptFlags` optional change out into a separate commit, or fold it into the first commit.
