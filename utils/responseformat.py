from rest_framework import status


def success_response(data=None):
    content = {
        'response_code': status.HTTP_200_OK,
        'success': True,
        'message': "success",
        'data': data,
    }
    return content


def fail_response(data=None, code=status.HTTP_500_INTERNAL_SERVER_ERROR):
    content = {
        'response_code': code,
        'success': False,
        'message': "success",
        'data': data,
    }
    return content
