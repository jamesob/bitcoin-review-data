- [x] faa921f78 move-only: Add util/hash_type
- [x] 000000770 refactor: Remove unused code
- [x] fa5668bfb refactor: Use type-safe assumeutxo hash
- [x] fae33f98e Fix assumeutxo crash due to invalid base_blockhash
- [x] fa340b879 refactor: Avoid magic value of all-zeros in assumeutxo base_blockhash

Nice change; cleans up not only the crash bug but removes special 
interpretation of the `00000...` hash as null.
