from nose.tools import *
from map import *

def test_gothon_game_map():
    assert_equal(START.go('shoot!'), try_again)
    assert_equal(START.go('dodge!'), try_again)
    room = START.go('tell a joke')
    assert_equal(room, laser_weapon_armory)
