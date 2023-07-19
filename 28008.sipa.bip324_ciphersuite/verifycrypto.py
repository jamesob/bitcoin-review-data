#!/usr/bin/env python3
from chacha20poly1305 import ChaCha20Poly1305

fh = bytearray.fromhex

print("vector 2.8.2")

plaintext_from_test = fh(
"4c616469657320616e642047656e746c656d656e206f662074686520636c6173"
"73206f66202739393a204966204920636f756c64206f6666657220796f75206f"
"6e6c79206f6e652074697020666f7220746865206675747572652c2073756e73"
"637265656e20776f756c642062652069742e"
)

assert plaintext_from_test.decode() == "Ladies and Gentlemen of the class of '99: If I could offer you only one tip for the future, sunscreen would be it."

key_from_test = fh(
"808182838485868788898a8b8c8d8e8f909192939495969798999a9b9c9d9e9f"
)

nonce_from_test = fh(
"07000000" "4041424344454647"
)

aad_from_test = fh(
"50515253c0c1c2c3c4c5c6c7"
)

cip = ChaCha20Poly1305(key_from_test)
res = cip.encrypt(nonce_from_test, plaintext_from_test, aad_from_test)

# print(res.hex())
assert res.hex() == (
"d31a8d34648e60db7b86afbc53ef7ec2a4aded51296e08fea9e2b5a736ee62d6"
"3dbea45e8ca9671282fafb69da92728b1a71de0a9e060b2905d6a5b67ecd3b36"
"92ddbd7f2d778b8c9803aee328091b58fab324e4fad675945585808b4831d7bc"
"3ff4def08e4b7a9de576d26586cec64b61161ae10b594f09e26a7e902ecbd060"
"0691"
)
print("✓ test replicates 2.8.2 vector")


print("vector A.5")

plaintext = fh(
"496e7465726e65742d4472616674732061726520647261667420646f63756d65"
"6e74732076616c696420666f722061206d6178696d756d206f6620736978206d"
"6f6e74687320616e64206d617920626520757064617465642c207265706c6163"
"65642c206f72206f62736f6c65746564206279206f7468657220646f63756d65"
"6e747320617420616e792074696d652e20497420697320696e617070726f7072"
"6961746520746f2075736520496e7465726e65742d4472616674732061732072"
"65666572656e6365206d6174657269616c206f7220746f206369746520746865"
"6d206f74686572207468616e206173202fe2809c776f726b20696e2070726f67"
"726573732e2fe2809d"
)

aad = fh(
"f33388860000000000004e91"
)


key = fh(
"1c9240a5eb55d38af333888604f6b5f0473917c1402b80099dca5cbc207075c0"
)

nonce = fh(
"00000000" "0102030405060708"
)

cip2 = ChaCha20Poly1305(key)
res2 = cip2.encrypt(nonce, plaintext, aad)

# print(res2.hex())
assert res2.hex() == (
"64a0861575861af460f062c79be643bd5e805cfd345cf389f108670ac76c8cb2"
"4c6cfc18755d43eea09ee94e382d26b0bdb7b73c321b0100d4f03b7f355894cf"
"332f830e710b97ce98c8a84abd0b948114ad176e008d33bd60f982b1ff37c855"
"9797a06ef4f0ef61c186324e2b3506383606907b6a7c02b0f9f6157b53c867e4"
"b9166c767b804d46a59b5216cde7a4e99040c5a40433225ee282a1b0a06c523e"
"af4534d7f83fa1155b0047718cbc546a0d072b04b3564eea1b422273f548271a"
"0bb2316053fa76991955ebd63159434ecebb4e466dae5a1073a6727627097a10"
"49e617d91d361094fa68f0ff77987130305beaba2eda04df997b714d6c6f2c29"
"a6ad5cb4022b02709beead9d67890cbb22392336fea1851f38"
)
print("✓ test replicates A.5 vector")


def int_to_hex(value, n):
    # Each byte has 2 hex characters. So, the number of hex characters should be n*2
    return hex(value)[2:].zfill(n*2)

def rev_byte_order(hexstr: str):
    # Reversing the byte order
    return ''.join(reversed([hexstr[i:i+2] for i in range(0, len(hexstr), 2)]))


def do_encrypt(plaintext: str, aad: str, key: str, nonce_tuple: tuple[int, int]) -> str:
    nonce = rev_byte_order(int_to_hex(nonce_tuple[0], 4)) + rev_byte_order(int_to_hex(nonce_tuple[1], 8))
    # print(nonce)
    cip = ChaCha20Poly1305(fh(key))
    return cip.encrypt(fh(nonce), fh(plaintext), fh(aad) if aad else None)


def TestChaCha20Poly1305(
        plaintext: str,
        aad: str,
        key: str,
        nonce_tuple: tuple[int, int],
        expected_cipher: str):
    """Perform test vectors as they appear in Core, but with an unrelated Python implementation of ChaCha20Poly1305."""
    result = do_encrypt(plaintext, aad, key, nonce_tuple)
    assert result.hex() == expected_cipher


print("non-RFC vectors")
TestChaCha20Poly1305("8d2d6a8befd9716fab35819eaac83b33269afb9f1a00fddf66095a6c0cd91951"
                     "a6b7ad3db580be0674c3f0b55f618e34",
                     "",
                     "72ddc73f07101282bbbcf853b9012a9f9695fc5d36b303a97fd0845d0314e0c3",
                     [0x3432b75f, 0xb3585537eb7f4024],
                     "f760b8224fb2a317b1b07875092606131232a5b86ae142df5df1c846a7f6341a"
                     "f2564483dd77f836be45e6230808ffe402a6f0a3e8be074b3d1f4ea8a7b09451");
TestChaCha20Poly1305("",
                     "36970d8a704c065de16250c18033de5a400520ac1b5842b24551e5823a3314f3"
                     "946285171e04a81ebfbe3566e312e74ab80e94c7dd2ff4e10de0098a58d0f503",
                     "77adda51d6730b9ad6c995658cbd49f581b2547e7c0c08fcc24ceec797461021",
                     [0x1f90da88, 0x75dafa3ef84471a4],
                     "aaae5bb81e8407c94b2ae86ae0c7efbe");

print("✓ test replicates non-RFC vectors")
