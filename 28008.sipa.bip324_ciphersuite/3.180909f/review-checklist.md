- [x] a1df59a185 crypto: remove outdated variant of ChaCha20Poly1305 AEAD
- [x] cacc8fe2b5 crypto: add the ChaCha20Poly1305 AEAD as specified in RFC8439
- [x] fbb1a9ef23 crypto: add FSChaCha20, a rekeying wrapper around ChaCha20
- [x] cf8c2b8327 crypto: add FSChaCha20Poly1305, rekeying wrapper around ChaCha20Poly1305
- [x] 8124f216fa bench: add benchmark for FSChaCha20Poly1305
- [x] f468ffdab8 crypto: support split plaintext in ChaCha20Poly1305 Encrypt/Decrypt
- [ ] 9e65744c4f Add BIP324Cipher, encapsulating key agreement, derivation, and stream/AEAD ciphers

Verified that `bip324_tests.cpp` faithfully matches the contents of the tests
performed by the Python implementation in the bip repo by regenerating the CPP
test vectors locally and diffing. Also compared the contents of
`run_test_vectors.py` to the CPP tests.

- [ ] 180909f2c8 tests: add decryption test to bip324_tests
