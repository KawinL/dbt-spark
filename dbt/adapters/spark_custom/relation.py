from typing import Optional

from dataclasses import dataclass

from dbt.adapters.base.relation import BaseRelation, Policy
from dbt.exceptions import RuntimeException


@dataclass
class SparkQuotePolicy(Policy):
    database: bool = False
    schema: bool = False
    identifier: bool = False


@dataclass
class SparkIncludePolicy(Policy):
    database: bool = False
    schema: bool = True
    identifier: bool = True


@dataclass(frozen=True, eq=False, repr=False)
class SparkRelation(BaseRelation):
    quote_policy: SparkQuotePolicy = SparkQuotePolicy()
    include_policy: SparkIncludePolicy = SparkIncludePolicy()
    print('init spark relation', include_policy)
    quote_character: str = '`'
    is_delta: Optional[bool] = None
    is_hudi: Optional[bool] = None
    information: str = None

    def __post_init__(self):
        print('post init spark relation', self.include_policy)
        if self.database != self.schema and self.database:
            raise RuntimeException('Cannot set database in spark!')

    def render(self):
        print('render spark relation', self.include_policy)
        print('database', self.database, self.database is not None)
        # self.include_policy.database=False

        if self.include_policy.database and self.include_policy.schema:
            self.include_policy.database=False
            raise RuntimeException(
                'Got a spark relation with schema and database set to '
                'include, but only one can be set'
            )
        
        return super().render()
