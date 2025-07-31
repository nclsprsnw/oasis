"""
Weather score calculation module for climate risk assessment.

This module processes weather data to calculate risk scores for different
climate-related indicators including heat, rainfall, drought, and extreme events.
"""
# pylint: disable=duplicate-code

import pandas as pd


def weather_csv():  # pylint: disable=too-many-locals,too-many-statements
    """
    Process weather data and calculate climate risk scores.

    Returns:
        pandas.DataFrame: Processed weather data with risk scores by commune and year.
    """
    codes_metro = [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
        "2A",
        "2B",
        "30",
        "31",
        "32",
        "33",
        "34",
        "35",
        "36",
        "37",
        "38",
        "39",
        "40",
        "41",
        "42",
        "43",
        "44",
        "45",
        "46",
        "47",
        "48",
        "49",
        "50",
        "51",
        "52",
        "53",
        "54",
        "55",
        "56",
        "57",
        "58",
        "59",
        "60",
        "61",
        "62",
        "63",
        "64",
        "65",
        "66",
        "67",
        "68",
        "69",
        "70",
        "71",
        "72",
        "73",
        "74",
        "75",
        "76",
        "77",
        "78",
        "79",
        "80",
        "81",
        "82",
        "83",
        "84",
        "85",
        "86",
        "87",
        "88",
        "89",
        "90",
        "91",
        "92",
        "93",
        "94",
        "95",
    ]

    data_weather_50_23 = []
    data_weather_24_25 = []

    # for code in codes_metro:
    # key_50_23 = f"raw/climate/MENSQ_{code}_previous-1950-2023.csv.gz"
    # try:
    #     response = s3_client.get_object(Bucket=AWS_S3_BUCKET, Key=key_50_23)
    #     df = pd.read_csv(response.get("Body"), sep=';', compression='gzip')
    #     data_weather_24_25.append(df)
    # except botocore.exceptions.ClientError as e:
    #     if e.response['Error']['Code'] == "NoSuchKey":
    #         print(f"File not found for {code}")
    #     else:
    #         raise

    # key_24_25 = f"raw/climate/MENSQ_{code}_latest-2024-2025.csv.gz"
    # try:
    #     response = s3_client.get_object(Bucket=AWS_S3_BUCKET, Key=key_24_25)
    #     df = pd.read_csv(response.get("Body"), sep=';', compression='gzip')
    #     data_weather_24_25.append(df)
    # except botocore.exceptions.ClientError as e:
    #     if e.response['Error']['Code'] == "NoSuchKey":
    #         print(f"File not found for {code}")
    #     else:
    #         raise

    # try:
    #     response = s3_client.get_object(
    #         Bucket=AWS_S3_BUCKET,
    #         Key="processed/referentiel/ref_espace_communes.csv"
    #     )

    #     data_insee = pd.read_csv(response.get('Body'), index_col=0)

    # except FileNotFoundError:
    #     print("Le fichier INSEE est introuvable")
    #     data_insee = None

    for code in codes_metro:
        try:
            df = pd.read_csv(
                f"./data/MENSQ_{code}_previous-1950-2023.csv.gz",
                compression="gzip",
                sep=";",
            )
            data_weather_50_23.append(df)

        except FileNotFoundError:
            print(f"File not found for department {code} in 1950-2023")

        try:
            df2 = pd.read_csv(
                f"./data/MENSQ_{code}_latest-2024-2025.csv.gz",
                compression="gzip",
                sep=";",
            )
            data_weather_24_25.append(df2)

        except FileNotFoundError:
            print(f"File not found for department {code} in 2024-2025")

        try:
            data_insee = pd.read_csv("../ref_espace_communes.csv")
        except FileNotFoundError:
            print("Le fichier INSEE est introuvable")
            data_insee = None

    data_weather_50_25 = pd.concat(
        data_weather_50_23 + data_weather_24_25, ignore_index=True
    )

    columns_selected = {
        "NUM_POSTE": "postal_code",
        "NOM_USUEL": "city",
        "LAT": "latitude",
        "LON": "longitude",
        "AAAAMM": "date",
        "TXAB": "temp_max_abs_celsius",
        "NBJTX35": "days_temp_max_35c_plus",
        "TM": "temp_mean_avg_celsius",
        "RR": "precip_total_mm",
        "RRAB": "precip_max_24h_mm",
        "NBJRR50": "days_precip_50mm_plus",
        "INST": "sunshine_duration_min",
        "FXIAB": "wind_gust_max_m_s",
        "NBJORAG": "days_with_thunderstorm",
        "NBJGREL": "days_with_hail",
    }

    data_weather_50_25.rename(columns=columns_selected, inplace=True)
    data_weather_50_25 = data_weather_50_25[list(columns_selected.values())]

    data_weather_50_25["date"] = pd.to_datetime(
        data_weather_50_25["date"], format="%Y%m"
    )

    data_weather_50_25["year"] = data_weather_50_25["date"].dt.year
    data_weather_50_25["month"] = data_weather_50_25["date"].dt.month
    data_weather_50_25["quarter"] = data_weather_50_25["date"].dt.quarter
    data_weather_50_25["year_quarter"] = (
        data_weather_50_25["year"].astype(str)
        + "T"
        + data_weather_50_25["quarter"].astype(str)
    )
    data_weather_50_25["postal_code"] = (
        data_weather_50_25["postal_code"].astype(str).str.zfill(8).str[:5]
    )

    data_weather_14_24 = data_weather_50_25[
        (data_weather_50_25["year"] >= 2014) & (data_weather_50_25["year"] < 2025)
    ].sort_values("date", ascending=True)

    data_weather_14_24 = (
        data_weather_14_24.merge(
            data_insee,
            left_on="postal_code",
            right_on="code_commune_INSEE",
            how="inner",
        )
        .drop(columns=["latitude_x", "longitude_x", "city", "postal_code"])
        .rename(columns={"latitude_y": "latitude", "longitude_y": "longitude"})
    )

    cols_to_fill = [
        "temp_max_abs_celsius",
        "days_temp_max_35c_plus",
        "precip_total_mm",
        "sunshine_duration_min",
        "temp_mean_avg_celsius",
        "precip_max_24h_mm",
        "days_precip_50mm_plus",
        "wind_gust_max_m_s",
        "days_with_thunderstorm",
        "days_with_hail",
    ]

    for col in cols_to_fill:
        data_weather_14_24[col] = data_weather_14_24.groupby(
            ["code_commune_INSEE", "month"]
        )[col].transform(lambda x: x.fillna(x.mean()))

        mask_missing = data_weather_14_24[col].isna()
        data_weather_14_24.loc[mask_missing, col] = data_weather_14_24.groupby(
            ["code_postal", "month"]
        )[col].transform(lambda x: x.fillna(x.mean()))

        mask_missing = data_weather_14_24[col].isna()
        data_weather_14_24.loc[mask_missing, col] = data_weather_14_24.groupby(
            ["nom_departement", "month"]
        )[col].transform(lambda x: x.fillna(x.mean()))

        mask_missing = data_weather_14_24[col].isna()
        data_weather_14_24.loc[mask_missing, col] = data_weather_14_24.groupby(
            ["code_region", "month"]
        )[col].transform(lambda x: x.fillna(x.mean()))

    def heat_related_indicators(temp_max_abs_celsius, days_temp_max_35c_plus):
        if (temp_max_abs_celsius <= 30) and (days_temp_max_35c_plus == 0):
            return "Low"
        if (30 < temp_max_abs_celsius <= 35) or (1 <= days_temp_max_35c_plus <= 2):
            return "Moderate"
        if (35 < temp_max_abs_celsius <= 40) or (3 <= days_temp_max_35c_plus <= 5):
            return "High"
        if (temp_max_abs_celsius > 40) or (days_temp_max_35c_plus > 5):
            return "Critical"
        return "Unknown"

    def heavy_rainfall(precip_max_24h_mm, days_precip_50mm_plus):
        if precip_max_24h_mm <= 20 and days_precip_50mm_plus == 0:
            return "Low"
        if (20 < precip_max_24h_mm <= 40) or (days_precip_50mm_plus == 1):
            return "Moderate"
        if (40 < precip_max_24h_mm <= 60) or (2 <= days_precip_50mm_plus <= 3):
            return "High"
        if precip_max_24h_mm > 60 or days_precip_50mm_plus > 3:
            return "Critical"
        return "Unknown"

    def drought(precip_total_mm, sunshine_duration_min, temp_mean_avg_celsius):
        score = 0

        if precip_total_mm < 20:
            score += 2
        elif 20 <= precip_total_mm < 40:
            score += 1

        if sunshine_duration_min > 300:
            score += 2
        elif 251 <= sunshine_duration_min <= 300:
            score += 1

        if temp_mean_avg_celsius > 27:
            score += 3
        elif 25 < temp_mean_avg_celsius <= 27:
            score += 2
        elif 22 <= temp_mean_avg_celsius <= 25:
            score += 1

        if score <= 1:
            return "Low"
        if score in (2, 3):
            return "Moderate"
        if score in [4, 5]:
            return "High"
        return "Critical"

    def extrem_events(wind_gust_max_m_s, days_with_thunderstorm, days_with_hail):
        score = 0

        if wind_gust_max_m_s > 30:
            score += 2
        elif 25 < wind_gust_max_m_s <= 30:
            score += 1

        if days_with_thunderstorm > 5:
            score += 2
        elif 4 <= days_with_thunderstorm <= 5:
            score += 1

        if days_with_hail > 3:
            score += 2
        elif 2 <= days_with_hail <= 3:
            score += 1

        if score == 0:
            return "Low"
        if score in (1, 2):
            return "Moderate"
        if score in (3, 4):
            return "High"
        return "Critical"

    data_weather_14_24["heat_level"] = data_weather_14_24.apply(
        lambda row: heat_related_indicators(
            row["temp_max_abs_celsius"], row["days_temp_max_35c_plus"]
        ),
        axis=1,
    )

    data_weather_14_24["rainfall_level"] = data_weather_14_24.apply(
        lambda row: heavy_rainfall(
            row["precip_max_24h_mm"], row["days_precip_50mm_plus"]
        ),
        axis=1,
    )

    data_weather_14_24["drought_level"] = data_weather_14_24.apply(
        lambda row: drought(
            row["precip_total_mm"],
            row["sunshine_duration_min"],
            row["temp_mean_avg_celsius"],
        ),
        axis=1,
    )

    data_weather_14_24["extrem_events_level"] = data_weather_14_24.apply(
        lambda row: extrem_events(
            row["wind_gust_max_m_s"],
            row["days_with_thunderstorm"],
            row["days_with_hail"],
        ),
        axis=1,
    )

    risk_mapping = {"Low": 0, "Moderate": 1, "High": 2, "Critical": 3}

    data_weather_14_24["heat_score"] = data_weather_14_24["heat_level"].map(
        risk_mapping
    )
    data_weather_14_24["rainfall_score"] = data_weather_14_24["rainfall_level"].map(
        risk_mapping
    )
    data_weather_14_24["drought_score"] = data_weather_14_24["heat_level"].map(
        risk_mapping
    )
    data_weather_14_24["extrem_events_score"] = data_weather_14_24[
        "extrem_events_level"
    ].map(risk_mapping)

    data_weather_14_24["avg_risk_score"] = data_weather_14_24[
        ["heat_score", "rainfall_score", "drought_score", "extrem_events_score"]
    ].mean(axis=1)

    def risk_score_level(score):
        if score < 0.5:
            return "Low"
        if score < 1.5:
            return "Moderate"
        if score < 2.5:
            return "High"
        return "Critical"

    data_weather_14_24["risk_score_level"] = data_weather_14_24["avg_risk_score"].apply(
        risk_score_level
    )

    data_risk_by_dept = (
        data_weather_14_24.groupby(["nom_departement", "year_quarter"])[
            "avg_risk_score"
        ]
        .mean()
        .round(2)
        .reset_index()
    )

    data_insee["code_departement"] = (
        data_insee["code_commune_INSEE"].astype(str).str[:2]
    )

    data_risk_by_dept = data_risk_by_dept.merge(
        data_insee, right_on="nom_departement", left_on="nom_departement", how="left"
    ).drop(
        columns=[
            "code_postal",
            "nom_departement",
            "latitude",
            "longitude",
            "nom_commune_complet",
            "code_region",
            "nom_region",
        ]
    )

    return data_risk_by_dept
