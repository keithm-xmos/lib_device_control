#!/usr/bin/env python
import xmostest

def runtest():
    testlevel = 'smoke'
    resources = xmostest.request_resource('xsim')

    binary = 'test_xscope/bin/test_xscope.xe'.format()
    tester = xmostest.ComparisonTester(open('xscope.expect'),
                                       'lib_device_control',
                                       'lib_device_control_transport_tests',
                                       'transport_test_%s' % testlevel,
                                       {})
    tester.set_min_testlevel(testlevel)
    xmostest.run_on_simulator(resources['xsim'], binary, simargs=[], tester=tester)

    binary = 'test_usb/bin/test_usb.xe'.format()
    tester = xmostest.ComparisonTester(open('usb.expect'),
                                       'lib_device_control',
                                       'lib_device_control_transport_tests',
                                       'transport_test_%s' % testlevel,
                                       {})
    tester.set_min_testlevel(testlevel)
    xmostest.run_on_simulator(resources['xsim'], binary, simargs=[], tester=tester)

    binary = 'test_i2c/bin/test_i2c.xe'.format()
    tester = xmostest.ComparisonTester(open('i2c.expect'),
                                       'lib_device_control',
                                       'lib_device_control_transport_tests',
                                       'transport_test_%s' % testlevel,
                                       {})
    tester.set_min_testlevel(testlevel)
    xmostest.run_on_simulator(resources['xsim'], binary, simargs=[], tester=tester)