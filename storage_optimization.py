# Databricks notebook / PySpark script
def maintain_tables(catalog: str, schema: str, table_names: list, vacuum_retain_hours: int = 168):
    for table_name in table_names:
        full_table_name = f"`{catalog}`.`{schema}`.`{table_name}`"
        print(f"Running maintenance on {full_table_name}")
        try:
            spark.sql(f"OPTIMIZE {full_table_name}")
            print(f"OPTIMIZE completed for {full_table_name}")
            spark.sql(f"VACUUM {full_table_name} RETAIN {vacuum_retain_hours} HOURS")
            print(f"VACUUM completed for {full_table_name}")
            spark.sql(f"ANALYZE TABLE {full_table_name} COMPUTE STATISTICS")
            print(f"ANALYZE completed for {full_table_name}")
        except Exception as e:
            print(f"Error while processing {full_table_name}: {str(e)}")
    print("Maintenance run finished.")
# Example usage
catalog = "main"
schema = "sales"
table_names = ["orders", "customers", "transactions"]

maintain_tables(catalog, schema, table_names)
