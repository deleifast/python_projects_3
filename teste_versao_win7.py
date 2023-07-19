__intname__ = 'tests.windows_tools.registry'
__author__ = 'Orsiris de Jong'
__copyright__ = 'Copyright (C) 2020-2021 Orsiris de Jong'
__licence__ = 'BSD 3 Clause'
__build__ = '2021052501'

__intname__ = 'tests.windows_tools.product_key'
__author__ = 'Orsiris de Jong'
__copyright__ = 'Copyright (C) 2020-2021 Orsiris de Jong'
__licence__ = 'BSD 3 Clause'
__build__ = '2021031601'

import re, platform, six

from windows_tools.product_key import *
from windows_tools.registry import *


def test_get_value():
    product_name = get_value(hive=HKEY_LOCAL_MACHINE, key=r'SOFTWARE\Microsoft\Windows NT\CurrentVersion',
                             value='ProductName', arch=KEY_WOW64_32KEY | KEY_WOW64_64KEY)
    print('Product Name: %s' % product_name)
    assert product_name.startswith('Windows'), 'product_name should start with "Windows"'


def test_get_values():
    uninstall = get_values(hive=HKEY_LOCAL_MACHINE, key=r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
                           names=['DisplayName', 'Version'], arch=KEY_WOW64_32KEY | KEY_WOW64_64KEY)
    print(uninstall)
    assert isinstance(uninstall[0], dict), 'get_values() should return list of dict'
    assert len(uninstall[0]) > 0, 'get_values() should return at least one installed product'


def test_get_keys():
    uninstall_recursive = get_keys(hive=HKEY_LOCAL_MACHINE, key=r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
                                   recursion_level=2,
                                   filter_on_names=['DisplayName', 'Version'], arch=KEY_WOW64_32KEY | KEY_WOW64_64KEY)
    print(uninstall_recursive)
    assert isinstance(uninstall_recursive,
                      dict), 'get_keys() should return a dict with entries per key, containing dict or lists'
    assert len(uninstall_recursive) > 0, 'get_keys() should return at least one softwre to uninstall'


if __name__ == '__main__':
#    print('Example code for %s, %s' % (__intname__, __build__))
    test_get_value()
#    test_get_values()
#    test_get_keys()

PRODUCT_KEY_REGEX = r'([A-Z0-9]{5}-){4}[A-Z0-9]{5}'


def test_get_windows_product_key_from_wmi():
    wmi_key = get_windows_product_key_from_wmi()
    print('Key from WMI: "{}"'.format(wmi_key))
    if wmi_key is not None and wmi_key != "":
        assert re.match(PRODUCT_KEY_REGEX, wmi_key), 'Found product key matches product key format'


def test_get_windows_product_key_from_reg():
    reg_key = get_windows_product_key_from_reg()
    print('Key from REG: "{}"'.format(reg_key))
    if reg_key is not None and reg_key != "":
        assert re.match(PRODUCT_KEY_REGEX, reg_key), 'Found product key matches product key format'


if __name__ == '__main__':
#    print('Example code for %s, %s' % (__intname__, __build__))
    test_get_windows_product_key_from_wmi()
#    test_get_windows_product_key_from_reg()
print ("Maquina: " + platform.machine())
print ("Rede: " + platform.node())

six.moves.input( 'Pressione <ENTER> para sair...' )
