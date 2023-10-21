import dropbox

# Replace with your Dropbox API credentials
app_key = 'hvr42e05zuhwium'
app_secret = 'asewtnhbuglulua'
oauth2_refresh_token = '1e1ucJVigowAAAAAAAAAAatMW9D_80UiUvXxvb0_oUKo9cCmkpaL7UGInwUcYEni'

# Initialize Dropbox client
dbx = dropbox.Dropbox("sl.Bm73n-LQcSlV_Pj2pUm_ksfT7ixjNnMNFf-Tb_sbbwWrtC7kLVs_c_F2BMOS8vthVdgMIlisWR0_JWislE0n7EwVBbVUAsmapmVkPSCmB-USlb6zsz2zsvdtMinC2d3XcpoVSP4Rcgkn")

# dbx = dropbox.Dropbox(
#         app_key='hvr42e05zuhwium',
#         app_secret='asewtnhbuglulua',
#         oauth2_refresh_token='1e1ucJVigowAAAAAAAAAAatMW9D_80UiUvXxvb0_oUKo9cCmkpaL7UGInwUcYEni'
#     )

parent_folder_path = ''

try:
    dbx.files_list_folder(parent_folder_path)
except dropbox.exceptions.ApiError as err:
    print(f"Error navigating to the parent folder: {err}")

# List folders in the root directory (home)
try:
    result = dbx.files_list_folder('')
    for entry in result.entries:
        if isinstance(entry, dropbox.files.FolderMetadata):
            print(f"Folder: {entry.name}")
except dropbox.exceptions.AuthError as err:
    print(f"Error: {err}")