import json
import requests


def test_get_songs_all():
    response = requests.get("http://127.0.0.1:8000/songs")
    assert len(response.json()) != 0
    assert response.status_code == 200


def test_get_audiobooks_all():
    response = requests.get("http://127.0.0.1:8000/audiobooks")
    assert len(response.json()) != 0
    assert response.status_code == 200


def test_get_podcasts_all():
    response = requests.get("http://127.0.0.1:8000/audiobooks")
    assert len(response.json()) != 0
    assert response.status_code == 200


def test_post_audiobook():
    data = {
        "title": "1984",
        "duration": "3544",
        "uploaded_time": "2021-05-08T13:33:44.645000",
        "author": "Geroge Orwell",
        "narrator": "Mr X"
    }
    response = requests.post(
        "http://127.0.0.1:8000/audiobooks",
        data=json.dumps(data)
    )
    assert len(response.json()) != 0
    assert response.status_code == 200
    # Following is the teardown process
    requests.delete(f"http://127.0.0.1:8000/audiobooks/{response.json().get('id')}")


def test_post_song():
    data = {
        "title": "Hurt",
        "duration": "3544",
        "uploaded_time": "2021-05-08T13:33:44.645000",
    }
    response = requests.post(
        "http://127.0.0.1:8000/songs",
        data=json.dumps(data)
    )
    assert len(response.json()) != 0
    assert response.status_code == 200
    # Following is the teardown process
    requests.delete(f"http://127.0.0.1:8000/songs/{response.json().get('id')}")


def test_post_podcasts():
    data = {
        "title": "Lore",
        "duration": "3544",
        "uploaded_time": "2021-05-08T13:33:44.645000",
        "host": "Aaron Manke"
    }
    response = requests.post(
        "http://127.0.0.1:8000/podcasts",
        data=json.dumps(data)
    )
    assert len(response.json()) != 0
    assert response.status_code == 200
    # Following is the teardown process
    requests.delete(f"http://127.0.0.1:8000/podcasts/{response.json().get('id')}")


def test_post_podcasts_with_optional_participants():
    data = {
        "title": "Spooked",
        "duration": "3544",
        "uploaded_time": "2021-05-08T13:33:44.645000",
        "host": "JT",
        "participants": ["JT", "P Pan", "Mr Y"]
    }
    response = requests.post(
        "http://127.0.0.1:8000/podcasts",
        data=json.dumps(data)
    )
    assert len(response.json()) != 0
    assert response.status_code == 200
    # Deleting created object to keep the database sanitized
    requests.delete(f"http://127.0.0.1:8000/podcasts/{response.json().get('id')}")


def test_post_podcasts_too_many_participants():
    """
    This should fail, more than 20 participants are not allowed
    """
    data = {
        "title": "Lore",
        "duration": "3544",
        "uploaded_time": "2021-05-08T13:33:44.645000",
        "host": "Aaron Manke",
        "participants": ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    }
    response = requests.post(
        "http://127.0.0.1:8000/podcasts",
        data=json.dumps(data)
    )
    assert response.status_code == 500


def test_get_and_delete_song():
    data = {
        "title": "Hurting",
        "duration": "3544",
        "uploaded_time": "2021-05-08T13:33:44.645000",
    }
    response = requests.post(
        "http://127.0.0.1:8000/songs",
        data=json.dumps(data)
    )
    get_response = requests.get(f"http://127.0.0.1:8000/songs/{response.json().get('id')}")
    assert len(get_response.json()) != 0
    assert get_response.status_code == 200
    delete_response = requests.delete(f"http://127.0.0.1:8000/songs/{response.json().get('id')}")
    assert delete_response.status_code == 200


def test_get_and_delete_podcast():
    data = {
        "title": "Lore",
        "duration": "3544",
        "uploaded_time": "2021-05-08T13:33:44.645000",
        "host": "Aaron Manke"
    }
    response = requests.post(
        "http://127.0.0.1:8000/podcasts",
        data=json.dumps(data)
    )
    get_response = requests.get(f"http://127.0.0.1:8000/podcasts/{response.json().get('id')}")
    assert len(get_response.json()) != 0
    assert get_response.status_code == 200
    delete_response = requests.delete(f"http://127.0.0.1:8000/podcasts/{response.json().get('id')}")
    assert delete_response.status_code == 200


def test_get_and_delete_audiobook():
    data = {
        "title": "1984",
        "duration": "3544",
        "uploaded_time": "2021-05-08T13:33:44.645000",
        "author": "Geroge Orwell",
        "narrator": "Mr X"
    }
    response = requests.post(
        "http://127.0.0.1:8000/audiobooks",
        data=json.dumps(data)
    )
    get_response = requests.get(f"http://127.0.0.1:8000/audiobooks/{response.json().get('id')}")
    assert len(get_response.json()) != 0
    assert get_response.status_code == 200
    delete_response = requests.delete(f"http://127.0.0.1:8000/audiobooks/{response.json().get('id')}")
    assert delete_response.status_code == 200





