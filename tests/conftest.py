from py.xml import html
from config.common_methods import CommonMethods
import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """
        This is in-built method of pytest which executes as early as possible by using below decorator:
         @pytest.hookimpl(tryfirst=True)
        This method sets a customised run time html_report_path at the the starting of the test.
    """
    # creates dynamic folder at run time
    report_path = CommonMethods().create_new_folder
    report = report_path + "/my_report.html"

    # adjust plugin options
    config.option.htmlpath = report
    config.option.self_contained_html = True


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_header(cells):
    """
        Marker @pytest.hookimpl(optionalhook=True) enables optionalhook
        and this method inserts the table headers in the report.
    """
    cells.insert(2, html.th('Request Json'))
    cells.insert(3, html.th('Response Json'))
    cells.insert(4, html.th('Status Code'))


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    """
        Marker @pytest.hookimpl(optionalhook=True) enables optionalhook
        and this method inserts the table rows and respective data in the report.
    """
    cells.insert(2, html.td(report.request_json))
    cells.insert(3, html.td(report.response_text))
    cells.insert(4, html.td(report.status))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
        Marker @pytest.hookimpl(hookwrapper=True) wraps the execution of other hook implementations.
        This funntion yields report with desired data.
    """
    outcome = yield
    report = outcome.get_result()
    report.request_json = getattr(item, 'request_json', 'request_json')
    report.response_text = getattr(item, 'response_text', 'response_text')
    report.status = getattr(item, 'status', 'status')
