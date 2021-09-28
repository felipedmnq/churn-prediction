<p align="center">
  <img width="1060" height="400" src="https://miro.medium.com/max/800/0*dzmm3qresODlScte">
</p>

<h3 align="center">https://share.streamlit.io/felipedmnq/churn-prediction/API/streamlit_pred.py</h3>

## The Project Objective

**Main objectives:**
- Learn about classification problems.
- Discover and study the main classification algorithms.
- Discover and study the main  metrics for classification problems.

**Secondary goals:**
- Practice EDA.
- Practice python programming concepts for Data Science.
- Practice problem solving.
_ Practice GitHub usage.
- Practice Story Telling.

## The Problem

TOP BANK is a bank that operates mainly in Europe offering financial products from bank accounts to investments, including some types of insurance and investment products. The company's main product is a bank account, in which the customer can deposit his salary, make withdrawals, deposits and transfer to other accounts. This bank account has no cost to the customer and is valid for 12 months, it means that the customer needs to renew the contract of that account to continue using it for the next 12 months. In the last few months the Analytics team realized that the rate of customers canceling their accounts and leaving the bank was raising and that worries the company.

## The Challange

As a Data Science Consultant, you need to create an action plan to decrease the number of churn customers and deliver a possible solution for the problem. 

## Planning

* First look at the dataset.
* Cleaning Dataset.
* EDA.
* Modeling.
* Modeling evaluation.
* Solution delivery.

## Tools Used to Solve the Problem

<table>
     <tbody>
       <tr valign="top">
          <td width="25%" align="center">
            <span>Python</span><br><br>
            <img height="64px" src="https://cdn.svgporn.com/logos/python.svg">
          </td>
          <td width="25%" align="center">
            <span>SciKit Learn</span><br><br>
            <img height="64px" src="https://e7.pngegg.com/pngimages/905/45/png-clipart-scikit-learn-python-scikit-logo-brand-learning-text-computer.png">
          </td>
          <td width="25%" align="center">
            <span>Pandas</span><br><br>
            <img height="64px" src="https://pandas.pydata.org/static/img/pandas.svg">
          </td>
          <td width="25%" align="center">
            <span>NumPy</span><br><br>
            <img height="64px" src="https://numpy.org/images/logos/numpy.svg">
          </td>
        </tr>
        <tr valign="top">
          <td width="25%" align="center">
            <span>Matplotlib</span><br><br>
            <img height="64px" src="https://matplotlib.org/_images/sphx_glr_logos2_001.png">
          </td>
          <td width="25%" align="center">
            <span>Seaborn</span><br><br>
            <img height="64px" src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg">
          </td>
          <td width="25%" align="center">
            <span>Plotly</span><br><br>
            <img height="64px" src="https://upload.wikimedia.org/wikipedia/commons/8/8a/Plotly_logo_for_digital_final_%286%29.png">
          </td>
          <td width="25%" align="center">
            <span>JobLib</span><br><br>
            <img height="64px" src="https://joblib.readthedocs.io/en/latest/_static/joblib_logo.svg">
          </td>
        <tr valign="top">
          <td width="25%" align="center">
            <span>XGBoost</span><br><br>
            <img height="64px" src="https://miro.medium.com/max/720/1*yhE3CBwTrlXcAIvNJNTQiA.png">
          </td>
          <td width="25%" align="center">
            <span>CatBoost</span><br><br>
            <img height="64px" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjifalk1omESSaUXBBKVI16qaoPQYPxya-Sd5Gm__po7WPeP8R3aDBZD-hnYZbWYeSdg&usqp=CAU">
          </td>
          <td width="25%" align="center">
            <span>Pandas Profiling</span><br><br>
            <img height="64px" src="https://camo.githubusercontent.com/8a45c0936d6113b12b7b32942f448270eda8f714665ba8629f36c291f0ccd5fd/68747470733a2f2f70616e6461732d70726f66696c696e672e6769746875622e696f2f70616e6461732d70726f66696c696e672f646f63732f6173736574732f6c6f676f5f6865616465722e706e67">
          </td>
          <td width="25%" align="center">
            <span>Streamlit</span><br><br>
            <img height="64px" src="https://assets.website-files.com/5dc3b47ddc6c0c2a1af74ad0/5e18182ad27bcfbb9dff263a_RGB_Logo_Horizontal_Color_Light_Bg-p-1080.png">
          </td>
        <tr valign="top">
          <td width="25%" align="center">
            <span>YellowBrick</span><br><br>
            <img height="64px" src="https://backend.openteams.com/media/CACHE/images/projects/03wsmfn2o0mbdepb1p1y0ykwpj5cbffvwtpb90hx/dce34eea84527d611b97ea79af75f966.png">
          </td>
        </tr>
      </tbody>
    </table>

