from typing import List
from dataclasses import dataclass, field, InitVar


@dataclass
class Updates():
    updates_json: InitVar[List['Update']]
    updates: List = field(default_factory=list)

    def __post_init__(self, updates_json):
        if updates_json:
            self.updates = [Update(update_dict)
                            for update_dict in updates_json]

    def __getitem__(self, key):
        return self.updates[key]

    def is_empty(self):
        return True if len(self.updates) == 0 else False


@dataclass
class Update():
    update: dict

    def get(self, key):
        return self.update[key]
    
    def __getitem__(self, key):
        return self.update[key]
