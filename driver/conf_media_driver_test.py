# Copyright (c) 2019 Intel Corporation
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pathlib import Path

INSTALL = ['media-driver']
# TODO: Temporarily hardcoded path. Prepare test scripts automatically
TEST_SCRIPT_PATH = Path('/localdisk/driver_test_scripts')
TESTS = [
    'CABA1_SVA_B',
    'CABA1_Sony_D',
    'avc_cbr_001',
    'avc_cqp_001',
    'scale_001'
]

for test_id in TESTS:
    action(f'Run test {test_id}',
           work_dir=TEST_SCRIPT_PATH,
           cmd=f'./run_test.sh {test_id}')
