#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pwnlib.tubes

r = pwnlib.tubes.remote.remote("127.0.0.1", 1337)
r.sendline(
    b'(&<`#9]~<5Yz81Uwv-Q+*)MKnJ7H5F~DeAS@?P<<:(\\8I5WWlD1in@Pk+)K:`H$F"D~2}{?h=,vvc9s754J31l/EDhHA@)cC<A:^!\\6}4XEV0/SusrOp(Lm%I#"\'E%|{Abx>_{t:\\[Y6tml2Si/POe+Mba\'IG]\\"ZYB]{>ZSXv9ONr5KJn20/Ei,,Aec'
)

r.recvuntil(b"idek{", timeout=5)
print(r.recvuntil(b"}"))

exit(0)
