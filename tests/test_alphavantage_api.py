from config import config
import pytest
from config.helper import build_service_url, submit_request, export_result_to_html_report


def test_get_times_daily_ibm(request):
    # sc1: symbol=IBM and outputsize=default

    service_url = build_service_url(config.SYMBOL_IBM, config.DEFAULT_OUTPUT_SIZE)
    request_json = {}
    response = submit_request("GET", service_url, request_json)
    assert response.status_code == 200
    export_result_to_html_report(request,response.text,request_json,response.status_code)


def test_get_times_daily_ibm_output_full(request):
    # sc2: symbol=IBM and outputsize=full

    service_url = build_service_url(config.SYMBOL_IBM, config.FULL_OUTPUT_SIZE)
    request_json = {}
    response = submit_request("GET", service_url, request_json)
    assert response.status_code == 200
    export_result_to_html_report(request, response.text, request_json, response.status_code)


def test_get_times_daily_tsco_output_default(request):
    # sc3: symbol=TSCO.LON and outputsize=default

    service_url = build_service_url(config.SYMBOL_TSCO, config.DEFAULT_OUTPUT_SIZE)
    request_json = {}
    response = submit_request("GET", service_url, request_json)
    assert response.status_code == 200
    export_result_to_html_report(request, response.text, request_json, response.status_code)


@pytest.mark.invalid
def test_get_times_daily_invalid_symbol(request):
    # sc4: invalid symbol

    service_url = build_service_url(config.INVALID_SYMBOL, config.DEFAULT_OUTPUT_SIZE)
    request_json = {}
    response = submit_request("GET", service_url, request_json)
    assert response.status_code == 200
    assert 'Invalid API call. Please retry or visit the documentation' in response.text
    export_result_to_html_report(request, response.text, request_json, response.status_code)


@pytest.mark.invalid
def test_get_times_daily_invalid_api_key(request):
    # sc5: invalid api key

    service_url = build_service_url(config.SYMBOL_IBM, config.DEFAULT_OUTPUT_SIZE,api_key=config.INVALID_API_KEY)
    request_json = {}
    response = submit_request("GET", service_url, request_json)
    assert response.status_code == 200
    assert 'the parameter apikey is invalid or missing' in response.text
    export_result_to_html_report(request, response.text, request_json, response.status_code)


@pytest.mark.invalid
def test_get_exceeds_throttle_limit(request):
    # sc6: throttle_limit > 5 per minute
    service_url = build_service_url(config.SYMBOL_IBM, config.DEFAULT_OUTPUT_SIZE)
    request_json = {}
    for i in range(0, 6):
        response = submit_request("GET", service_url, request_json)
        assert response.status_code == 200
        if i > 4:
            assert (config.THROTTLE_TEXT in response.text)
            export_result_to_html_report(request, response.text, request_json, response.status_code)
            break
