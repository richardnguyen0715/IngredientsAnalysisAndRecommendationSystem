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
#### Data Cleaning and Normalizing:
1. **To run**: Data Cleaning and Normalizing.ipynb
2. **Datasets**:cleaned_recipes_translated.txt, cleaned_recipes_2_translated.txt
3. **Note**:This section will demonstrate how to clean and normalize data, from a plain text file converted into a binary dataframe, with rows being the names of dishes, and columns being the names of ingredients present in the original data.
#### Data Exploration:
1. **To run**: DataExploration.ipynb
2. **Datasets**:ingredients.csv
3. **Note**: This section will present the information you need to know about the cooking field.
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

#### Data Modeling 02 - Recipe Substitutes:
1. **To run**: Datamodeling_02.ipynb
2. **How to use**: Please click "Run All," and a GUI will appear shortly afterward. Insert one recipe at a time in the text box and click ENTER to view the suggested substitutes.

#### Data Modeling 03 - Recipe Recommendation:
1. **To run**: DataModeling_03.ipynb
2. **How to use**: Please click "Run All," and a GUI will appear shortly afterward. Insert your desired ingredients (separated by comma) in the text box and click the ENTER button to see a list of recommended recipes.
---
### Our Work:
Link here: [Notion](https://pool-argument-1f9.notion.site/IntroDS-Lap01-Handling-Real-World-Problems-1130a9b1c8bb800ba10ccbf7706fb0a3?pvs=4)
