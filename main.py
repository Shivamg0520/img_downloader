import requests
import os
import re

user = input("Enter the name of image: ")

user_agent = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36"
}
url = f"https://www.google.com/search?sca_esv=2b9a61f20e275e74&sxsrf=AE3TifP6-OuBlGEIUwFYM7dt_jSnd6RDEg:1753739242573&udm=2&fbs=AIIjpHwLh0wKnd07MekH1toIM_nAdmqaIXjqwAyfX1RPQQMkC15qilEkVg2ulljEe2oHEV0AaNEsjh-Ud8ghRBUC55_ZQfTapopqddelreSlHva1eYXAMU2HOHKdcVRxSx5TI7kc7BUKsguAucmbR4br51laIDwaOY-udTexAi4xIc75ymvRYs73kptUIXPsMbJPUSJNgFsRputBHM3hyfDdri-yyGPyGHlV-x9cB066K-A39Mu3l9ykIOjnBtFIX0Id-u4lBKdsmoMfHCfoVvcoavWUJyXsPQ&q={user}&sa=X&ved=2ahUKEwilgdTkw-COAxXVR2wGHeU3IF4QtKgLegQICxAB&biw=1536&bih=742&dpr=1.25"
response = requests.get(url= url, headers= user_agent).text
pattern = r'"(https://[^"]+\.jpg)",[0-9]+,[0-9]+\]'
images = re.findall(pattern, response)
print(f"Totla number of images: {len(images)}")
nu_of_images = int(input("Number of images to be downloaded: "))

if images:
    if not os.path.exists(user):
        os.mkdir(user)
        os.chdir(user)
    else:
        os.chdir(user)
for img in images[:nu_of_images]:
    img_url = img
    try:
        response = requests.get(url=img_url, timeout=10)
        response.raise_for_status()
        img_name = img_url.split('/')[-1]
        with open(img_name, "wb") as file:
            file.write(response.content)
        print(f"Downloaded: {img_name}")
    except Exception as e:
        print(f"Failed to download {img_url}: {e}")
