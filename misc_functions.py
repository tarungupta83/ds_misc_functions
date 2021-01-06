
#%config Completer.use_jedi = False # In my computer autocomplete does not work in jupyter properly so you guys can ignore


# Get the zip file link as an input and donwload the zip file in respective folder
def get_file(url):
    !pip install wget
    import os
    import wget
    wget.download(url)

# Get the zip file link as an input and donwload the zip file in respective folder
def get_file_unzip(url, folder):
    import os
    import zipfile
    file_name = url.split("/")[-1]
    #print("./"+ file_name)
    #wget.download(url,file_name)
    get_file(url)
    if os.path.exists(folder):
        pass
    else:
        os.makedirs(folder)
    with zipfile.ZipFile(file_name,"r") as zip_ref:
        zip_ref.extractall(folder)
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print("The file does not exist")

# If you want to get all the files inside a folder to the maximum depth

########################################################################
##### JUST BEWARE DONT RUN ON IMAGE DATA YOU WILL GO MAD ###############
#####        DONT WORRY ITS HANDLED WITh 20 FILES        ###############
########################################################################

def get_all_filenames(directory, depth):
    import os
    nof_of_files = depth
    for dirname, _, filenames in os.walk(directory):
        if len(filenames) > nof_of_files:
            print("Just check in this ( {} ) directory you have more than {} file, if i expand you will go mad".format(dirname, nof_of_files))
        else:
            for filename in filenames:
                print(os.path.join(dirname, filename))

## Get the google drive mounted
def mount_gdrive():
    from google.colab import drive
    drive.mount('/content/drive')

## As you know many a times data comes in a single folder where you need to
## devide the data into test and train you can use this function to do so
def divide_data(files_folder, no_of_files, make_folder):
    import os
    import shutil
    if os.path.exists(make_folder):
        pass
    else:
        os.makedirs(make_folder)
    for dirname, _, filenames in os.walk(files_folder):
        dirname_path = os.path.join(make_folder, dirname.split("/")[-1])
        #print(dirname)
        if os.path.exists(dirname_path):
            pass
        else:
            os.makedirs(dirname_path)
        #print(dirname_path)
        for filename in filenames[:no_of_files]:
            file_path = os.path.join(dirname, filename)
            shutil.move(file_path, dirname_path)
            print("Moved File " , file_path , " to ", dirname_path)