import requests

# 선택할 곳에 커서두기
# 쉬프트
# 페이지
def test_local_get_hello(base_url_local):
    """
    로컬 API(/hello) GET 테스트
    """
    url = f"{base_url_local}/hello"

    response = requests.get(url)

    assert response.status_code == 200
