## ----------------------------------------------------------------------
## FAIL: test_port_scanner_ip (__main__.UnitTests.test_port_scanner_ip)
## ----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/boilerplate-port-scanner/test_module.py", line 10, in test_port_scanner_ip
    self.assertEqual(actual, expected, 'Expected scanning ports of IP address to return [443].')
AssertionError: Lists differ: [] != [443]

Second list contains 1 additional elements.
First extra element 0:
443

- []
+ [443] : Expected scanning ports of IP address to return [443].

----------------------------------------------------------------------
Ran 8 tests in 178.581s

FAILED (failures=1)
