def callLimit(limit: int):
    """Decorator for callLimit"""
    count = 0

    def callLimiter(function):
        """Outer function for wrapper"""
        def limit_function(*args: any, **kwds: any):
            """Actual wrapper (passes args, kwds, and calls function)"""
            try:
                nonlocal count
                if count >= limit:
                    raise RuntimeError(function, 'call too many times')
                count += 1
                function(*args, **kwds)
            except BaseException as e:
                print(type(e).__name__, ":", e)

        return limit_function

    return callLimiter
