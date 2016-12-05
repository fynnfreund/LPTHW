from nose.tools import *
from app import app
from tests.tools import assert_response


client = app.test_client() # create a testing client (like a fake web browser)
client.testing = True # enable this so that errors in your web app bubble up to the testing client

def test_index():
    global client
    resp = client.get('/')
    assert_response(resp, status=302)

    resp = client.get('/game')
    assert_response(resp) # just to make sure to get a valid response

    resp = client.post('/game')
    assert_response(resp, contains="You Died!")

    # go to another scene in the game
    testdata = {'userinput': 'tell a joke'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="LaserWeaponArmory")

    # from there, go to yet another scene
    testdata = {'userinput': '132'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="The Bridge")
