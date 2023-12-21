from ..interfaces import ActionConfig

__all__ = ("foo",)


def foo(config: ActionConfig = ActionConfig()):
    x = []  # [i for i in range(1000)]
    return x
