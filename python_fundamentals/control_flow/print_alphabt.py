#!/usr/bin/env python3

print("{}".format("".join(chr(letter) for letter in range(ord('a'),
      ord('z') + 1) if chr(letter) not in "qe")), end="")

