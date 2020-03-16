"""
This script compares the column headings from a spreadsheet to the field names from a SQL table. The purpose is to
verify that the column name matches the field name for import purposes.

Author: Jeffrey C. Belknap
Date: February 7, 2020
"""

spreadsheet_column_names = [
    "source",
    "dateTime",
    "fundId",
    "fundName",
    "oneMth",
    "threeMth",
    "sixMth",
    "forecast",
    "oneDayChg",
    "fiveDayChg",
    "tradeThreshold",
    "currentState",
    "sizedEquityRatio",
    "actualEquityRatio",
    "targetVol",
    "rpmVol",
    "modelName",
    "date1DayPast",
    "retOneDayPast",
    "date2DayPast",
    "retTwoDayPast",
    "trendIndicator",
    "stressFilterMultiplier",
    "adjStressVolCap",
    "modelNameCore",
    "adjCoreVolCap",
    "forecastCore",
    "sizeEquityRatioCore",
    "equityRatioFloor",
    "fundEquityBeta",
    "reserveAsset"
]
# for column_name in spreadsheet_column_names:
#     print(column_name)

database_field_names = [
    "data_source             char(4)     COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL",
    "bus_datetime            datetime    NOT NULL",
    "fundId                  int         NOT NULL",
    "fundName                varchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL",
    "oneMth                  float(53)   NULL",
    "threeMth                float(53)   NULL",
    "sixMth                  float(53)   NULL",
    "forecast                float(53)   NULL",
    "oneDayChg               float(53)   NULL",
    "fiveDayChg              float(53)   NULL",
    "tradeThreshold          float(53)   NULL",
    "currentState            float(53)   NULL",
    "sizedEquityRatio        float(53)   NULL",
    "actualEquityRatio       float(53)   NULL",
    "targetVol               float(53)   NULL",
    "rpmVol                  float(53)   NULL",
    "modelName               varchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL",
    "date1DayPast            datetime    NULL",
    "retOneDayPast           float(53)   NULL",
    "date2DayPast            datetime    NULL",
    "retTwoDatPast           float(53)   NULL",
    "trendIndicator          int         NULL",
    "stressFilterMultiplier  float(53)   NULL",
    "adjStressVolCap         float(53)   NULL",
    "modelNameCore           varchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL",
    "adjCoreVolCap           float(53)   NULL",
    "forecastCore            float(53)   NULL",
    "sizeEquityRatioCore     float(53)   NULL",
    "equityRatioFloor        float(53)   NULL",
    "fundEquityBeta          float(53)   NULL",
    "reserveAsset            float(53)   NULL"
]
# for field_name in database_field_names:
#     print(field_name)

# Merge the two dictionaries and find the longest key
merged_names = dict(zip(spreadsheet_column_names, database_field_names))
max_key_len, max_key = max((len(k), k) for k in merged_names.keys())
# print(max_key_len, max_key)

# Print the column to field comparison
row_format = "{:<25}  {:<}"
print(row_format.format("Column Name", "Field Name"))
print(row_format.format("-----------", "----------"))
for k, v in merged_names.items():
    field_name = v.split()[0]
    if k != field_name:
        v += " [** Doesn't Match **]"
    print(row_format.format(k, v))
