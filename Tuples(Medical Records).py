patient = ("Jason Omondi", 30, "118/76", 68)
age = patient[1]
heart_rate = patient[3]
# immutability reason: prevents accidental edits of critical data
p_list = list(patient)
p_list[3] = 72
updated_patient = tuple(p_list)

patients = (
  ("Jason Omondi",30,"118/76",68),
  ("John Doe",45,"120/80",72),
  ("Mary Ann",27,"110/70",65),
  ("Paul Kim",60,"130/85",80),
  ("Lucy Wang",50,"125/78",75)
)
names = [p[0] for p in patients]
