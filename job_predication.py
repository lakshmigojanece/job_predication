import pandas as pd
from sqlalchemy import create_engine

# -----------------------------
# STEP 1: LOAD CSV FILE
# -----------------------------
csv_path = r"C:\Users\Lakshmiveni\Downloads\HR_Job_Placement_Dataset (2).csv"
df = pd.read_csv(csv_path)

print("CSV loaded successfully")
print(df.head())
print("Shape:", df.shape)

# -----------------------------
# STEP 2: CONNECT TO MYSQL
# -----------------------------
mysql_user = "root"
mysql_password = "root"
mysql_host = "localhost"
mysql_port = 3306
mysql_db = "job_prediction_3"

engine = create_engine(
    f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}"
)

print("MySQL connected")

# -----------------------------
# STEP 3: UPLOAD DATA TO MYSQL
# -----------------------------
table_name = "job_prediction"
df.to_sql(table_name, con=engine, if_exists="replace", index=False)

print("Data uploaded to MySQL")
