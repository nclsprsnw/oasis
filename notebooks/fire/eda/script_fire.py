"""
Fire data processing module for wildfire risk assessment.

This module processes fire data from CSV files and calculates fire risk scores.
"""
# pylint: disable=duplicate-code

import pandas as pd


def fire_csv():
    """
    Load and process fire data from CSV files.

    Returns:
        pandas.DataFrame: Processed fire data with risk calculations.
    """

    # AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET")
    # AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    # AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

    # load_dotenv()

    # s3_client = boto3.client(
    #     "s3",
    #     aws_access_key_id=AWS_ACCESS_KEY_ID,
    #     aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    # )

    # response = s3_client.get_object(
    #     Bucket=AWS_S3_BUCKET, Key="raw/fire/Incendies.csv"
    # )

    # data_fire = pd.read_csv(response.get("Body"), sep=';', skiprows=3)
    # data_fire.head()

    # response = s3_client.get_object(
    #     Bucket=AWS_S3_BUCKET,
    #     Key="processed/referentiel/ref_espace_communes.csv"
    # )

    # data_insee = pd.read_csv(response.get('Body'), index_col=0)
    # data_insee.head()

    # response = s3_client.get_object(
    #     Bucket=AWS_S3_BUCKET,
    #     Key="processed/surface departement/surface_departements.csv"
    # )
    # data_depart_surface = pd.read_csv(response.get('Body'))
    # data_depart_surface.head()

    data_fire = pd.read_csv("./data/Incendies.csv", sep=";", skiprows=3)

    data_insee = pd.read_csv("../ref_espace_communes.csv")
    data_depart_surface = pd.read_csv("./data/surface_departements.csv")

    columns_remove = [
        "Nom de la commune",
        "Surface forêt (m2)",
        "Surface maquis garrigues (m2)",
        "Autres surfaces naturelles hors forêt (m2)",
        "Surfaces agricoles (m2)",
        "Autres surfaces (m2)",
        "Surface autres terres boisées (m2)",
        "Surfaces non boisées naturelles (m2)",
        "Surfaces non boisées artificialisées (m2)",
        "Surfaces non boisées (m2)",
        "Précision des surfaces",
        "Type de peuplement",
        "Décès ou bâtiments touchés",
        "Nombre de décès",
        "Nombre de bâtiments totalement détruits",
        "Nombre de bâtiments partiellement détruits",
        "Précision de la donnée",
    ]

    columns_rename = {
        "Année": "year",
        "Numéro": "id",
        "Département": "department",
        "Code INSEE": "INSEE code",
        "Date de première alerte": "first alert date",
        "Surface parcourue (m2)": "area burned (m²)",
        "Nature": "cause",
    }

    data_fire.drop(columns=columns_remove, inplace=True)
    data_fire.rename(columns=columns_rename, inplace=True)
    print("Data fire shape:", data_fire.shape)

    codes_metro = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
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

    data_fire = data_fire[data_fire["department"].isin(codes_metro)].copy()
    print("Data fire only code metro:", data_fire.shape)

    data_fire["first alert date"] = pd.to_datetime(data_fire["first alert date"])

    data_fire["year"] = data_fire["first alert date"].dt.year
    data_fire["month"] = data_fire["first alert date"].dt.month
    data_fire["quarter"] = data_fire["first alert date"].dt.quarter
    data_fire["year_quarter"] = (
        data_fire["year"].astype(str) + "T" + data_fire["quarter"].astype(str)
    )
    data_fire["cause"] = data_fire["cause"].fillna("Unknown")

    data_fire = pd.merge(
        data_fire,
        data_insee,
        left_on="INSEE code",
        right_on="code_commune_INSEE",
        how="inner",
    ).drop(columns=["code_region", "code_commune_INSEE"])
    print("Data fire with INSEE code:", data_fire.shape)

    data_depart_surface.rename(
        columns={"Numéro": "department", "Superficie (m²)": "area (m²)"}, inplace=True
    )

    data_fire = pd.merge(data_fire, data_depart_surface, on="department")
    print("Data fire with department area:", data_fire.shape)

    agg_data_fire = (
        data_fire.groupby(["department", "year", "quarter", "year_quarter"])
        .agg({"area burned (m²)": "sum", "area (m²)": "first"})
        .reset_index()
    )
    agg_data_fire.sort_values("year_quarter", inplace=True)
    print("Agg data fire:", agg_data_fire.shape)

    agg_data_fire["ratio"] = (
        agg_data_fire["area burned (m²)"] / agg_data_fire["area (m²)"]
    )

    def danger_fire_level(ratio):
        if ratio < 0.0001:
            return "Low"
        if ratio < 0.0005:
            return "Moderate"
        if ratio < 0.001:
            return "High"
        return "Critical"

    agg_data_fire["danger_fire_level"] = agg_data_fire["ratio"].apply(danger_fire_level)
    print("Agg data fire + two columns:", agg_data_fire.shape)

    data_fire = data_fire.merge(
        agg_data_fire[
            [
                "department",
                "year",
                "quarter",
                "year_quarter",
                "ratio",
                "danger_fire_level",
            ]
        ],
        on=["department", "year", "quarter", "year_quarter"],
        how="left",
    )
    print("Data fire + agg data fire:", data_fire.shape)

    risk_mapping = {"Low": 0, "Moderate": 1, "High": 2, "Critical": 3}

    data_fire["fire_score"] = (
        data_fire["danger_fire_level"].map(risk_mapping).astype(float)
    )
    print("Data fire final shape:", data_fire.shape)

    fire_score_dept_quarter = (
        data_fire.groupby(["department", "year_quarter"])["fire_score"]
        .mean()
        .reset_index()
        .sort_values(by="year_quarter", ascending=True)
    )
    print("fire score department by quarter:", fire_score_dept_quarter.shape)

    return fire_score_dept_quarter
