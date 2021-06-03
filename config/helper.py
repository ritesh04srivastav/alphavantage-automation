from config import config
import requests


def build_service_url(symbol, output, api_key=config.VALID_API_KEY):
    function_url = 'function=' + config.FUNCTION_TIME_DAILY
    api_key_url = 'apikey=' + api_key
    symbol_url = 'symbol=' + symbol
    output_url = 'outputsize=' + output + '&'
    service_url = config.BASE_URL + function_url + '&' + symbol_url + '&' + output_url + api_key_url

    return service_url


def submit_request(method_type, service_url, request_json, headers=None):
    if headers is None:
        headers = {}
    response = requests.request(method_type, service_url, headers=headers, data=request_json)
    return response


def export_result_to_html_report(request,response_text,request_json,status):
    request.node.response_text = response_text
    request.node.request_json = request_json
    request.node.status = status
