# Copyright 2015 Internap.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from unittest import TestCase

from flexmock import flexmock
from netman.core.objects.switch_base import SwitchOperations


class BackwardCompatibleSwitchOperationsTest(TestCase):
    def setUp(self):
        self.switch = flexmock(SwitchOperations())

    def test_remove_access_vlan_call_unset_access_vlan(self):
        self.switch.should_receive("unset_access_vlan").with_args(1000).once()

        self.switch.remove_access_vlan(1000)



