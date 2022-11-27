pip install -r requirements.txt
kaggle competitions download -c titanic
mkdir kaggle\input
mv titanic kaggle\input
move titanic.zip kaggle\input
tar -xf kaggle\input\titanic.zip -C %~dp0kaggle\input
python split_data.py