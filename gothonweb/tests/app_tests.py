from nose.tools import *
from app import app
from tests.tools import assert_response


client = app.test_client() # create a testing client (like a fake web browser) - global variable
client.testing = True # enable this so that errors in your web app bubble up to the testing client

def test_index():
    global client # get the variable client
    resp = client.get('/') # get this route url / and save/put info in resp
    assert_response(resp, status=302) # redirect status is 302

    resp = client.get('/game')
    assert_response(resp) # just to make sure to get a valid response

    resp = client.post('/game') # use POST, but provide no data
    assert_response(resp, contains="You Died!")

    # go to another scene in the game
    testdata = {'userinput': 'tell a joke'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Laser Weapon Armory")

    # from there, go to yet another scene
    testdata = {'userinput': '132'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="The Bridge")
