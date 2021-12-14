from dbt.adapters.spark_custom.connections import SparkConnectionManager  # noqa
from dbt.adapters.spark_custom.connections import SparkCredentials
from dbt.adapters.spark_custom.relation import SparkRelation  # noqa
from dbt.adapters.spark_custom.column import SparkColumn  # noqa
from dbt.adapters.spark_custom.impl import SparkAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import spark_custom

Plugin = AdapterPlugin(
    adapter=SparkAdapter,
    credentials=SparkCredentials,
    include_path=spark_custom.PACKAGE_PATH)
