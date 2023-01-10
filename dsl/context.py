from typing import Any, Dict, Optional


class Context:
    def __init__(self, parent: Optional['Context'] = None):
        self.parent: Context = parent
        self.symbols: Dict[str, Any] = {}
        self.var_count: int = 0

    def make_child(self):
        return Context(self)

    def define(self, name: str, value: Any):
        self.symbols[name] = value

    def resolve(self, name: str) -> Optional[Any]:
        if name in self.symbols:
            return self.symbols[name]
        if self.parent:
            return self.parent.resolve(name)
        return None
