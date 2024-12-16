# IntroDS-FinalPro-HandlingReal-WorldProblems
*The Final Project of Introduction to Data Science Course - HCMUS - Oct 2024.*
## Group Information
1. **Class:** 22_21.
2. **Theory Class Lecturer:** Mr. Le Ngoc Thanh.
3. **Practice Class Lecturer:** Mr. Le Nhut Nam.
4. **Group ID:** 9.
5. **Member's information:** ID - Name
    * 22120412 - [Nguyễn Anh Tường.](https://github.com/richardnguyen0715)
    * 22120384 - [Nguyễn Đình Trí.](https://github.com/dinhtri2305)
    * 22120398 - [Vũ Hoàng Nhật Trường.](https://github.com/Truong5724)
    * 22120424 - [Phạm Ngọc Bảo Uyên.](https://github.com/phamuyen171)
    * 22120449 - [Lê Nguyễn Huyền Vy.](https://github.com/lorchidee1005)
6. **Time**: Oct 01, 2024 - Dec 24, 2024.

---
## Quick Guide
#### Data Collection:
1. **To run**: DataCollection.ipynb.
2. **Datasets**: Dataset_child/
3. **Note**: Here I will divide the data collection process into several parts with different data sets. One of the main reasons is that this kitchenart website will block us if we do data scraping too many times ( Unusual access to the website ).
#### Data Preprocessing:
1. **To run**:
2. **Datasets**:
3. **Note**:
#### Data Exploration:
1. **To run**:
2. **Datasets**:
3. **Note**:
#### Data Modeling 00 - Context Generation Machine:
##### Application Needed:
   * Step 01: Install [LMStudtio](https://lmstudio.ai/).
   * Step 02: Download a model.
   * Step 03: Start LMStudio Server.
1. **To run**: Context_Machine.ipynb
2. **Datasets**: 
   * Context: ingredients_analysis.csv
   * Context Cleaned: cleaned_ingredients_data.csv
   * Context Encoded: numerical_context_data.csv
3. **Note**: You must check clearly what port number LMStudio provides, what model you are using and edit the code accordingly.

#### Data Modeling 01 - Ingredients replacement:
1. **To run**: Datamodeling_01.ipynb
2. **How to use**: Replace the below code with the ingredients you currently have and are missing.
```python
current_ingredients = ['active yeast', 'agave nectar', 'all-purpose flour']
missing_ingredients = ['brown sugar', 'bacon']

recommendations = recommend_replacements(current_ingredients, missing_ingredients)
recommendations
```
3. **Note**: Here I have used additional context for the ingredients, so you **must complete the above step (00).**

#### Data Modeling 02 - Ingredients replacement:
1. **To run**: Datamodeling_02.ipynb
2. **How to use**: Replace the below code with the ingredients you currently have and are missing.
```python
current_ingredients = ['active yeast', 'agave nectar', 'all-purpose flour']
missing_ingredients = ['brown sugar', 'bacon']

recommendations = recommend_replacements(current_ingredients, missing_ingredients)
recommendations
```
3. **Note**: Here I have used additional context for the ingredients, so you **must complete the above step (00).**

#### Data Modeling 03 - Recipe Recommendation:
1. **To run**: DataModeling_03.ipynb
2. **How to use**: Please click "Run All," and a GUI will appear shortly afterward. Enter your desired ingredients (separated by comma) in the text box and click the ENTER button to see a list of recommended recipes.


