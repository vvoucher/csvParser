from name_files import name_files
from open_csv_file import open_csv_file
from rename_header import rename_header
from create_timestamp import create_timestamp
from set_hours import set_hours
from filter_NG import filter_NG
# from drop_rows import drop_rows

def autogague(station, line, dataBase):
    # file=name_files(station,"Report", ".csv")
    # dataBase = open_csv_file(file)
    # dataBase = rename_header(dataBase)
    # print(dataBase)
    dataBase = create_timestamp(dataBase)
    dataBase = set_hours(dataBase)
    result = filter_NG(dataBase, line)
    # simpleResult = drop_rows(result)
    # print(simpleResult)
    # pathToSave=name_files(station, "Result" + line, ".csv")
    # result.to_csv(pathToSave)

    # print(result, "\n")
    # print("Zapisano dane:       ", pathToSave)
    # print("\n")
    return result

