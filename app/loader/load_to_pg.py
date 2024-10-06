import polars as pl

from app.constants import TYCHO_FILE_PATH

POSTGRES_URI = "postgresql://postgres:postgres@localhost:5432/postgres"
POSTGRES_TABLE_NAME = "tycho_stars"

# df_pl = pl.read_csv(TYCHO_FILE_PATH)


#df_pl.write_database(table_name=POSTGRES_TABLE_NAME, connection=POSTGRES_URI)

df = pl.read_database_uri("SELECT * FROM tycho_stars", POSTGRES_URI)

A = ["2695-04139-1",
"1711-02475-1",
"8588-04200-1",
"6232-01333-1",
"4252-01870-1",
"6550-04525-1",
"2019-01251-1",
"3833-01034-1",
"2243-01831-1",
"1125-02186-1",
"7885-02065-1",
"7527-01031-1",
"3827-01079-1",
"6779-02194-1",
"7814-03706-1",
"8663-02929-1",
"7367-00804-1",
"8283-04134-1",
"3664-01985-1",
"8595-03312-1",
"7663-04093-1",
"2029-01690-1",
"3523-01684-1",
"3156-02223-1",
"3663-02668-1",
"3850-01385-1",
"7689-02617-1",
"0870-00988-1",
"2851-02168-1",
"8446-01644-1",
"2837-02311-1",
"4416-01799-1",
"1000-02508-1",
"6868-01829-1",
"1735-03180-1",
"5351-00760-1",
"2286-01329-1",
"7293-02215-1",
"4628-00237-1",
"8579-02692-1",
"5847-02333-1",
"1758-02416-1",
"1423-01349-1",
"5460-01592-1",
"5938-02918-1",
"1329-01746-1",
"8785-01898-1",
"4771-01188-1",
"2924-02742-1",
"2457-02407-1",
"9275-03641-1",
"4146-01274-1",
"3467-01257-1",
"7892-07679-1",
"8140-06533-1",
"7401-03471-1",
"3320-02808-1",
"3845-01190-1",
"8438-01959-1",
"4766-02450-1",
"9200-02603-1",
"1859-01470-1",
"0113-01856-1",
"8654-03422-1",
"7388-01093-1",
"6535-03619-1",
"0833-01381-1",
"9007-05848-1",
"8979-03464-1",
"8659-03107-1",
"3574-03347-1",
"6977-01267-1",
"1920-02194-1",
"5547-01518-1",
"6803-02158-1",
"1266-01416-1",
"1058-03399-1",
"9005-03919-1",
"8478-01395-1",
"0129-01873-1",
"0187-02184-1",
"5331-01752-1",
"3358-03141-1",
"3105-02070-1",
"9007-05849-1",
"5949-02777-1",
"8534-02277-1",
"1472-01436-1",
]
print(len(A))
with pl.Config(tbl_cols=-1):
   #print(df.select(["TYC", "VTmag"]).drop_nulls().sort("VTmag", descending=False).head())

    starnames = A
    has_been_found = []

    for star in A:
        has_been_found.append(bool((df.get_column("TYC") == star).sum()))


    zzzz = pl.from_dict({"star_name": starnames, "is_found": has_been_found})

    zzzz.write_csv("checking_stars.csv")



with pl.Config(tbl_cols=-1):
    pldf = df.filter(pl.col("TYC") == A[0])
    pldf.write_csv("one_liner_star.csv",include_header=True)

