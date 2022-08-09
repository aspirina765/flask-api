from unittest.mock import patch, Mock
import sys

class TestServer():
    @staticmethod
    def test_get_r(test_client):
        response = test_client.get('/r')
        assert response.status_code == 200
        assert b'pong' in response.data
    def test_get_d(test_client):
        response = test_client.get('/d')
        assert response.status_code == 200
        assert b'pong' in response.data
    def test_get_dly(test_client):
        response = test_client.get('/dly')
        assert response.status_code == 200
        assert b'pong' in response.data
