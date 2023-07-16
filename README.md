# eyeForm – myopiAI
### <font size=50>掌握近視未來，智慧在你手中」，這是一個近視控制網路大數據AI平台，利用人工智慧為近視的學齡兒童指引最合適的診療之道。</font>
![eyeForm_platform](https://github.com/neurobit-ai/eyeForm/assets/94299157/54c5bd90-d9d8-410a-a567-d859b053f26d)

# Web Demos
## 1. Main entrance website:
[eyeForm – myopiAI](https://neurobit.synology.me/wordpress/)
## 2. Database:
[eyeForm/myopia.db.xlsx](https://docs.google.com/spreadsheets/d/1kBLwr1Lxec6yi5wEET5opkSKt_TD3cVQjICWlDyHS4o/edit#gid=1477633965) from Google Sheets for myopia website version
## 3. eyeForm for AI test website form
- Default (EN) version for [EN: eyeForm - AI test](https://neurobit-ai.github.io/eyeForm/myopia/)
- English version for [EN: eyeForm - AI test](https://neurobit-ai.github.io/eyeForm/myopia/us-en/)
- Traditional Chinese version for [TW: eyeForm – AI test](https://neurobit-ai.github.io/eyeForm/myopia/zh-tw/)
- Simplified Chinese version for [CH: eyeForm – AI test](https://neurobit-ai.github.io/eyeForm/myopia/zh-cn/)
#### Access to the TSGH exclusive platform is restricted to authorized users only.
- TSGH version (Traditional Chinese version) for [TSGH: eyeForm - AI test](https://neurobit-ai.github.io/eyeForm/)
- eyeForm.db.xlsx from Google Sheets for TSGH website version

# Technical documentation
## 1. How to update data_to_plot.pkl
1. Download eyeForm.db.xlsx from Google Sheets
2. Run data_to_plot.ipynb <a href="https://colab.research.google.com/github/neurobit-ai/eyeForm/blob/main/data_to_plot.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
3. Upload data_to_plot.pkl

## 2. How to update eyeForm.db risk columns
1. Download eyeForm.db.xlsx from Google Sheets
2. Run db_risk0123.ipynb <a href="https://colab.research.google.com/github/neurobit-ai/eyeForm/blob/main/db_risk0123.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
3. Open db_risk0123.xlsx, insert 2 rows on top, select risk columns, copy and paste into eyeForm.db

- eyeForm/myopia.db.xlsx from Google Sheets for myopia website version: 
[eyeForm/myopia.db.xlsx](https://docs.google.com/spreadsheets/d/1kBLwr1Lxec6yi5wEET5opkSKt_TD3cVQjICWlDyHS4o/edit#gid=1477633965)

## 3. SageMaker Serverless Inference
- [Doc](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html)
- [Repo](https://github.com/neurobit-ai/eyeForm-SageMaker)

## 4. System Architecture
- [Drawio](https://drive.google.com/file/d/1-smnQNOvg643gtuWUa2kjEe1_j8orKmA/view?usp=sharing)
