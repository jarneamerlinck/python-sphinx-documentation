import pytest

def test_base_import():
    import packagename_jarne
def test_submodule_import():
    import packagename_jarne.submodule
def test_PID_import():
    import packagename_jarne.PID
def test_package_version():
    import packagename_jarne.PID