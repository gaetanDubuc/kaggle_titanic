poetry shell
poetry install
kaggle competitions download -c titanic
mkdir kaggle\input
move titanic.zip kaggle\input
tar -xf kaggle\input\titanic.zip -C %~dp0kaggle\input
python scripts/split_data.py