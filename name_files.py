from today_to_file import today_to_file

def name_files(number, folder, extension):
    today = today_to_file() 
    # lapPath = "C:\\Users\\UR100\\Documents\\csvParser\\" //laptop production path
    # path = lapPath + folder + "\\" + "RS" + number + "DAY" + "\\" + "RS" + number + "Report" + today + extension #".csv" //laptop production path
    path = folder + "\\" + "RS" + number + "DAY" + "\\" + "RS" + number + "Report" + today + extension #".csv" // test pc path
    # path = "D:\\" + folder + "\\" + "RS" + number + "DAY" + "\\" + "RS" + number + "Report" + today + extension #".csv" // production path
    # print("Sciezka:         ", path)
    return path