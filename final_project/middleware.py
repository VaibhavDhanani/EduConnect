class UserDetailsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        name = request.COOKIES.get("name", "default")
        role = request.COOKIES.get("role", "default")
        uid = request.COOKIES.get("uid", "default")

        request.user_name = name
        request.user_role = role
        request.user_id = uid

        response = self.get_response(request)
        return response
