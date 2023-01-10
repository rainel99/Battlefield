from typing import Any, Dict, Optional


class Context:
    def __init__(self, parent: Optional['Context'] = None):
        self.parent: Context = parent
        self.symbols: Dict[str, Any] = {}
        self.var_count: int = 0

    def asing_value(self, name: str, value: Any):
        self.symbols[name] = value

    def find_value(self, name: str) -> Optional[Any]:
        if name in self.symbols:
            return self.symbols[name]
        if self.parent:
            return self.parent.find_value(name)
        return None
