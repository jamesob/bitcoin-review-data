- [x] a1df59a185 crypto: remove outdated variant of ChaCha20Poly1305 AEAD
- [x] cacc8fe2b5 crypto: add the ChaCha20Poly1305 AEAD as specified in RFC8439
- [x] 5e0ca4ba37 crypto: add FSChaCha20, a rekeying wrapper around ChaCha20
- [x] c8a9cc079a crypto: add FSChaCha20Poly1305, rekeying wrapper around ChaCha20Poly1305
- [x] 4b0e3823bd bench: add benchmark for FSChaCha20Poly1305
- [x] df4303b996 crypto: support split plaintext in ChaCha20Poly1305 Encrypt/Decrypt

Most easily reviewed with `--color-moved=dimmed-zebra --color-moved-ws=ignore-all-space`, especially for the test changes.

- [ ] 19d3358ea7 Add BIP324Cipher, encapsulating key agreement, derivation, and stream/AEAD ciphers
- [ ] d377aa6086 tests: add decryption test to bip324_tests
