import pandas as pd

# Дни занятий
day_training = ['Wed', 'Fri', 'Sat']

#  Чтение данных из гугл таблицы
sheet_id = '1myYmDRspwQOYf4SuleW29154MS-Ze1SN37mjC77_IIQ'
sheet_name = 'List2'

url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
df = pd.read_csv(url)

# считываем данные:
contacts = df.iloc[0]['2']
examination = df.iloc[1]['2']

# для владельца оружия

doc_4_lesson, price_prolongation, day_and_time_4prolongation = (df.iloc[3][column] for column in range(2, 5))

# для занятия по усовершенствованию навыка работы с оружием

doc_4skill_upgrade, price_4skill_upgrade, schedule_individual_lessons = (df.iloc[4][column] for column in range(2, 5))
handgun_program, long_gun_program = (df.iloc[row][2] for row in range(8, 10))

# для первичного обучения

doc_not_gun_owner, price_not_gun_owner, day_and_time_not_gun_owner = (df.iloc[5][column] for column in range(2, 5))

# для индивидуального занятия

doc_individual_lesson, price_individual_lesson = (df.iloc[7][column] for column in range(2, 4))
