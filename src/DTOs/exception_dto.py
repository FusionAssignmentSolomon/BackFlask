from dataclasses import dataclass
from typing import Optional

from dataclasses_json import DataClassJsonMixin


@dataclass
class ExceptionDTO(DataClassJsonMixin):
    status_code: int
    general_error_message: str
    custom_error_message: Optional[str] = None
