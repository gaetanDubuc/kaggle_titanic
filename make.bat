poetry shell
poetry install
kaggle competitions download -c titanic
mkdir input\titanic
mkdir \kaggle\temp/
move titanic.zip input\titanic
tar -xf input\titanic\titanic.zip -C %~dp0input\titanic
python scripts/split_data.py