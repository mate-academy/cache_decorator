from typing import Any

import pytest


@pytest.fixture(autouse=True)
def clear_cache(request: Any) -> None:
    from app.main import clear_cache
    clear_cache()
