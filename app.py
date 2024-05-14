import gradio
import pandas as pd
import joblib

def convert_y_n(inp_str):
  return 1 if inp_str == 'Yes' else 0

def convert_sex(inp_str):
  return 1 if inp_str == 'Male' else 0

# Function for prediction
def predict_death_event(age, anaemia, creat, diabetes, ejec, bp, plt, serum_c, serum_na, sex, smok, time):
  inp_list = [float(age), convert_y_n(anaemia), float(creat), convert_y_n(diabetes), float(ejec), convert_y_n(bp), float(plt), float(serum_c), int(serum_na), convert_sex(sex), convert_y_n(smok), int(time)]
  cols = ['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes', 'ejection_fraction', 'high_blood_pressure', 'platelets', 'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time']
  df = pd.DataFrame([inp_list], columns=cols)
  return xgb_model_loaded.predict(df)[0]

xgb_model_loaded = joblib.load(open("xgboost-model.pkl", "rb"))

# Inputs from user
age = gradio.Slider(minimum=0, maximum=100, step=1, label='Age')
anaemia = gradio.Radio(['Yes', 'No'], label='Anaemia')
creatinine_phosphokinase = gradio.Slider(minimum=0, maximum=100, step=1, label='Creatinine Phosphokinase')
diabetes = gradio.Radio(['Yes', 'No'], label='Diabetes')
ejection_fraction = gradio.Slider(minimum=0, maximum=100, step=1, label='Ejection Fraction')
high_blood_pressure = gradio.Radio(['Yes', 'No'], label='High Blood Pressure')
platelets = gradio.Slider(minimum=0, maximum=1000000, step=1, label='Platelets')
serum_creatinine = gradio.Slider(minimum=0, maximum=100, step=1, label='Serum Creatinine')
serum_sodium = gradio.Slider(minimum=0, maximum=1000, step=1, label='Serum Sodium')
sex = gradio.Radio(['Male', 'Female'], label='Sex')
smoking = gradio.Radio(['Yes', 'No'], label='Smoking')
time = gradio.Slider(minimum=0, maximum=100, step=1, label='Time')

# Output response
out_resp = gradio.Textbox(lines=1, type="text", label='Death')

title = "Patient Survival Prediction"
description = "Predict survival of patient with heart failure, given their clinical record"

iface = gradio.Interface(fn = predict_death_event,
                         inputs = [age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time],
                         outputs = [out_resp],
                         title = title,
                         description = description,
                         allow_flagging='never')

if __name__ == "__main__":
  iface.launch(server_name='0.0.0.0')