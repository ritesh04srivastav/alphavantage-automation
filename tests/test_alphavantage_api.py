from config import config
import pytest
from config.config import INVALID_SYMBOL_TEXT, INVALID_API_TEXT, THROTTLE_TEXT
from config.helper import build_service_url, submit_request, export_result_to_html_report, validate_response


def test_get_times_daily_ibm(request):
    # sc1: symbol=IBM and outputsize=default

    service_url = build_service_url(config.SYMBOL_IBM, config.DEFAULT_OUTPUT_SIZE)
    request_json = {}
    response = submit_request("GET", service_url, request_json)
    validate_response(response,'Symbol": "IBM"')
    validate_response(response,' Output Size": "Compact"')
    export_result_to_html_report(request,response.text,request_json,response.status_code)


def test_get_times_daily_ibm_output_full(request):
    # sc2: symbol=IBM and outputsize=full

    service_url = build_service_url(config.SYMBOL_IBM, config.FULL_OUTPUT_SIZE)
    request_json = {}
    response = submit_request("GET", service_url, request_json)
    validate_response(response, 'Symbol": "IBM"')
    validate_response(response, 'Output Size": "Full size"')
    export_result_to_html_report(request, response.text, request_json, response.status_code)


def test_get_times_daily_tsco_output_default(request):
    # sc3: symbol=TSCO.LON and outputsize=default

    service_url = build_service_url(config.SYMBOL_TSCO, config.DEFAULT_OUTPUT_SIZE)
    request_json = {}
    response = submit_request("GET", service_url, request_json)
    validate_response(response, 'Symbol": "TSCO.LON"')
    validate_response(response, 'Output Size": "Compact"')
    export_result_to_html_report(request, response.text, request_json, response.status_code)


@pytest.mark.invalid
def test_get_times_daily_invalid_symbol(request):
    # sc4: invalid symbol

    service_url = build_service_url(config.INVALID_SYMBOL, config.DEFAULT_OUTPUT_SIZE)
    request_json = {}
    response = submit_request("GET", service_url, request_json)
    validate_response(response, INVALID_SYMBOL_TEXT)
    export_result_to_html_report(request, response.text, request_json, response.status_code)


@pytest.mark.invalid
def test_get_times_daily_invalid_api_key(request):
    # sc5: invalid api key

    service_url = build_service_url(config.SYMBOL_IBM, config.DEFAULT_OUTPUT_SIZE,api_key=config.INVALID_API_KEY)
    request_json = {}
    response = submit_request("GET", service_url, request_json)
    validate_response(response, INVALID_API_TEXT)
    export_result_to_html_report(request, response.text, request_json, response.status_code)


@pytest.mark.invalid
def test_get_exceeds_throttle_limit(request):
    # sc6: throttle_limit > 5 per minute
    service_url = build_service_url(config.SYMBOL_IBM, config.DEFAULT_OUTPUT_SIZE)
    request_json = {}
    for i in range(0, 6):
        response = submit_request("GET", service_url, request_json)
        if i > 4:
            validate_response(response, THROTTLE_TEXT)
            export_result_to_html_report(request, response.text, request_json, response.status_code)
            break
