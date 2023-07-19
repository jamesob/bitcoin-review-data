- [x] df1e25d68f crypto: remove outdated variant of ChaCha20Poly1305 AEAD
- [x] 26a7c254dc crypto: add the ChaCha20Poly1305 AEAD as specified in RFC8439

Verified that test vectors match those from the RFC documents.

- [ ] 2b1241f5cb crypto: add FSChaCha20, a rekeying wrapper around ChaCha20
- [ ] c61fa6ab59 crypto: add FSChaCha20Poly1305, rekeying wrapper around ChaCha20Poly1305
- [ ] 19880ea18a bench: add benchmark for FSChaCha20Poly1305
- [ ] 3ce01712b2 crypto: support split plaintext in ChaCha20Poly1305 Encrypt/Decrypt
- [ ] 3c5d629cdf Add BIP324Cipher, encapsulating key agreement, derivation, and stream/AEAD ciphers
- [ ] b0b6d11f16 tests: add decryption test to bip324_tests