## EDA

**Dataset describe:**

- RowNumber: the row number.
- CustomerID: customer unique id.
- Surname: customer surname.
- CreditScore: customer credit score.
- Geography: customer country.
- Gender: customer gender.
- Age: customer age.
- Tenure: customer time of activity in years.
- Balance: monetary values in the customer account.
- NumOfProducts: number os banck products used by the customer.
- HasCrCard: if the customer has or not credict card.
- IsActiveMember: is the customer is active or not. Active: at least one bank movimentation in the past 12 months.
- EstimateSalary: customer salary estimate.
- Exited: if the customer is in churn or not.

#### Data Describe

|                 |   count |        mean |          std |    min |      25% |      50% |       75% |    max |
|:----------------|--------:|------------:|-------------:|-------:|---------:|---------:|----------:|-------:|
| RowNumber       |   10000 |   5000.5    |  2886.9      |   1    |  2500.75 |   5000.5 |   7500.25 |  10000 |
| CreditScore     |   10000 |    650.529  |    96.6533   | 350    |   584    |    652   |    718    |    850 |
| Age             |   10000 |     38.9218 |    10.4878   |  18    |    32    |     37   |     44    |     92 |
| Tenure          |   10000 |      5.0128 |     2.89217  |   0    |     3    |      5   |      7    |     10 |
| Balance         |   10000 |  76485.9    | 62397.4      |   0    |     0    |  97198.5 | 127644    | 250898 |
| NumOfProducts   |   10000 |      1.5302 |     0.581654 |   1    |     1    |      1   |      2    |      4 |
| HasCrCard       |   10000 |      0.7055 |     0.45584  |   0    |     0    |      1   |      1    |      1 |
| IsActiveMember  |   10000 |      0.5151 |     0.499797 |   0    |     0    |      1   |      1    |      1 |
| EstimatedSalary |   10000 | 100090      | 57510.5      |  11.58 | 51002.1  | 100194   | 149388    | 199992 |
| Exited          |   10000 |      0.2037 |     0.402769 |   0    |     0    |


#### **Hypothesis Formulation**

H1. Male customers are mole likely to churn than female customers.

  
  - Accordingly the data, women are more likely to churn than men.
  - More than 25% of women have exited the bank, while only 16,45% of man have exited.


![gender](https://user-images.githubusercontent.com/71295866/135167519-4928c67c-4358-4484-ba5e-1c056be3c94c.jpg)

<h4 align="center">H1 Validation: FALSE</h4>
  

H2. Younger customers are mole likely to churn than older customers.

  - Accordingly the data, elder customers are more likely to churn than younger.
  - 23% of elder customers have exited the bank, while only 8% of younger customers have exited.

![customers](https://user-images.githubusercontent.com/71295866/135167984-c83870c9-8e91-4060-ab5a-342311edffd5.jpg)

<h4 align="center">H2 Validation: FALSE</h4>

H3. Customers with less time as customers are mole likely to churn.

  - Accordingly the data, customers with less time as customers have almost the same exited proportion as customer with more time.
  - Customer with less than 4 years as customer have a range from 19% to 23% outings, while customer with more than 3 years have a range from 17% to 22%, almost the same.


![tenure](https://user-images.githubusercontent.com/71295866/135168153-e13163f8-d187-4036-baa9-1bbb3ee9d8b6.jpg)


<h4 align="center">H3 Validation: INCONCLUSIVE</h4>

H4. Customers with less balance values are more likely to churn.

  - Accordingly the data, customers with lower balance are more likely to remain customers.
  - Customer with balance lower than €10000 are more likely to remain customers. Only 13,8% of lower balance customers are 'Exited', while more than 24% of the customers with more than €10000 have exited.

![lower10k](https://user-images.githubusercontent.com/71295866/135170595-78827dfd-d2a3-4522-86f1-3cf21c38fdbd.jpg)

![bigger10k](https://user-images.githubusercontent.com/71295866/135170610-b5436bcd-7677-4c11-9be4-c44d037a8f1f.jpg)


<h4 align="center">H4 Validation: FALSE</h4>

H5. Customer with less bank products are more likely to churn.

H6. Customer without creditcard are more likely to churn.

H7. Active members are less likely to churn.

H8. Customer with bigger estimated salary are less likely to churn.

H9. Customers from which country are more likely to exit?



    

## Model Deploy

## Next Steps

## Conclusion
